from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student, Teacher


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/student_list.html', context)


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {
        'student': student,

    }
    return render(request, 'students/student_detail.html', context)


def student_create(request):
    if request.method == 'POST':
        print("Receiving a post method")
        form = StudentForm(request.POST)
        if form.is_valid():
            print('the form is valid')
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            teacher = Teacher.objects.first()
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                teacher=teacher
            )
            print('Student has been created!')
            return redirect('/students')
    context = {
        'form': form
    }
    return render(request, 'students/student_create.html', context)
