from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from CompApp.models import complain
from CompApp import models
from CompApp.forms import NewComplainForm,SearchForm

# Create your views here.
def about(request):
    s=render(request,'CompApp/about.html')
    return s
def category(request):
    s=render(request,'CompApp/category.html')
    return s
def contact(request):
    s=render(request,'CompApp/contact.html')
    return s
def complain_info_view(request):
    c=complain.objects.all()
    data={'c':c}
    res=render(request,'CompApp/complain.html',data)
    return res
def editComplain(request):
    b=models.complain.objects.get(complain_id=request.GET['complainid'])
    fields={'complain_id':b.complain_id,'Name':b.Name,'Category':b.Category,'Phone_no':b.Phone_no,'Address':b.Address}
    form=NewComplainForm(initial=fields)
    res=render(request,'CompApp/edit_complain.html',{'form':form,'b':b})
    return res

def edit(request):
    if request.method=='POST':
        form=NewComplainForm(request.POST)
        b=models.complain()
        b.complain_id=request.POST['complainid']
        b.Name=form.data['Name']
        b.Category=form.data['Category']
        b.Phone_no=form.data['Phone_no']
        b.Address=form.data['Address']
        b.save()
    return HttpResponseRedirect('CompApp/view-complain')

def deleteComplain(request):
    complainid=request.GET['complainid']
    b=models.complain.objects.filter(complain_id=complainid)
    b.delete()
    return HttpResponseRedirect('CompApp/view-complain')
def newComplain(request):
    f=NewComplainForm()
    return render(request,'CompApp/new_complain.html',{'f':f})

def viewComplain(request):
    b=models.complain.objects.all()
    # username=request.session['username']
    return render(request,'CompApp/view_complain.html',{'b':b})

def searchComplain(request):
    form=SearchForm()
    return render(request,'CompApp/search_complain.html',{'form':form})

def search(request):
    form=SearchForm(request.POST)
    b=models.complain.objects.filter(Category=form.data['Category'])
    return render(request,'CompApp/search_complain.html',{'form':form,'b':b})

def add(request):
    if request.method=='POST':
        f=NewComplainForm(request.POST)
        b=models.complain()
        b.Name=f.data['Name']
        b.Category=f.data['Category']
        b.Phone_no=f.data['Phone_no']
        b.Address=f.data['Address']
        b.save()
    s="record stored <br> <a href='/CompApp/view-complain'>view all complains</a>"
    return HttpResponse(s)
