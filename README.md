# Ex.04 Design a Website for Server Side Processing
## Date:12.12.2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html

<html>
<head>
    <title>Mileage calculator</title>

    <style>
        body {
            background-color: steelblue;
            font-size: 25px;
            text-align: center;
        }

        .box {
            width: 45%;
            margin: 70px auto;
            padding: 20px;
            background-color: purple;
            border: 4px dashed lime;
            border-radius: 15px;
            color: orange;
        }

        input[type="number"] {
            width: 155px;
            padding: 5px;
            margin-left: 12px;
        }

        input[type="submit"] {
            margin-top: 17px;
            padding: 9px 23px;
            background: ghostwhite;
            border: 3px solid greenyellow;
            cursor: pointer;
        }
    </style>
</head>

<body>

    <div class="box">
        <h1>Mileage calculator</h1>
        <h3>Saigokul.k (25004959)</h3>

        <form method="POST">
            {% csrf_token %}

            <p>
                distance (km):
                <input type="number">
            </p>

            <p>
                fuel consumed(litres):
                <input type="number">
            </p>

            <input type="submit" value="Calculate">

            <p>
            <br>
            mileage:
            <input type="text"value="{{mileage}}">
            km/l
            </p>
        </form>

    </div>

</body>
</html>

views.py

from django.shortcuts import render
def mileage(request):
    d=int(request.POST.get('distance',0))
    f=int(request.POST.get('fuel consumed',1))
    mileage=d/f if request.method == 'POST' else 0
    print("distance=",d)
    print("fuel consumed=",f)
    print("mileage=",mileage)
    return render(request,'mathapp/math.html',{'d':d,'f':f,'mileage':mileage})



urls.py

from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.mileage, name='mileage'),
]

```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (34).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (33).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
