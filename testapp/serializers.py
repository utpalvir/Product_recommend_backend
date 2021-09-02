from rest_framework import serializers
from testapp.models import product
from testapp.models import division
from testapp.models import IndustryDomain, questionAnswer, customer, Region, resource, Output, projects



#from django.contrib.auth.models import User


class productSerializer(serializers.ModelSerializer):

    class Meta:
        model = product
        fields='__all__'
        #fields = ('productid',product_name')

class divisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = division
        fields='__all__'

class IndustryDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryDomain
        fields = '__all__'
class questionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = questionAnswer
        fields = '__all__'
class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=customer
        fields = '__all__'
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Region
        fields='__all__'
class resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=resource
        fields='__all__'
class outputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Output
        fields='__all__'
class projectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=projects
        fields=('projectid','projectname','customername','resource','Allocation_start_date','Allocation_end_date')







"""class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')
"""
