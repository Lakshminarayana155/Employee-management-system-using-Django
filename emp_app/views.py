from django.shortcuts import render, HttpResponse
from .models import Role, Employee, Department
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,'index.htm')

def all_emply(request):
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    print(context)
    return render(request,'all_emply.htm',context)

def add_emply(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone=request.POST['phone']
        salary=int(request.POST['salary'])
        dept=int(request.POST['dept'])
        bonus=int(request.POST['bonus'])
        role=request.POST['role']
        new_emp=Employee(first_name=first_name,last_name= last_name, phone=phone, salary= salary, bonus= bonus,dept_id= dept, role_id= role, hire_date= datetime.now())
        new_emp.save()
        return HttpResponse("Employee added sucessfully")
    elif request.method=='GET':

        return render(request,'add_emply.htm')
    else:
        return HttpResponse("An exceptin occured! Employeed has not been added")

def remove_emply(request,emp_id=0):
    if emp_id:
        try:
            emply_to_be_deleted=Employee.objects.get(id=emp_id)
            emply_to_be_deleted.delete()
            return HttpResponse("Employee remvoed sucessfully")
        except:
            return HttpResponse("Please select an valid employee")

    emps=Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request,'remove_emply',context)

def filter_emply(request):
    if request.method =="POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps=Employee.objects.all()

        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps=emps.filter(dept__name__icontains = dept)
        if role:
            emps=emps.filter(role__name__icontains = role)
        
        context = {
            'emps' : emps
        }

        return render(request,'all_emply.htm',context)
    elif request.method == 'GET':
        return render(request,'filter_emply.htm')
    else:
        return HttpResponse('An Exception occured')




    return render(request,'filter_emply.htm')