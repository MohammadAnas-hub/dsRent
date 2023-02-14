from rest_framework import generics
from API.models import Service
from API.serializers import ServiceSerializer
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


# ====== Service Views Starts ========
@api_view(['GET'])
def GetAllServiceView(request):
    AllServices = Service.objects.all()
    serializer_class = ServiceSerializer(AllUsers, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetServiceByIDView(request):
    # Getting serviceId in uuid (Queru Param ?serviceId=)
    serviceId = request.query_params.get('service_id')
    # If serviceId is not provided
    if serviceId is None:
        return Response({"data": "Service Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ServiceData = Service.objects.get(serviceId=serviceId)
        serializer = ServiceSerializer(UserData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateServiceView(request):
    ReqData = request.data
    try:
        ReqData['password'] = make_password(request.data['password'])
        serializers = ServiceSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdateServiceView(request):
    # Getting serviceId in uuid (Queru Param ?userId=)
    serviceId = request.query_params.get('service_id')
    # If serviceId is not provided
    if serviceId is None:
        return Response({"data": "Service Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        sermodel = Service.objects.get(serviceId=serviceId)
        print(usrmodel)
        serializers = ServiceSerializer(instance=sermodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteServiceView(request):
    # Getting serviceId in uuid (Queru Param ?serviceId=)
    serviceId = request.query_params.get('service_id')
    # If serviceId is not provided
    if serviceId is None:
        return Response({"data": "Service Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        sermodel = Service.objects.get(serviceId=serviceId)
        sermodel.delete()
        return Response({"data": "Service Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    