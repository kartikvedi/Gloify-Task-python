from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.bookslist),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
]
