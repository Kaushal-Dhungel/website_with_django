from django.urls import path

from . import views


urlpatterns=[
    
    path('',views.mainbody, name = "mainbody"),
    path('mainaboutus', views.mainaboutus, name='mainaboutus'),
    path('newsignup', views.newsignup , name = 'newsignup'),
    path('login', views.login, name = 'login'),
    #path('register', views.register, name = 'register'),
    path('profile', views.profile, name = 'profile'),
    path('logout', views.logout, name = 'logout'),
    path('mainbody',views.mainbody, name = "mainbody"),
    path('searchresult',views.searchresult, name = "searchresult")
    
]