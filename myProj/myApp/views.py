from django.shortcuts import render
from django.http import HttpResponse
from .models import Car
from .forms import NewCar


# Create your views here.
def car(request):
    if(request.method == "POST"):
        myCar = NewCar(request.POST)

        if (myCar.is_valid()):
            Car.objects.create(make=request.POST["make"], model=request.POST["model"], year=request.POST["year"], mpg=request.POST["mpg"])
        else:
            print(myCar.errors)
            allEntries = Car.objects.all()
            context ={
                'EveryError': myCar.errors,
                'allEntries': allEntries,
                'mycar': NewCar()
            }
    allEntries = Car.objects.all()
    myCar = NewCar()
    context ={
        'methodType': request.method,
        'allEntries': allEntries,
        'myCar': myCar,
    }
    return render(request, 'myApp/infoCars.html', context)
