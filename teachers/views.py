import random 
from django.views import generic
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from students.models import Teacher
from .forms import TeacherModelForm
from .mixins import OrganisorAndLoginRequiredMixin


class TeacherListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'teachers/teacher_list.html'


    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Teacher.objects.filter(organisation=organisation)



class TeacherCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'teachers/teacher_create.html'
    form_class = TeacherModelForm

    def get_success_url(self):
        return reverse('teachers:teacher-list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f'{random.randint(0, 1000000)}')
        user.save()
        Teacher.objects.create(
            user=user,
            organisation=self.request.user.userprofile  
        )
        send_mail(
            subject = 'You are invited to be an agent!',
            message = 'You were added as an agent on SchoolCRM. Please come login to start working.',
            from_email = "admin@test.com",
            recipient_list = [user.email]  
        )
        return super(TeacherCreateView, self).form_valid(form)




class TeacherDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = 'teachers/teacher_detail.html'
    context_object_name = 'teacher'
    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Teacher.objects.filter(organisation=organisation)

class TeacherUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'teachers/teacher_update.html'
    form_class = TeacherModelForm
    queryset = Teacher.objects.all()

    def get_success_url(self):
        return reverse('teachers:teacher-list')

    def get_queryset(self):
        return Teacher.objects.all()


class TeacherDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = 'teachers/teacher_delete.html'
    context_object_name = 'teacher'


    def get_success_url(self):
        return reverse('teachers:teacher-list')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Teacher.objects.filter(organisation=organisation)

