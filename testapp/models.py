from django.db import models
from django.contrib.auth.models import User
from django.db import *
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ManyToManyField
from datetime import date

# Create your models here.


        
class division(models.Model):
    divisionid = models.CharField(primary_key=True, max_length=5)  # Field name made lowercase.
    division_name = models.CharField(max_length=20)
    def __str__(self):
        return self.divisionid
class IndustryDomain(models.Model):
    ind_id = models.CharField(primary_key=True,max_length=5)
    ind_name = models.CharField(max_length=40)
    def __str__(self):
        return self.ind_id

class product(models.Model):
    productid = models.CharField(primary_key=True, max_length=5)  # Field name made lowercase.
    product_name = models.CharField(max_length=200)
    division = models.ForeignKey(division,on_delete=models.CASCADE, default=10)
    industry = models.ForeignKey(IndustryDomain,on_delete=models.CASCADE,default=100)
    def __str__(self):
        return self.product_name
class Region(models.Model):
    RegionId = models.CharField(primary_key=True,max_length=15)
    RegionName = models.CharField(max_length=15)
    def __str__(self):
        return self.RegionName

class customer(models.Model):
    CustomerId = models.CharField(primary_key=True, max_length=20)
    ProductCount = models.CharField(max_length=20)
    CustomerName = models.CharField(max_length=20)
    count = models.CharField(max_length=20)
    Region = models.ForeignKey(Region,on_delete = models.CASCADE ,default="")
    def __str__(self):
        return self.CustomerName
#I was somewhere here
class resource(models.Model):
    ResourceId = models.CharField(primary_key=True,max_length=30)
    ResourceEmail = models.CharField(max_length=50)
    ResourceFirstName = models.CharField(max_length=30)
    ResourceLastName = models.CharField(max_length = 20)
    ResourceShortName = models.CharField(max_length = 20)
    def __str__(self):
        full_name=self.ResourceFirstName + self.ResourceLastName
        return self.ResourceId

class csm(models.Model):
    csmid = models.CharField(primary_key=True ,max_length=30)
    csmFirstName = models.CharField(max_length=30)
    csmLastName = models.CharField(max_length = 20)
    csmShortName = models.CharField(max_length = 20)
    def __str__(self):
        return self.csmShortName

class projects(models.Model):
    projectid = models.CharField(primary_key=True, max_length=10)  # Field name made lowercase.
    projectname = models.CharField( max_length=200)  # Field name made lowercase.
    customername = models.ForeignKey(customer,on_delete=models.CASCADE,default="")  # Field name made lowercase.
    country = models.CharField(max_length=10, blank=True, null=True)
    resource = models.ForeignKey(resource,on_delete = models.CASCADE,default=" ")
    customer_success_manager = models.ForeignKey(csm,on_delete=models.CASCADE,default=" ")
    Allocation_start_date = models.DateField(default=date.today())
    Allocation_end_date  = models.DateField(default=date.today())
    def __self__(self):
        return u"%s" % (self.projectname)
    def __return_all__(self):
        return u"%s %s %s" % (self.projectname, self.customername, self.country)
        # return u"%s %s %s" % (self.manufacturer, self.model_type, self.equipment_type)

    #class Meta:
        #managed = False
        #db_table = 'projects'


class storeinfo(models.Model):
    
    project = models.ForeignKey(projects,on_delete=models.CASCADE,default=100)  # Field name made lowercase.
    resource = models.ForeignKey(resource, max_length=40,on_delete=models.CASCADE)
    #customer = models.ManyToManyField(projects , on_delete=models.CASCADE, default="HCCI")
    customer = models.ForeignKey(customer,on_delete=models.CASCADE,default="")
    direct_product = models.ForeignKey(product,on_delete=models.CASCADE,default="")
    storeinfo_text = models.CharField(max_length=5000, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return (self.resource + "'s Information")
    def __all__(self):
        return u"%s %s %s %s %s" % (self.project ,self.resource,self.customer,self.direct_product,self.storeinfo_text)
    #def __str__(self):
       #return u"%s %s %s %s" % (self.resource_name,self.resource_email,self.storeinfo_text)


    #class Meta:
        #managed = False
        #db_table = 'storeinfo'
class Output(models.Model):
    outputId = models.CharField(primary_key=True,max_length=100, default=500)
    resource = models.ForeignKey(resource,on_delete=models.CASCADE,default="")
    recommended_products = models.ForeignKey(product,on_delete=models.CASCADE,default=1)
    customer = models.ForeignKey(customer,on_delete=models.CASCADE,default=10)
    def __str__(self):
        #queryset = self._meta.model.objects.all()
        #return queryset
        return self.outputId

class stage(models.Model):
    stageId = models.CharField(primary_key=True , max_length=10,default=1)
    stageName = models.CharField(max_length=20 , default="")
    def __str__(self):
        return self.stageId 
    
class SaleStage(models.Model):
    sales_Name = models.CharField(primary_key=True , max_length= 30, default= "" )
    sales_stage = models.ForeignKey(stage , on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    def __str__(self):
        return self.sales_email
class questionAnswer(models.Model):
    questionId = models.CharField(primary_key=True,max_length=30)
    question = models.CharField(max_length=2000,default="Test")
    answer = models.ForeignKey(product, on_delete=models.CASCADE,default="True")
    #ustomer = models.ForeignKey(customer, on_delete=models.CASCADE, default=" ")
    textinput = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return u"%s %s %s %s" % (self.questionId , self.question,self.answer,self.textinput)

