from django.urls import path

from .views import student_create, student_list, student_detail

app_name = 'students'

urlpatterns = [
    path('', student_list),
    path('<int:pk>/', student_detail),
    path('create/', student_create)
]
