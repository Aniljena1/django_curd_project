from django.shortcuts import render,redirect
from .models import Company
from .forms import CompanyForm
from django.contrib import messages
# Create your views here.


def view(request):
    org=Company.objects.all()
    return render(request,'home.html',{'org':org})

def Emp_form(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'From created successfully')
            return redirect('/')
    else:
        form = CompanyForm()

    return render(request, 'create.html', {'form':form})


def updaet(request,id):
    if request.method == 'POST':
        org=Company.objects.get(pk = id)
        form = CompanyForm(request.POST,instance=org)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        org = Company.objects.get(pk=id)
        form=CompanyForm(instance=org)
    return render(request,'update.html',{'form':form})





def delete_view(request,id):
    if request.method == 'POST':
        org=Company.objects.get(pk = id)
        org.delete()
        return redirect('/')




