from doctor.models import Doctor,User,Patient
from django.views.generic import CreateView,DetailView,ListView
from doctor.models import Doctor,Patient,User,Blog,Category
from doctor.forms import DoctorSignupForm,PatientSignupForm,Blog_Form
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    return render(request, 'register.html')

def homepage(request):
    return render(request,'index.html')

class doctor_register(CreateView):
    model = User
    form_class = DoctorSignupForm
    template_name = 'doctor_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('docdetails')

class patient_register(CreateView):
    model = User
    form_class = PatientSignupForm
    template_name = 'patient_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patdetails')


def doctor_login_request(request):
     if request.method=="POST":
         form = AuthenticationForm(data=request.POST)
         if form.is_valid():
             username=form.cleaned_data.get("username")
             password=form.cleaned_data.get("password")
             user=authenticate(username=username,password=password)
             if user is not None:
                 login(request,user)
                 return render(request,"ask.html")
             else:
                messages.error(request,'Invalid username or password')
         else:
            messages.error(request,'Invalid username or password')
     return render(request,'login.html',context={'form':AuthenticationForm()})


def patient_login_request(request):
     if request.method=="POST":
         form = AuthenticationForm(data=request.POST)
         if form.is_valid():
             username=form.cleaned_data.get("username")
             password=form.cleaned_data.get("password")
             user=authenticate(username=username,password=password)
             if user is not None:
                 login(request,user)
                 return redirect('showblogs')
             else:
                messages.error(request,'Invalid username or password')
         else:
            messages.error(request,'Invalid username or password')
     return render(request,'login.html',context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect(homepage)

class doctor_details(DetailView):
    model=Doctor
    template_name='docdetails.html'

class patient_details(DetailView):
    model=Patient
    template_name='patdetails.html'

def addblog(request):
    form=Blog_Form()
    if request.method=='POST':
        form=Blog_Form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('showblogs'))
    else:
        form=Blog_Form()
    context={
        'form':form
    }
    return render(request,'addblog.html',context)

class showblogs(ListView):
    model=Blog
    template_name='showblogs.html'

class blogDetail(DetailView):
    model=Blog
    template_name='blogdetail.html'
