"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import home
#from admins.views import admins
from student.views import studentl
from faculty.views import faculty
from parent.views import parent
from contact.views import contact
from home.views import aboutus
from home.views import courses
from home.views import stdprofile
from home.views import prntprofile
from home.views import fcltprofile
from faculty.views import leave
from home.views import fcltattendance
from home.views import fclttimetables
from home.views import admins
from home.views import stdhome
from home.views import stdattendance
from home.views import stdtimetables
from home.views import stdmarks,student
from home.views import stdexams
from home.views import stdlist
# from home.views import fee
from parent.views import feez
from home.views import prnthome
from home.views import feestatus
from home.views import paymentsuccessful
from home.views import gallery
from home.views import noticeboard






urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
   # path('admins/',admins),
    
    
    path('',home),
    path('contact/',contact),
    path('aboutus/',aboutus),
    path('courses/',courses),
    
    
    path('faculty/',faculty),
    path('fcltprofile/',fcltprofile),
    path('fcltleave/',leave),
    path('fcltattendance/',fcltattendance),
    path('fclttimetables/',fclttimetables),
    path('admins/',admins),


    path('student/',studentl),
    path('stdhome/',stdhome),
    path('stdprofile/',stdprofile),
    path('stdattendance/',stdattendance),
    path('stdtimetables/',stdtimetables),
    path('stdexams/',stdexams),
    path('students/',student),
    path('stdmarks/',stdmarks),
    path('stdlist/',stdlist),
    path('noticeboard/',noticeboard),


    # path('fee/',fee),
    path('fee/',feez),
    path('feestatus/',feestatus),
    path('paymentsuccessful/',paymentsuccessful),
 
   
    path('parent/',parent),
    path('prnthome/',prnthome),
    path('prntprofile/',prntprofile),
    path('gallery/',gallery),
    
    
    

    
    
]
