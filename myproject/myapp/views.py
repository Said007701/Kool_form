from django.shortcuts import render,redirect
from .models import Kool
from .forms import KoolForm

def Create(request):
    if request.method == "POST":
        form = KoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = KoolForm()

    return render(request, 'myapp/create.html',{'form':form})

def list_book(request):
    books = Kool.objects.all()
    return render(request,'myapp/list_book.html', {'books':books})

def update_book(request, list_id):
    book = Kool.objects.get(id=list_id)
    if request.method == 'POST':
        form = KoolForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = KoolForm(instance=book)
    
    return render(request, 'myapp/update.html', {'form': form, 'book': book})

def delete_book(request, list_id):
    book = Kool.objects.get(id=list_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_book')
    
    return render(request, 'myapp/delete.html', {'book': book})



def index(request):
    return render(request,'myapp/index.html')

def login(request):
    if request.method == "POST":
        form = KoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = KoolForm()
    return render(request,'myapp/login.html',{'form':form})

def register(request):
    if request.method == "POST":
        form = KoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_book')
    else:
        form = KoolForm()
    return render(request,'myapp/register.html',{'form':form})

def password(request):
    return render(request,'myapp/password-reset.html')

def pages(request):
    return render(request,'myapp/404.html')

def contact(request):
    return render(request,'myapp/contact.html')

def list(request):
    books = Kool.objects.all()
    return render(request,'myapp/list_book.html', {'books':books})
