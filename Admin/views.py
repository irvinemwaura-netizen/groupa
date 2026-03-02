from gc import get_objects
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from Admin.models import Student
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})
def add_record(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get('name')
        course = request.POST.get('course')
        age = request.POST.get('age')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        Student.objects.create(
            image=image,
            name=name,
            course=course,
            age=age,
        email=email,
        date_of_birth=date_of_birth)
        return redirect('index')
    return render(request, 'add_record.html')
def update_record(request, id):
    students = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        students.image = request.FILES.get('image')
        students.name = request.POST.get('name')
        students.course = request.POST.get('course')
        students.age = request.POST.get('age')
        students.email = request.POST.get('email')
        students.date_of_birth = request.POST.get('date_of_birth')
        if request.FILES.get('image'):
            students.image = request.FILES.get('image')
        students.save()
        return redirect('index')
    return render(request, 'update_record.html', {'students': students})


def delete_record(request, pk):
    students = get_object_or_404(Student, id=pk)

    if request.method == "POST":
        students.delete()
        return redirect('index')  # change to your list page name
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('sign_up')
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'sign_up.html')
def log_in(request):

    return render(request, 'log_in.html')