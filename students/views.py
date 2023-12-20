from typing import Any
from django.core.mail import send_mail
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from teachers.mixins import OrganisorAndLoginRequiredMixin
from .forms import StudentModelForm, CustomUserCreationForm
from .models import Student

# CRUD+L - CREATE, RETRIEVE, UPDATE AND DELETE + LIST

class SignupView(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('login')


class LandingPageView(generic.TemplateView):
    template_name = 'landing.html'


def landing_page(request):
    return render(request, 'landing.html')


class StudentListView(LoginRequiredMixin, generic.ListView):
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        # check the request user
        user = self.request.user
        # checking if the user is organiser
        if user.is_organisor:
            # if he is - then they will have a user profile
            queryset = Student.objects.filter(organisation=user.userprofile)
        else:
            queryset = Student.objects.filter(organisation=user.teacher.organisation)
            # filter for the agent that is logged in
            queryset = queryset.filter(teacher__user=user)
        return queryset

def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/student_list.html', context)


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

    def get_queryset(self):
        # check the request user
        user = self.request.user
        # checking if the user is organiser
        if user.is_organisor:
            # if he is - then they will have a user profile
            queryset = Student.objects.filter(organisation=user.userprofile)
        else:
            queryset = Student.objects.filter(organisation=user.teacher.organisation)
            # filter for the agent that is logged in
            queryset = queryset.filter(teacher__user=user)
        return queryset


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {
        'student': student,

    }
    return render(request, 'students/student_detail.html', context)


class StudentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'students/student_create.html'
    form_class = StudentModelForm

    def get_success_url(self):
        return reverse('students:student-list')

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject='A student has been created',
            message='Go to the site to see the new student',
            from_email='test@test.com',
            recipient_list=['test2@test.com']
        )
        return super(StudentCreateView, self).form_valid(form)


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


class StudentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'students/student_update.html'
    form_class = StudentModelForm

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Student.objects.filter(organisation=user.userprofile)


    def get_success_url(self):
        return reverse('students:student-list')


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


class StudentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'students/student_delete.html'


    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        return Student.objects.filter(organisation=user.userprofile)


    def get_success_url(self):
        return reverse('students:student-list')


def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('/students')
