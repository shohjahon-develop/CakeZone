from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.forms import ContactForms
from blog.models import One, Master, Say, Ved, Cust, Chef


# Create your views here.
def index(request):
    ones = One.objects.all()
    masters = Master.objects.all()
    says = Say.objects.all()
    custs = Cust.objects.all()
    context = {
        "ones":ones,
        "masters":masters,
        "says":says,
        "custs":custs
    }
    return render(request,"index.html",context=context)

def onesdetailview(request,id):
    try:
        ones=One.objects.get(id=id)
        context = {
            "ones":ones
        }
    except ones.DoesNotExist:
        raise Http404("No ones found")
    return render(request,"ones_Detail.html",context=context)


def custsdetailview(request, custs):
    cust = get_object_or_404(Cust,slug=custs)
    context = {
        "cust":cust
    }
    return render(request,"custs_Detail.html",context=context)

def saysdetailview(request,id):
    try:
        says=Say.objects.get(id=id)
        context = {
            "says":says
        }
    except says.DoesNotExist:
        raise Http404("No ones found")
    return render(request,"says_Detail.html",context=context)
def mastersdetailview(request,id):
    try:
        masters=Master.objects.get(id=id)
        context = {
            "masters":masters
        }
    except masters.DoesNotExist:
        raise Http404("No masters found")
    return render(request,"masters_Detail.html",context=context)


def contact(request):
    contact = ContactForms(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2> SO'ROV MUVOFIQYIATLI BAJARILDI  !!! <h2/> ")
    context = {
        "contact":contact
    }
    return render(request,"contact.html",context=context)

def about(request):
    return render(request,"about.html",context={})

def service(request):
    return render(request,"service.html",context={})

def team(request):
    chefs = Chef.objects.all()
    context = {
        "chefs":chefs
    }
    return render(request,"team.html",context=context)

def chefsdetailview(request, chefs):
    chef = get_object_or_404(Chef,slug=chefs)
    context = {
        "chef":chef
    }
    return render(request,"chefs_Detail.html",context=context)
def testimonial(request):
    return render(request,"testimonial.html",context={})

def menu(request):
    veds = Ved.objects.all()
    context = {
        "veds":veds
    }
    return render(request,"menu.html",context=context)

def vedsdetailview(request, veds):
    ved = get_object_or_404(Ved,slug=veds)
    context = {
        "ved":ved
    }
    return render(request,"veds_Detail.html",context=context)









































































