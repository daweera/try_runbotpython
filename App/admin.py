from django.contrib import admin
from App.models import Employee # ModuleNotFoundError: No module named 'App' ?

class EmpolyeeAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'occupation', 'gender']
    search_fields =['name']
    list_per_page = 8
    
admin.site.register(Employee,EmpolyeeAdmin)
    
    

