from django.shortcuts import render
def mileage(request):
    d=int(request.POST.get('distance',0))
    f=int(request.POST.get('fuel consumed',1))
    mileage=d/f if request.method == 'POST' else 0
    print("distance=",d)
    print("fuel consumed=",f)
    print("mileage=",mileage)
    return render(request,'mathapp/math.html',{'d':d,'f':f,'mileage':mileage})

# Create your views here.
