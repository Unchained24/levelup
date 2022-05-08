from django.urls import path,include
from users import views

urlpatterns = [
  

    path('',views.LoginAdmin, name="login"),
    path('view',views.ViewDetails, name="view"),
    path('logout',views.logoutUser, name="logout"),
]
