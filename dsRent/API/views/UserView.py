from rest_framework import generics
from API.models import UserModel
from API.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from django.contrib.auth.hashers import make_password
from rest_framework import mixins
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


# This Helps To Develop CRUD APIs Of UserModel (All at one set)


# ====== User Views Starts ========
@api_view(['GET'])
def GetAllUsersView(request):
    AllUsers = UserModel.objects.all()
    serializer_class = UserSerializer(AllUsers, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GeUserByIDView(request):
    # Getting UserId in uuid (Queru Param ?userId=)
    UserId = request.query_params.get('user_id')
    # If UserId is not provided
    if UserId is None:
        return Response({"data": "User Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        UserData = UserModel.objects.get(userId=UserId)
        serializer = UserSerializer(UserData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateUserView(request):
    ReqData = request.data
    try:
        ReqData['password'] = make_password(request.data['password'])
        serializers = UserSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdateUserView(request):
    # Getting UserId in uuid (Queru Param ?userId=)
    UserId = request.query_params.get('user_id')
    # If UserId is not provided
    if UserId is None:
        return Response({"data": "User Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        usrmodel = UserModel.objects.get(userId=UserId)
        # serializers = UserSerializer(usrmodel, many=False)        
        print(usrmodel)
        serializers = UserSerializer(instance=usrmodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteUserView(request):
    # Getting UserId in uuid (Queru Param ?userId=)
    UserId = request.query_params.get('user_id')
    # If UserId is not provided
    if UserId is None:
        return Response({"data": "User Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        usrmodel = UserModel.objects.get(userId=UserId)
        usrmodel.delete()
        return Response({"data": "User Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    