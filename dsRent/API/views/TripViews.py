from API.models import Trips
from API.serializers import TripsSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from rest_framework import mixins
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


# ====== Trip Views Starts ========
@api_view(['GET'])
def GetAllTripsView(request):
    AllTrips = Trips.objects.all()
    serializer_class = TripsSerializer(AllTrips, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def GetTripByIDView(request):
    # Getting VehicleID in uuid (Queru Param ?trip_id=)
    TripID = request.query_params.get('trip_id')
    # If TripID is not provided
    if TripID is None:
        return Response({"data": "Trip Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        TripData = Trips.objects.get(tripsId=TripID)
        serializer = TripsSerializer(TripData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateTripView(request):
    ReqData = request.data
    try:
        # ReqData['password'] = make_password(request.data['password'])
        serializers = TripsSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PATCH'])
def UpdateTripView(request):
    # Getting TripId in uuid (Queru Param ?trip_id=)
    TripId = request.query_params.get('trip_id')
    # If TripId is not provided
    if TripId is None:
        return Response({"data": "Trip Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        trpmodel = Trips.objects.get(tripsId=TripId)
        # serializers = UserSerializer(usrmodel, many=False)        
        # print(usrmodel)
        serializers = TripsSerializer(instance=trpmodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteTripsView(request):
    # Getting Vehicle in uuid (Queru Param ?VehicleId=)
    TripID = request.query_params.get('trip_id')
    # If TripID is not provided
    if TripID is None:
        return Response({"data": "Trip Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        trpmodel = Trips.objects.get(tripsId=TripID)
        trpmodel.delete()
        return Response({"data": "Trips Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)