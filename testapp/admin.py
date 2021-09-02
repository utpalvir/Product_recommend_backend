from django.contrib import admin
from . models import IndustryDomain, Output, SaleStage, product
from . models import division
from .models import IndustryDomain
from .models import projects
from .models import storeinfo
from .models import stage 
from .models import SaleStage 
from .models import Output, customer, Region, resource, csm, questionAnswer

admin.site.register(product)
admin.site.register(division)
admin.site.register(IndustryDomain)
admin.site.register(projects)
admin.site.register(storeinfo)
admin.site.register(SaleStage)
admin.site.register(Output)
admin.site.register(stage)
admin.site.register(customer)
admin.site.register(Region)
admin.site.register(resource)
admin.site.register(questionAnswer)
admin.site.register(csm)





# Register your models here.
