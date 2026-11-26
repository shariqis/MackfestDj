from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentModelForm,EmpModelForm
from .models import Student,Enmployee,Department
# Create your views here.
def home(request,myname):
    name= myname
    return HttpResponse(f"Hello  {name}")

def about(request,m):
    num=[12,88,33,97,6]
    mydate={'1':22,'4':44,'6':22}
    return render(request,'about.html',{'name':m,           
            "address":"elkm","mtime":16,
            "mark":num,'data':mydate})    


def addStud(request):
    if request.method=="POST":
        frm= StudentModelForm(request.POST)
        if frm.is_valid():
            print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
            frm.save()
        print("............................")
        # return  HttpResponse(f"SAVED SUCCESSFULLY")
        return redirect("viewStud")

    else:
        frm= StudentModelForm()

        print("///////////////////")
        
        return render(request,'addStd.html',{'form':frm})


def viewStud(request):
    data= Student.objects.all()
    return render(request,"viewstd.html",{"da":data})


def delStud(request,sid):
    # s= Student.objects.get(id=sid)

    s= get_object_or_404(Student,id=sid)

    s.delete()

    return redirect("viewStud")


def edit_stud(request,sid):    

    stud= get_object_or_404(Student,id=sid)


    if request.method=="POST":
        form= StudentModelForm(request.POST,instance=stud)

        if form.is_valid():
            form.save()
            return redirect("viewStud")


    else:

        form=StudentModelForm(instance=stud)

        return render(request,'editstud.html',{'form':form,"student":stud})


def addEmp(request):

    print(list(Department.objects.all()))

    form=EmpModelForm()
    print(form)
    return render(request,"addEMP.html",{'frm':form})