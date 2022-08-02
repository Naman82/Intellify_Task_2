from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth,User
from django.contrib import messages
from app.models import Student,Teacher



User = get_user_model()

# Create your views here.

def index(request):
    return render(request,'index.html')

def student(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        rollno = request.POST['rollno']
        standard = request.POST['standard']
        section = request.POST['section']
        stream = request.POST['stream']
        password=request.POST['password']
        password2=request.POST['password2']
        profile=request.FILES['photoInput']
        # state=request.POST['state']
        # city=request.POST['city']
        # pincode=request.POST['pincode']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('student')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('student')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_student=True)
                user.save()
                current_user = User.objects.get(username=username)
                student_user = Student(user=current_user,profile_img=profile,registration_id=username,standard=standard,class_section=section,stream=stream,roll_number=rollno)
                student_user.save()
                return redirect('student_login')

        else:
            messages.info(request,'Password does not match , Try again')
            return redirect('student')
    else:
        return render(request,'student_register.html')

def teacher(request):
    if request.method =='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        subjects=request.POST['subjects']
        classes=request.POST['classes']
        mobile=request.POST['mobile']
        password=request.POST['password']
        password2=request.POST['password2']
        profile=request.FILES['photoInput']

        print(subjects)
        print(classes)

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('teacher')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('teacher')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_teacher=True)
                user.save();
                current_user = User.objects.get(username=username)
                teacher_user = Teacher(user=current_user,profile_img=profile,teacher_id=username,subject=subjects,class_taught=classes,contact_number=mobile)
                teacher_user.save()
                return redirect('teacher_login')

        else:
            messages.info(request,'Password does not match , Try again')
            return redirect('teacher')
    else:
        return render(request,'teacher_register.html')

def student_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_student==True:
                auth.login(request,user)
                return redirect('student_home')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('student_login')

        else:
            messages.info(request,'Credentials Invalid')
            return redirect('student_login')
    else:
        return render(request,'student_login.html')

def teacher_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_teacher==True:
                auth.login(request,user)
                return redirect('teacher_home')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('teacher_login')

        else:
            messages.info(request,'Credentials Invalid')
            return redirect('teacher_login')
    else:
        return render(request,'teacher_login.html')

def student_home(request):
    users=User.objects.get(username=request.user)
    students=Student.objects.get(user=request.user)
    return render(request,'student_home.html',{'users':users, 'students':students})

def teacher_home(request):
    users=User.objects.get(username=request.user)
    teachers=Teacher.objects.get(user=request.user)
    return render(request,'teacher_home.html',{'users':users, 'teachers':teachers})
    

def logout(request):
    auth.logout(request)
    return redirect('/')