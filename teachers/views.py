from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from students.models import Teacher
from .forms import TeacherModelForm


class TeacherListView(LoginRequiredMixin, generic.ListView):
    template_name = 'teachers/teacher_list.html'


    def get_queryset(self):
        return Teacher.objects.all()



class TeacherCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'teachers/teacher_create.html'
    form_class = TeacherModelForm

    def get_success_url(self):
        return reverse('teachers:teacher-list')

    def form_valid(self, form):
        teacher = form.save(commit=False)
        teacher.organisation =  self.request.user.userprofile
        teacher.save()
        return super(TeacherCreateView, self).form_valid(form)


class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'
    def get_queryset(self):
        return Teacher.objects.all()

class TeacherUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'teachers/teacher_update.html'
    form_class = TeacherModelForm
    queryset = Teacher.objects.all()

    def get_success_url(self):
        return reverse('teachers:teacher-list')

    def get_queryset(self):
        return Teacher.objects.all()


class TeacherDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'teachers/teacher_delete.html'
    context_object_name = 'teacher'


    def get_success_url(self):
        return reverse('teachers:teacher-list')

    def get_queryset(self):
        return Teacher.objects.all()

