#from models import User
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from testapp import serializers
from rest_framework import generics
from . models import IndustryDomain, customer, division, product, projects, questionAnswer, Region, resource, Output, projects
from . serializers import productSerializer
from . serializers import divisionSerializer
from . serializers import IndustryDomainSerializer, questionAnswerSerializer, customerSerializer, RegionSerializer, resourceSerializer,outputSerializer,projectsSerializer
from itertools import groupby


#from .serializers import UserSerializer


class productList(APIView):
    def get(self , request):
        product1 =product.objects.all()
        serializer = productSerializer(product1 , many= True)
        return Response(serializer.data)
    def post(self):
        pass

class divisionList(APIView):
    def get(self ,request):
        division1 = division.objects.all()
        serializer = divisionSerializer(division1 , many=True)
        return Response(serializer.data)
    def post(self):
        pass

class IndustryList(APIView):
    def get(self, request):
        ind1 = IndustryDomain.objects.all()
        serializer = IndustryDomainSerializer(ind1,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class QnAList(APIView):
    def get(self,request):
        qnaObj1 = questionAnswer.objects.all()
        serializer = questionAnswerSerializer(qnaObj1,many=True)
        return Response(serializer.data)
    def post(self):
        pass

class CustomerList(APIView):
    def get(self,request):
        cust1 = customer.objects.all()
        serializer = customerSerializer(cust1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
class RegionList(APIView):
    def get(self,request):
        Region1 = Region.objects.all()
        serializer =RegionSerializer(Region1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
class ResourceList(APIView):
    def get(self,request):
        resource1 = resource.objects.all()
        serializer =resourceSerializer(resource1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
class outputview(APIView):
    def get(self,request):
        output1 = Output.objects.all()
        print(output1)
        serializer = outputSerializer(output1,many=True)
        #print(serializer)
        #print(serializer.data)
        #print(serializer.data.OrderedDict.recommended_products)
        #testlist=[]
        """def key_fun(k):
            return k['serializer.data.recommended_products']
        for key,value in groupby(serializer.data, key_fun):
            testlist.append(key, list(value))
        """
        return Response(serializer.data)
    def post(self):
        pass
class projectList(APIView):
    def get(self,request):
        project1=projects.objects.all()
        serializer = projectsSerializer(project1,many=True)
        return Response(serializer.data)
    def post(self):
        pass
    


    









"""class UserList(APIView):
    def get(self,request):
        usr1 = User.objects.all()
        serializer = UserSerializer(usr1 , many=True)
        return Response(serializer.data)
    def post(self):
        pass
"""


"""
class DirContents(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        files = FileObj.objects.filter(parent=kwargs.get('dir_id'))
        dirs = DirObj.objects.filter(parent=kwargs.get('dir_id'))

        context = {
            "request": request,
        }

        files_serializer = FileObjSerializer(files, many=True, context=context)
        dirs_serializer = DirObjSerializer(dirs, many=True, context=context)

        response = files_serializer.data + dirs_serializer.data

        return Response(response)
"""

# Create your views here.
