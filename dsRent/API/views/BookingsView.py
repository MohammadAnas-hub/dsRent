from rest_framework import generics
from API.models import Bookings
from API.serializers import BookingSerializer
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


# ====== Booking Views Starts ========
@api_view(['GET'])
def GetAllBookingsView(request):
    AllBookings = Bookings.objects.all()
    serializer_class = BookingSerializer(AllBookings, many=True)
    return Response({"data":serializer_class.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def GetBookingsByIDView(request):
    # Getting tripId in uuid (Queru Param ?tripId=)
    tripId = request.query_params.get('trip_id')
    # If tripId is not provided
    if tripId is None:
        return Response({"data": "Trip Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        TripData = Bookings.objects.get(tripId=tripId)
        serializer = BookingSerializer(TripData, many=False)
        return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    except Exception as err:
        print(err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def CreateBookingsView(request):
    ReqData = request.data
    try:
        ReqData['password'] = make_password(request.data['password'])
        serializers = BookingSerializer(data=ReqData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print(err)
        return Response(serializers.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['PATCH'])
def UpdateBookingsView(request):
    # Getting tripId in uuid (Queru Param ?tripId=)
    tripId = request.query_params.get('trip_id')
    # If tripId is not provided
    if tripId is None:
        return Response({"data": "Trip Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    ReqData = request.data
    try:
        trpmodel = Bookings.objects.get(tripId=tripId)
        serializers = BookingSerializer(instance=trpmodel,data=ReqData, many=False)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        print("Error ==>", err)
        return Response(str(err), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def DeleteBookingsView(request):
    # Getting tripId in uuid (Queru Param ?tripId=)
    tripId = request.query_params.get('trip_id')
    # If tripId is not provided
    if tripId is None:
        return Response({"data": "Trip Id Not Provided"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        trpmodel = Bookings.objects.get(tripId=tripId)
        trpmodel.delete()
        return Response({"data": "Trip Model Deleted"}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({"msg": err.message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    