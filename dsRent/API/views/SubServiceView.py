from rest_framework import generics
from API.models import SubServices
from API.serializers import SubServiceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from django.contrib.auth.hashers import make_password
from rest_framework import mixins
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


# This Helps To Develop CRUD APIs Of SubService (All at one set)


# ====== Sub Service Views Starts ========
@api_view(['GET'])
def GetAllSubServicesView(request):
    AllSubServices = SubServices.objects.all()
    serializer_class = SubServiceSerializer(AllSubServices, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetSubServicesByIDView(request):
    # Getting subServiceId in uuid (Queru Param ?subServiceId=)
    subServiceId = request.query_params.get('subService_id')
    # If subServiceId is not provided
    if subServiceId is None:
        return Response({"data": "subService Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        subServiceData = SubServices.objects.get(subServiceId=subServiceId)
        serializer = SubServiceSerializer(subServiceData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateSubServicesView(request):
    ReqData = request.data
    try:
        ReqData['password'] = make_password(request.data['password'])
        serializers = SubServiceSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdateSubServicesView(request):
    # Getting subServiceId in uuid (Queru Param ?subServiceId=)
    subServiceId = request.query_params.get('subService_id')
    # If subServiceId is not provided
    if subServiceId is None:
        return Response({"data": "Sub Service Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        sermodel = SubServices.objects.get(serviceId=serviceId)
        print(usrmodel)
        serializers = SubServiceSerializer(instance=sermodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteSubServicesView(request):
    # Getting subServiceId in uuid (Queru Param ?subServiceId=)
    subServiceId = request.query_params.get('subService_id')
    # If subServiceId is not provided
    if subServiceId is None:
        return Response({"data": "Sub Service Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        sermodel = SubServiceSerializer.objects.get(serviceId=serviceId)
        sermodel.delete()
        return Response({"data": "Sub Service Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    