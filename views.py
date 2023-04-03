from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
d={
    'january':'first month of the year',
    'february':'shortest month of the year',
    'march':' month of exam',
    'april':'month of fools',
    'may':'month of vacation',
    'june':'month of admissions',
    'july':'longest month of year',
    'august':'no non-veg month',
    'september':'ganapathi bappa moreya',
    'october':'month of dasara',
    'november':'month of lights',
    'december': None
}
def index(request):
    l=list(d)
    return render(request,'index.html',{'data':l})
    
def month_with_num(request,month):
    l=list(d)
    data=l[month-1]
    red_path=reverse('disp',args=[data])
    return HttpResponseRedirect(red_path)

def months(request,month):
    try:
        return render(request,'month.html',{'message':d[month],'m':month})
    except:
        return HttpResponseNotFound('invalid month name')
