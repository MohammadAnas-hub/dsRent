from API.models import VehicleDetails
from API.serializers import VehicleDetailsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from rest_framework import mixins
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


# ====== Vehicle Details Views Starts ========
@api_view(['GET'])
def GetAllVehicleDetailsView(request):
    AllVehicle = VehicleDetails.objects.all()
    serializer_class = VehicleDetailsSerializer(AllVehicle, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetVehicleByIDView(request):
    # Getting VehicleID in uuid (Queru Param ?vehicle_id=)
    VehicleID = request.query_params.get('vehicle_id')
    # If VehicleID is not provided
    if VehicleID is None:
        return Response({"data": "Vehicle Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        VehicleData = VehicleDetails.objects.get(vehicleDetailsID=VehicleID)
        serializer = VehicleDetailsSerializer(VehicleData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateVechileDetailsView(request):
    ReqData = request.data
    try:
        # ReqData['password'] = make_password(request.data['password'])
        serializers = VehicleDetailsSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['DELETE'])
def DeleteVehicleDetailsView(request):
    # Getting Vehicle in uuid (Queru Param ?VehicleId=)
    VehicleID = request.query_params.get('vehicle_id')
    # If UserId is not provided
    if VehicleID is None:
        return Response({"data": "Vehicle Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        vehmodel = VehicleDetails.objects.get(vehicleDetailsID=VehicleID)
        vehmodel.delete()
        return Response({"data": "VehicleDetails Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)