from django.shortcuts import render
from django.http import HttpResponse
from student.models import stddetails



# Create your views here.
def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'aboutus.html')

def courses(request):
    return render(request,'courses.html')

def noticeboard(request):
    return render(request,'noticeboard.html')

def stdprofile(request):
    return render(request,'stdprofile.html')

def student(request):
    return render(request,'student.html')

def prntprofile(request):
    return render(request,'prntprofile.html')

def fcltprofile(request):
    return render(request,'fcltprofile.html')

def admins(request):
    return render(request,'admins.html')

def stdhome(request):
    return render(request,'stdhome.html')

def stdattendance(request):
    return render(request,'stdattendance.html')

def stdtimetables(request):
    return render(request,'stdtimetables.html')

def stdmarks(request):
    return render(request,'stdmarks.html')

def stdlist(request):

    stdinfo = stddetails.objects.all()
    std={
        'data':stdinfo
    }
    return render(request,'stdlist.html',context=std)



# def fee(request):
#    return render(request,'fee.html')






def prnthome(request):
    return render(request,'prnthome.html')

def feestatus(request):
    return render(request,'feestatus.html')

# def fcltleave(request):
#     return render(request,'fcltleave.html')

def fcltattendance(request):
    return render(request,'fcltattendance.html')

def fclttimetables(request):
    return render(request,'fclttimetables.html')

def stdexams(request):
    return render(request,'stdexams.html')

def paymentsuccessful(request):
    return render(request,'paymentsuccessful.html')

def gallery(request):
    return render(request,'gallery.html')





