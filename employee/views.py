from django.shortcuts import render
from .models import Employee
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rest_framework import viewsets
from rest_framework import permissions
from django.http import JsonResponse
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
# Create your views here.

def index(request):
    employee = Employee.objects.all()
    page = request.GET.get('page', 1)
    
    paginator = Paginator(employee, 10)
    try:
        employee = paginator.page(page)
    except PageNotAnInteger:
        employee = paginator.page(1)
    except EmptyPage:
        employee = paginator.page(paginator.num_pages)
    context = {'employee':employee}
    return render(request,'Home/index.html',context)

@api_view(['GET'])
def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serialize = EmployeeSerializer(employees,many = True)
        return JsonResponse(serialize.data,safe=False)

""" def index(request):
 user_list = User.objects.all()
 page = request.GET.get('page', 1)

 paginator = Paginator(user_list, 10)
 try:
     users = paginator.page(page)
 except PageNotAnInteger:
     users = paginator.page(1)
 except EmptyPage:
     users = paginator.page(paginator.num_pages)

 return render(request, 'core/user_list.html', { 'users': users }) """