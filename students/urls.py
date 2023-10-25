from django.urls import path

from .views import student_create, student_list, student_detail, student_update

app_name = 'students'

urlpatterns = [
    path('', student_list),
    path('<int:pk>/', student_detail),
    path('<int:pk>/update', student_update),
    path('create/', student_create)

]
