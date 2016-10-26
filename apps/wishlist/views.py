from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import item, User
from django.http import HttpResponseRedirect

# Create your views here.


def index(request):

    if not session(request):
        return redirect('loginreg:index')
    context={
    'myitems':item.objects.filter(users=User.objects.get(id=request.session['user']['id'])),
    "allitems":item.objects.exclude(users=User.objects.get(id=request.session['user']['id'])).exclude(join=User.objects.filter(id=request.session['user']['id'])),
    'addedproducts':item.objects.filter(join=User.objects.filter(id=request.session['user']['id']))
    }
    return render(request, "wishlist/index.html", context)


def add(request):
    if not session(request):
        return redirect('loginreg:index')
    return render(request, "wishlist/additem.html")

def create(request):
    if not session(request):
        return redirect('loginreg:index')
    validate = item.objects.itemvalidate(request.POST)
    print(validate)
    if validate:
        for error in validate:
            messages.error(request, error)
            return redirect('wishlist:additem')
    else:
        item.objects.createproduct(request.POST, request.session['user']['id'])
        return redirect('wishlist:index')


def delete(request, id):
    item.objects.get(id = id).delete()
    return redirect('wishlist:index')

def remove(request, id):
    item.objects.delete(id,request.session['user']['id'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def show(request, id):
    if not session(request):
        return redirect('loginreg:index')
    context = {
    "item": item.objects.filter(id=id)
    }
    return render(request, "wishlist/show.html", context)

def join(request, id):
    item.objects.join(id,request.session['user']['id'])
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def session(request):
    if 'user' not in request.session:
        return False
    else:
        return True
