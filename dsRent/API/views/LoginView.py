from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from API.serializers import RegisterSerializer
from rest_framework import generics
import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from API.models import UserModel
from rest_framework.decorators import api_view
import jwt
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
# from Exceptions.ExceptionsClass import LoginException
from django.core import exceptions


@api_view(['POST'])
def RegisterView(request):
    ReqData = request.data
    try:
        email = request.data['email']
        user = UserModel.objects.filter(email=email).first()
        if user is not None:
            return Response("Email/Phone Already Exists",status=status.HTTP_400_BAD_REQUEST)
        ReqData['password'] = make_password(request.data['password'])
        serializers = RegisterSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            payload = {
                # 'id':str(serializers.userId),
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=10),
                'iat':datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            print(token)
            return Response({"data":serializers.data, "token":token},status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    def post(self, request):
        try:
            email = request.data['email']
            password = request.data['password']


            user = UserModel.objects.filter(email=email).first()
            if user is None:
                raise exceptions.ValidationError("Use Not Found")

            if not check_password(password, user.password):
                raise exceptions.ValidationError("Incorrect Password")

            payload = {
                'id':str(user.userId),
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=1),
                'iat':datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')
            
            data = {
                'token':token,
                'email':email,
                'firstName':user.firstName,
                'lastName':user.lastName,
                'userId':str(user.userId)
            }

            return Response({"data":data}, status = status.HTTP_200_OK)
        except LoginException as err:
            return Response(str(err), status = status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
        except Exception as err:
            print("Error: " + str(err))
            return Response(str(err), status = status.HTTP_500_INTERNAL_SERVER_ERROR)