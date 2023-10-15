from django.http import HttpResponse
from django.shortcuts import render

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