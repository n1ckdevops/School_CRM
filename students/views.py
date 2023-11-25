from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
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
    queryset = Student.objects.all()
    context_object_name = 'students'


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/student_list.html', context)


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'students/student_detail.html'
    queryset = Student.objects.all()
    context_object_name = 'student'


def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    context = {
        'student': student,

    }
    return render(request, 'students/student_detail.html', context)


class StudentCreateView(LoginRequiredMixin, generic.CreateView):
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


class StudentUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'students/student_update.html'
    form_class = StudentModelForm
    queryset = Student.objects.all()

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


class StudentDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'students/student_delete.html'
    queryset = Student.objects.all()

    def get_success_url(self):
        return reverse('students:student-list')


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
