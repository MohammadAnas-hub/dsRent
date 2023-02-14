from django.urls import path
from API.views.UserView import *
from API.views.VehicleDetailsView import *
from API.views.forgetPassword import *
from API.views.ServiceView import *
from API.views.SubServiceView import *
from API.views.BookingsView import *
from API.views.LoginView import *

app_name = 'API'

urlpatterns = [

    # ======== Users Enpoints =======
    path("get-all-users", GetAllUsersView, name="GetAllUsers"),
    path("get-user-by-id", GeUserByIDView, name="GetUserByID"),
    path("create-user", CreateUserView, name="CreateUser"),
    path("update-user", UpdateUserView, name="UpdateUser"),
    path("delete-user", DeleteUserView, name="DeleteUser"),

    # ========= Login =========
    path("login", LoginView.as_view(), name="LoginApi"),
    path('register', RegisterView, name='Register'),


    # forget password
    path("forget-password", forgetPassword, name="ForgetPassword"),
    path("update-password", UpdatePassword, name="UpdatePassword"),

    #============= service Endpoints==========
    path("get-all-services", GetAllServiceView, name="GetAllServices"),
    path("get-service-by-id", GetServiceByIDView, name="GetServicesByID"),
    path("create-service", CreateServiceView, name="CreateServices"),
    path("update-service", UpdateServiceView, name="UpdateServices"),
    path("delete-service", DeleteServiceView, name="DeleteServices"),


    # ============ Sub Services Endpoints ==========
    path("get-all-subservices", GetAllSubServicesView, name="GetAllSubServices"),
    path("get-subservice-by-id", GetSubServicesByIDView, name="GetSubsServicesByID"),
    path("create-subservice", CreateSubServicesView, name="CreateSubServices"),
    path("update-subservice", UpdateSubServicesView, name="UpdateSubServices"),
    path("delete-subservice", DeleteSubServicesView, name="DeleteSubServices"),


    # ======== VehicleDetails Enpoints =======
    path("get-all-vehicleDetails", GetAllVehicleDetailsView, name="GetAllVehicleDetails"),
    path("get-vehicleDetails-by-id", GetVehicleByIDView, name="GetVehicleDetailsByID"),
    path("create-vehicleDetails", CreateVechileDetailsView, name="CreateVehicleDetails"),
    path("delete-vehicleDetails", DeleteVehicleDetailsView, name="DeleteVehicleDetails"),


    # ======== Bookings Enpoints =======
    path("get-all-bookings", GetAllBookingsView, name="GetAllBookings"),
    path("get-bookings-by-id", GetBookingsByIDView, name="GetBookingsByID"),
    path("create-bookings", CreateBookingsView, name="CreateBookings"),
    path("update-bookings", UpdateBookingsView, name="UpdateBookings"),
    path("delete-bookings", DeleteBookingsView, name="DeleteBookings"),

]