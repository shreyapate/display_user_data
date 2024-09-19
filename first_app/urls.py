from first_app.views import GetUserDetails
from django.urls import path


urlpatterns = [
    path("get/user/details/", GetUserDetails.as_view())
]
