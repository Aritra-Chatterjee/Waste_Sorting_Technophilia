"""wastesorting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from ourapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="main"),
    path('citizenportal/',views.citizenportalhome),
    path('login/',views.login),
    path('request/',views.req),
    path('feedback/',views.feedback),
    path('thankyou/',views.thankyou),
    path('about/',views.about),
    path('collectorlogin/',views.collectorlogin),
    path('collectorportal/',views.collectorportal),
    path('requests/',views.reqs),
    path('citizendata/',views.citizendata),
    path('organic/',views.organic),
    path('recyclable/',views.recyclable),
    path('electronic/',views.electronic),
    path('feedbackdata/',views.feedbackdata),

]
