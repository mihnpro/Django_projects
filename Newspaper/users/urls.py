from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.Logout.as_view(), name='logout'),
]