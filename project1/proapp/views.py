from django.shortcuts import render
from django.http import HttpResponse
from proapp.models import Person
# Create your views here.c
def home(request):
    return HttpResponse("hi")
def second(request):
    return HttpResponse("how r u")
def home_page(request):
    q = 2
    name = 'sreya'
    return render(request, 'home.html', {'super': q, 'n': name})
def add(request):
    if request.method == 'POST':
        a = request.POST['num1']
        b = request.POST['num2']
        q = int(a)+int(b)
        return render(request, 'add.html', {'z': q})

    return render(request, 'add.html')

def add_person(request):
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['age']
        c = request.POST['place']
        d = request.POST['email']
        e = request.FILES['photo']
        q = Person(name=a,age=b,place=c,email=d,photo=e)
        q.save()
        return HttpResponse("sucessfully added")
    return render(request, 'add_person.html')

def views_person(request):
    q = Person.objects.all()
    return render(request, 'views_person.html', {'p': q})

def Update_person(request,id1):
    q = Person.objects.get(id=id1)
    if request.method == 'POST':
        q.name = request.POST['name']
        q.age= request.POST['age']
        q.place = request.POST['place']
        q.email= request.POST['email']
        q.save()
        return HttpResponse("updated successfully")
    return render(request, 'views_person.html', {'z': q})

def dlt_person(request,id2):
    q=Person.objects.get(id=id2)
    if q:
        q.delete()
        return HttpResponse('removed successfully')
    else:
        return HttpResponse('does not exit')
    return render(request,'views_person.html')

def search(request):
    if request.method == 'POST':
        a=request.POST['name']
        q=Person.objects.filter(name=a)

    return render(request,'views_person.html',{'x': q})