from django.contrib import admin
from .models import Nutrient, Usermeal, Usermealnutrientlink, Usermealevaluation

admin.site.register(Nutrient)
admin.site.register(Usermeal)
admin.site.register(Usermealnutrientlink)
admin.site.register(Usermealevaluation)
# Register your models here.
