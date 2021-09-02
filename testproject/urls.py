"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from testapp.models import division
from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from testapp import views
from django.urls import include, re_path



urlpatterns = [
    path('admin/', admin.site.urls),
    #re_path(r'^api/division/',views.divisionList.as_view()),
    re_path(r'^api/product/', views.productList.as_view()),
    re_path(r'^api/division/',views.divisionList.as_view()),
    re_path(r'^api/IndustryList',views.IndustryList.as_view()),
    re_path(r'^api/QnAList',views.QnAList.as_view()),
    re_path(r'^api/CustomerList',views.CustomerList.as_view()),
    re_path(r'^api/RegionList',views.RegionList.as_view()),
    re_path(r'^api/ResourceList',views.ResourceList.as_view()),
    re_path(r'^api/outputview',views.outputview.as_view()),
    re_path(r'^api/projectList',views.projectList.as_view())

]
