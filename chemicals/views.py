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

@login_required
def edit_chemical(request, chem_id):
    chem = get_object_or_404(Chemicals, pk=chem_id)
    if request.method == "POST":
        form = ChemicalForm(request.POST, instance=chem)
        if form.is_valid():
            form.save()
            return redirect('display')
    else:
        form = ChemicalForm(instance=chem)
        return render(request, "chemicals/addchemical.html", {'form': form, 'edit':True})
    
@login_required()
def stock(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display')
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
                return redirect('utendisplay')
        else:
            form = addUtensilForm()

        return render(request,'chemicals/utenadd.html',{'form':form})

def edit_utensil(request, id):
    utensil = Utensils.objects.get(id=id)
    if request.method == "POST":
        form = addUtensilForm(request.POST, instance=utensil)
        if form.is_valid():
            form.save()
            return redirect('utendisplay')
    else:
        form = addUtensilForm(instance=utensil)
        return render(request, 'chemicals/utenadd.html', {'form': form,'edit':True})
def utendisplay(request):
        uten=Utensils.objects.all()
        return render(request,'chemicals/utendisplay.html',{'uten':uten})

def addFine(request):
    if request.method == "POST":
        form = FineForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            # Retrieve the selected item (utensil)
            item = cleaned_data.get('Item')

            # Create a new Fine object
            fine_obj = Fine(
                admn_no=cleaned_data.get('admn_no'),
                Date=cleaned_data.get('Date'),
                Name=cleaned_data.get('Name'),
                Department=cleaned_data.get('Department'),
                status=cleaned_data.get('status'),
                Year=cleaned_data.get('Year'),
                Item=item,  # Assign the selected item (ForeignKey)
            )

            # Retrieve the price from the selected item and assign
            fine_obj.price = item.price

            # Save the Fine object
            fine_obj.save()

            return redirect('finedisplay')
    else:
        form = FineForm()

    return render(request, 'chemicals/fineadd.html', {'form': form})

def editFine(request, id):
    fine = Fine.objects.get(id=id)
    if request.method == "POST":
        form = FineForm(request.POST, instance=fine)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = FineForm(instance=fine)
        return render(request, 'chemicals/fineadd.html', {'form': form,'edit':True})
    
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
    utensil = get_object_or_404(Utensils, id=id)
    if request.method == 'POST':
        utensil.delete()
        return redirect('utendisplay')

@login_required
def delete_fine(request, pk):
    fine = get_object_or_404(Fine, pk=pk)
    fine.delete()
    return redirect('finedisplay')

@login_required
def add_stock(request):
    if request.method == 'POST':
        form = UtensilStockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = UtensilStockForm()
    return render(request, 'chemicals/addstock.html', {'form': form})

@login_required
def stock_list(request):
    stocks = UtensilsStock.objects.all()
    return render(request, 'chemicals/stocklist.html', {'stocks': stocks})