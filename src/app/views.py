from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth,User
from django.contrib import messages
from app.models import Student,Teacher

# To use existing "User" model with customization
User = get_user_model()

# Create your views here.

def index(request):
    return render(request,'index.html')

def student(request):
    # for post request storing form submission values from frontend in variables
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

        # passwords check
        if password == password2 :
            # existing email check
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('student')
            # existing username check
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('student')
            else:
                # user created
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_student=True)
                # user saved in database
                user.save()
                # user instance for Student model
                current_user = User.objects.get(username=username)
                # student created
                student_user = Student(user=current_user,profile_img=profile,registration_id=username,standard=standard,class_section=section,stream=stream,roll_number=rollno)
                #student saved in database
                student_user.save()
                return redirect('student_login')

        else:
            # if passwords check fail
            messages.info(request,'Password does not match , Try again')
            return redirect('student')
    else:
        return render(request,'student_register.html')

def teacher(request):
    # for post request storing form submission values from frontend in variables
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

        # passwords check
        if password == password2 :
            # existing email check
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('teacher')
            # existing username check
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
                return redirect('teacher')
            else:
                # user created
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,is_teacher=True)
                # user saved in database
                user.save();
                # getting user instance for Student model
                current_user = User.objects.get(username=username)
                # teacher created
                teacher_user = Teacher(user=current_user,profile_img=profile,teacher_id=username,subject=subjects,class_taught=classes,contact_number=mobile)
                # teacher saved in database
                teacher_user.save()
                return redirect('teacher_login')

        else:
            # if passwords check fail
            messages.info(request,'Password does not match , Try again')
            return redirect('teacher')
    else:
        return render(request,'teacher_register.html')

def student_login(request):
    # for post request storing form submission values from frontend in variables
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        # Authenticate user 
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            #check for student user
            if user.is_student==True:
                #login
                auth.login(request,user)
                return redirect('student_home')
            else:
                # if user is not student
                messages.info(request,'Credentials Invalid')
                return redirect('student_login')

        else:
            # if authenticate user fail
            messages.info(request,'Credentials Invalid')
            return redirect('student_login')
    else:
        return render(request,'student_login.html')

def teacher_login(request):
    # for post request storing form submission values from frontend in variables
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        

        # Authenticate user 
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            #check for teacher user
            if user.is_teacher==True:
                #login
                auth.login(request,user)
                return redirect('teacher_home')
            else:
                # if user is not teacher
                messages.info(request,'Credentials Invalid')
                return redirect('teacher_login')

        else:
            # if authenticate user fail
            messages.info(request,'Credentials Invalid')
            return redirect('teacher_login')
    else:
        return render(request,'teacher_login.html')

def student_home(request):

    # return users detail who is currently logged in 
    users=User.objects.get(username=request.user)

    #return student detail who is currently logged in
    students=Student.objects.get(user=request.user)
    return render(request,'student_home.html',{'users':users, 'students':students})

def teacher_home(request):

    # return users detail who is currently logged in 
    users=User.objects.get(username=request.user)

    #return teacher detail who is currently logged in
    teachers=Teacher.objects.get(user=request.user)
    return render(request,'teacher_home.html',{'users':users, 'teachers':teachers})
    

def logout(request):
    #logout
    auth.logout(request)
    return redirect('/')