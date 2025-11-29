from django.shortcuts import render

def home(request):
    team = [
        {"name": "Jhon Paul Flores", "role": "Developer"},
        {"name": "Drexelica Bern Reyes", "role": "Designer"},
    ]
    return render(request, "bernappl/home.html", {"team": team})
