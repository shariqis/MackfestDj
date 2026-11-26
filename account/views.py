from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth import get_user_model

from .forms import RegistratiomForm, StudentFileForm, StudentForm
from .models import StudentFile, UserProfile , Student
 

from django.core.mail import send_mail 

# Create your views here.

def home(request):
    return render(request,'account/home.html')


def register(request):
    if request.method=="POST":
        form= RegistratiomForm(request.POST)

        if form.is_valid():

            user=form.save()

            UserProfile.objects.create(user=user, role=form.cleaned_data['role'])

            messages.success(request,'Registration successfull please login ')

            return redirect('login')
        else:
            return redirect('regis')
        
    else:

        form=RegistratiomForm()

        return render(request,'account/register.html',{'form':form})



def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('usernme')
        passw=request.POST.get('passwo')


        user= authenticate(request,
                           username=uname,password=passw)

        if user is not None:
            login(request,user)
            if not user.is_active:
                messages.error(request,'Your Account is inactive... or waiting for approvel')

            
                return redirect('login')    
            if user.is_superuser:
                return redirect('/admin/')

            try:
                profile=user.userprofile

            except UserProfile.DoesNotExist :
                logout(request)  
                messages.error(request,
                               'user role is not configured . contact admin')
                return redirect('login')


            if profile.role=='student':

                return redirect('student_dashboard')
            elif profile.role=="teacher":
                return redirect('teacher_dashboard')


            logout(request)
            messages.error(request,'invalid user role')

        else:
            messages.error(request,'invalid usernamr or password')

      
    else:

        return render(request,'account/login.html')    


def studhome(request):
    
    return render(request,'account/studhom.html')    




@login_required(login_url='login')
def upload_file(request):

    if request.method == 'POST':
        form= StudentFileForm(request.POST,request.FILES)

        if form.is_valid():
            student_file=form.save(commit=False)
            student_file.student=request.user
            student_file.save()

            messages.success(request,'File uploaded successfully')
            return redirect('display_file')
    else:
        form= StudentFileForm()

        return render(request,'account/upload_file.html',{'form':form})


@login_required(login_url='login')
def display_file(request):
    # student_files= request.user.student_files.all()

    student_files= StudentFile.objects.all()
    # student_files= StudentFile.objects.filter(student=request.user)

    return render(request,'account/display_file.html',{'student_files':student_files})        





def send_email_view(request):
    # if request.method == 'POST':
        # subject = request.POST.get('subject')
        # message = request.POST.get('message')
        # recipient_email = request.POST.get('recipient_email')
        subject = "Test Email"
        message = "This is a test email sent from Django."
        recipient_email = "shariqis2016@gmail.com"

        if recipient_email and subject and message:
            try:
                send_mail(subject,
                          message,
                          None,
                          [recipient_email],
                            fail_silently=False
                          )

                messages.success(request, 'Email sent successfully.')
            except Exception as e:
                messages.error(request, f'Error sending email: {str(e)}')


        return HttpResponse('Email sent successfully.')
    

    # ===============================================================


from django.urls import reverse_lazy
from django.views.generic import CreateView , ListView , DetailView,UpdateView,DeleteView


class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'course']
    template_name = 'account/student_form.html'
    success_url = reverse_lazy('student_list')  # Redirect to the student list view after successful creation



class StudentsListView(ListView):
    model = Student
    template_name = 'account/student_list.html'
    context_object_name = 'students'  # Name of the context variable to use in the template



class StudentDetailView(DetailView):
    model = Student
    template_name = 'account/student_detail.html'
    context_object_name = 'student'  # Name of the context variable to use in the template

class StudentUpdateView(UpdateView):
    model = Student
    form_class= StudentForm  # Assuming you have a form class for updating students
    template_name = 'account/student_form.html'
    success_url = reverse_lazy('student_list')  # Redirect to the student list view after successful update


class StudentDeleteView(DeleteView):
    model=Student
    template_name="account/student_confirm_delete.html"
    success_url = reverse_lazy('student_list')  # Redirect to the student list view after successful update
   


#    ===============================================

def set_cookie(request):
    response=render(
        request,'cookie.html'
    )

    response.set_cookie(
        'myname',
        "shari",
        max_age=3600
    )
    return response


def get_cookie(request):
    name=request.COOKIES.get(
        'myname',
        'Guest'
    )

    return render(
        request,
        'cookie.html',
        {'name':name}
    )



def del_cook(request):
    response=HttpResponse(
        'cookies deleted'
    )

    response.delete_cookie('myname')
    return response



# ==============================================

def set_sess(request):
    request.session['my_name']="ANU"
    request.session['course']='python'

    return render(request,'sess.html')



def get_sess(request):
    name= request.session.get('my_name','guest')
    course= request.session.get('course','noooo')

    return render(request,'sess.html',{'Name':name,"Course":course})


def del_sess(request):
    request.session.flush()

    return render(request,'sess.html',{'msg':'session cleared successfully'})