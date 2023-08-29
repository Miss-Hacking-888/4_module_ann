from django.urls import path
from 

urlpatterns = [
    path('login/',login_view,  name ='login')
    path('profile/',profile_view,  name ='profile')
    path('logout/',logout_view,  name ='logout')

]