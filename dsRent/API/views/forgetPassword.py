from API.models import UserModel, ForgetPassword
from API.serializers import UserSerializer, ForgetPasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import datetime
import jwt
from django.contrib.auth.hashers import make_password


@api_view(['GET'])
def forgetPassword(request):
    UserId = request.query_params.get('user_id')
    # If UserId is not provided
    if UserId is None:
        return Response({"data": "User Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = UserModel.objects.get(userId=UserId)
        # serializer = UserSerializer(user, many=False)


        payload = {
                'id':str(user.userId),
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=1),
                'iat':datetime.datetime.utcnow()
            }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        tempData = {"user":UserId, "token":token}
        model = ForgetPassword
        serializers = ForgetPasswordSerializer(model, data=tempData)
        
        if serializers.is_valid():
            serializers.save()
            print(1111111111111111111111111111111111111111111111111111111111111111111111)

            # return Response({"token":token}, status=status.HTTP_200_OK)
        return Response({"data":serializers.data},status=status.HTTP_201_CREATED)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdatePassword(request):
    ReqData = request.data
    try:
        ReqData['password'] = make_password(request.data['password'])
        user = UserModel.objects.get(email=ReqData['email'])
        serializers = UserSerializer(instance=user, data=ReqData, many=False)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)