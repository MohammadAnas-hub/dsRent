from django.urls import path
from API.views.UserView import *

app_name = 'API'

urlpatterns = [

    # ======== Users Enpoints =======
    path("get-all-users", GetAllUsersView, name="GetAllUsers"),
    path("get-user-by-id", GeUserByIDView, name="GetUserByID"),
    path("create-user", CreateUserView, name="CreateUser"),
    path("update-user", UpdateUserView, name="UpdateUser"),
    path("delete-user", DeleteUserView, name="DeleteUser"),

]