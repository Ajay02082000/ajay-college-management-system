from django.shortcuts import render
from django.http import HttpResponse
from .models import prntdetails
from .models import fee

# Create your views here.
def parent(request):
    prntinfo = prntdetails.objects.all()
    prnt={
        'parent':prntinfo
    }
    return render(request,'parent.html',context=prnt)

def feez(request):
    if request.method == 'POST':
         studentname =request.POST['studentname']
         studentid =request.POST['studentid']
         feeamount =request.POST['feeamount']

         Register=fee(studentname=studentname,studentid=studentid,feeamount=feeamount)
         Register.save()
    return render(request,'fee.html', {})
