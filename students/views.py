from django.shortcuts import render, redirect

from .forms import StudentModelForm
from .models import Student


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
    form = StudentModelForm()
    if request.method == 'POST':
        print("Receiving a post method")
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students')
    context = {
        'form': form,
    }
    return render(request, 'students/student_create.html', context)


def student_update(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentModelForm(instance=student)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/students')
    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'students/student_update.html', context)


def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('/students')

# def student_update(request, pk):
#     student = Student.objects.get(id=pk)
#     form = StudentForm()
#     if request.method == 'POST':
#         print("Receiving a post method")
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             student.first_name = first_name
#             student.last_name = last_name
#             student.age = age
#             student.save()
#             print('Student has been created!')
#             return redirect('/students')
#     context = {
#         'student': student,
#         'form': form,
#
#     }
#     return render(request, 'students/student_update.html', context)

# def student_create(request):
#     form = StudentModelForm()
#     if request.method == 'POST':
#         print("Receiving a post method")
#         form = StudentModelForm(request.POST)
#         if form.is_valid():
#             print('the form is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             teacher = Teacher.objects.first()
#             Student.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 teacher=teacher
#             )
#             print('Student has been created!')
#             return redirect('/students')
#     context = {
#         'form': form,
#     }
#     return render(request, 'students/student_create.html', context)
