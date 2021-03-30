from django.urls import path,include,re_path
from . import views
from django.conf import  settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name="accounts"

urlpatterns = [
    path('register/',views.registerPage, name="register-page"),
    path('login/',views.loginPage, name="login-page"),
    path('',views.landingPage, name="home-page"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('about-us/', views.aboutusPage, name="aboutus-page"),
    path('contact-us/', views.contactusPage, name="contactus-page"),
    path('galleries/', views.galleriesPage, name="galleries-page"),

    
]