from django.shortcuts import render
from django.http import HttpResponse
from .models import fcltdetails
from .models import fcltleave

# Create your views here.
def faculty(request):
    fcltinfo = fcltdetails.objects.all()
    fclt={
        'faculty':fcltinfo
    }
    return render(request,'faculty.html',context=fclt)

def leave(request):
    if request.method == 'POST':
         teachername =request.POST['teachername']
         leavetype =request.POST['leavetype']
         leavestartdate =request.POST['leavestartdate']
         leaveenddate =request.POST['leaveenddate']

         Leaves=fcltleave(teachername=teachername,leavetype=leavetype,leavestartdate=leavestartdate,leaveenddate=leaveenddate)
         Leaves.save()
    return render(request,'fcltleave.html', {})