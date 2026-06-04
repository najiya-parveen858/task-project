from django.shortcuts import render,redirect
from django.views import View
from student.forms import *
from django.views.generic import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
class signupview(CreateView):
    template_name="signup.html"
    form_class=SignupForm
    success_url=reverse_lazy('signin')

class signinview(FormView):
    template_name="signin.html"
    form_class=signinForm
    def post(self,request):
        form_data=signinForm(data=request.POST)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get('username')
            pswd=form_data.cleaned_data.get('password')
            usr=authenticate(request,username=uname,password=pswd)
            if usr:
                return redirect('shome')
            else:
                return redirect('signin')
            
# class studenthomeview(TemplateView):
#     template_name='studenthome.html'

class addstudentview(CreateView):
    template_name='addstudent.html'
    form_class=StudentForm
    def post(self,request,**kwargs):
        form_data=StudentForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('shome')
        return render(request,"addstudent.html",{"form":form_data})
    

class studenthomeview(View):
    def get(self, request):
        data = student.objects.all()
        return render(request, "studenthome.html", {"data": data})







class deletestudview(View):
    def get(self,request, **kwargs):
        sid=kwargs.get('id')
        student.objects.get(id=sid).delete()
        return redirect('shome')

class editstudentview(View):
    def get(self,request, **kwargs):
         sid=kwargs.get('id')
         stud=student.objects.get(id=sid)
         form=StudentForm(instance=stud)
         return render(request,"editstudent.html",{"form":form})
    def post(self,request,*args, **kwargs):
         sid=kwargs.get('id')
         stud=student.objects.get(id=sid)
         form_data=StudentForm(data=request.POST,instance=stud,files=request.FILES)
         if form_data.is_valid():
            form_data.save()
            messages.info(request,"student data updated")
            return redirect('shome')
         return render(request,"editstudent.html",{"form":form_data})






































