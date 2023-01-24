from django.urls import path
from API.views.UserView import *
from API.views.VehicleDetailsView import *
from API.views.TripViews import *
from API.views.forgetPassword import *

app_name = 'API'

urlpatterns = [

    # ======== Users Enpoints =======
    path("get-all-users", GetAllUsersView, name="GetAllUsers"),
    path("get-user-by-id", GeUserByIDView, name="GetUserByID"),
    path("create-user", CreateUserView, name="CreateUser"),
    path("update-user", UpdateUserView, name="UpdateUser"),
    path("delete-user", DeleteUserView, name="DeleteUser"),

    # forget password
    path("forget-password", forgetPassword, name="ForgetPassword"),
    path("update-password", UpdatePassword, name="UpdatePassword"),


    # ======== VehicleDetails Enpoints =======
    path("get-all-vehicleDetails", GetAllVehicleDetailsView, name="GetAllVehicleDetails"),
    path("get-vehicleDetails-by-id", GetVehicleByIDView, name="GetVehicleDetailsByID"),
    path("create-vehicleDetails", CreateVechileDetailsView, name="CreateVehicleDetails"),
    path("delete-vehicleDetails", DeleteVehicleDetailsView, name="DeleteVehicleDetails"),


    # ======== Trip Enpoints =======
    path("get-all-trips", GetAllTripsView, name="GetAllTrips"),
    path("get-trip-by-id", GetTripByIDView, name="GetTripByID"),
    path("create-trip", CreateTripView, name="CreateTrip"),
    path("update-trip", UpdateTripView, name="UpdateTrip"),
    path("delete-trip", DeleteTripsView, name="DeleteTrip"),

]