from django.urls import path

from .views import student_create, student_list, student_detail, student_update, student_delete

app_name = 'students'

urlpatterns = [
    path('', student_list, name='student-list'),
    path('<int:pk>/', student_detail, name='student-detail'),
    path('<int:pk>/update/', student_update, name='student-update'),
    path('<int:pk>/delete/', student_delete, name='student-delete'),
    path('create/', student_create, name='student-create')

]
