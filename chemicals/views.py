from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
# Create your views here.

@login_required()
def home(request):
    return render(request, 'chemicals/home.html') 

@login_required()
def add_chemical(request):
    if request.method == "POST":
        form = ChemicalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = ChemicalForm()
    return render(request,"chemicals/addchemical.html",{'form':form})

@login_required()
def stock(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PurchaseForm()

    return render(request,'chemicals/purchase.html',{'form':form})

@login_required()
def purchased_details(request,chem_id):
    balance={
    'balance':Chemicals.objects.get(id=chem_id)
    }
    chem={
    'chem':PurchasedDetails.objects.filter(chem_name=chem_id)
    }
   
    return render(request,'chemicals/pur_details.html',{**balance,**chem,'chemi':chem_id})


@login_required()
def display_chemicals(request):
    chemicals = Chemicals.objects.all()
    return render(request, 'chemicals/display.html', {'chemicals': chemicals})

def addUtensil(request):
        if request.method == "POST":
            form = addUtensilForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = addUtensilForm()

        return render(request,'chemicals/utenadd.html',{'form':form})

def utendisplay(request):
        uten=Utensils.objects.all()
        return render(request,'chemicals/utendisplay.html',{'uten':uten})

def addFine(request):
    if request.method == "POST":
        form = addFineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = addFineForm()
    return render(request,'chemicals/fineadd.html',{'form':form})

def finedisplay(request):
    fine=Fine.objects.all()
    return render(request,'chemicals/finedisplay.html',{'fine':fine})



def fine_recived(request, fine_id):
    fine = get_object_or_404(Fine, id=fine_id)
    fine.status = "Received"
    fine.save()
    fine=Fine.objects.all()
    return render(request,'chemicals/finedisplay.html',{'fine':fine})

def balance_update(request,pk):
    if request.method=="POST":
        balance=request.POST.get('balance')
        obj=Chemicals.objects.get(id=pk)
        obj.Balance=balance
        obj.save()
        return redirect(f"view/{pk}")

@login_required
def delete_chemical(request, pk):
    chemical = get_object_or_404(Chemicals, pk=pk)
    chemical.delete()
    return redirect('display')

@login_required
def delete_utensil(request, id):
    utensil = get_object_or_404(Utensils, id=utensil_id)
    if request.method == 'POST':
        utensil.delete()
        return redirect('list_utensils')
    return render(request, 'confirm_delete.html', {'utensil': utensil})

@login_required
def delete_fine(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    fine.delete()
    return redirect('finedisplay')