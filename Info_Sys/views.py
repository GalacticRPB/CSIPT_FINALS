from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ResidentForm
from django.http import HttpResponseRedirect
from .models import Resident

# Create your views here.

def residentrecords(request):
    resident_List = Resident.objects.all() 
    return render(request,'info/residentrecords.html', {'resident_List': resident_List})

def residentform(request):
    submitted = False
    if request.method == "POST":
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = ResidentForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'info/residentform.html', {'form': form, 'submitted':submitted})

def editresident(request, resID):
    person = Resident.objects.get(pk=resID)
    form = ResidentForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('residentrecords')
    return render(request, 'info/residentrecordsedit.html', {'person': person, 'form': form})

def deleteresident(request, resID):
    person = Resident.objects.get(pk=resID)
    person.delete()
    return redirect('residentrecords')