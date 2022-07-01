from django.shortcuts import render
from App.models import Employee # ModuleNotFoundError: No module named 'App'

# Function to render Homepage
def home(request):
    employee_list = Employee.objects.all()
    return render(request, "home.html", {"employees":employee_list})
