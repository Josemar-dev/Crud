from django.shortcuts import render, redirect
from .models import menbro

def index(req):
    mem= menbro.objects.all().order_by('-id')
    userCount = menbro.objects.all().count()
    data = {
        'mem':mem,
        'userCount':userCount
    }
    return render(req, "index.html",data)

def add(req):
    return render(req, 'add.html')

def addrec(req):
    x = req.POST['primeiro']
    y = req.POST['segundo']
    z = req.POST['terceiro']
    mem=menbro(primeironome=x,segundonome=y,terceironome=z)
    mem.save()
    return redirect("/")

def delete(req, id):
    mem = menbro.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(req, id):
    mem = menbro.objects.get(id=id)
    return render(req, 'update.html', {'mem':mem})

def uprec(req):
    x = req.POST['primeiro']
    y = req.POST['segundo']
    z = req.POST['terceiro']
    mem = menbro.objects.get(id=req.POST['id'])
    mem.primeironome=x
    mem.segundonome=y
    mem.terceironome=z
    mem.save()
    return redirect("/")
