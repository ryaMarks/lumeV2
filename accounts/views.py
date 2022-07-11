from multiprocessing import context
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

# Create your views here.

def login_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
    
        user = authenticate(request, username=username, password=password)
    
        if user is None:
            context = {"error":"Usuario ou senha invalidos",}
            return render(request, "accounts/login.html",context)
        else:
            login(request,user)
            return redirect("/clientes/")

    return render(request, "accounts/login.html",{})

