from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Insurance
from .forms import InsuranceForm
@login_required
def insurance_list(request):
    insurances = Insurance.objects.filter(user=request.user)
    return render(request, 'insurance/insurance_list.html', {'insurances': insurances})
@login_required
def insurance_create(request):
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('insurance_list')
    else:
        form = InsuranceForm()
    return render(request, 'insurance/insurance_form.html', {'form': form})
@login_required
def insurance_update(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk, user=request.user)
    form = InsuranceForm(request.POST or None, instance=insurance)
    if form.is_valid():
        form.save()
        return redirect('insurance_list')
    return render(request, 'insurance/insurance_form.html', {'form': form})
@login_required
def insurance_delete(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk, user=request.user)
    if request.method == 'POST':
        insurance.delete()
        return redirect('insurance_list')
    return render(request, 'insurance/insurance_confirm_delete.html', {'insurance': insurance})

@login_required
def insurance_pay(request, pk):
    insurance = get_object_or_404(Insurance, pk=pk, user=request.user)
    if request.method == 'POST':
        try:
            amount = float(request.POST.get('amount'))
            insurance.amount_paid = amount
            insurance.is_paid = True
            insurance.save()
            return redirect('insurance_list')
        except (ValueError, TypeError):
            pass
    return render(request, 'insurance/insurance_pay.html', {'insurance': insurance})