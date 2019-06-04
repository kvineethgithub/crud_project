from django.shortcuts import render,redirect,get_object_or_404
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from  django.http import HttpResponse

def home(request):
    form=EmployeeForm()
    return render(request,'index.html',{'form':form})
def create(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Added successfully")
    return redirect(read)

def read(request):
    emps=Employee.objects.all()
    return render(request,'result.html',{'emps':emps})
def delete(request,id):
    emps=Employee.objects.filter(id=id)
    emps.delete()
    return redirect(read)
def update(request,id):

    emps=Employee.objects.get(id=id)
    form=EmployeeForm(instance=emps)

    return render(request,'update.html',{'form':form,'emps':emps})

def updated(request,id):
    if request.method=='POST':
        instance=get_object_or_404(Employee,id=id)
        form=EmployeeForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            # Employee.objects.filter(id=id).update(form)
    return redirect(read)




