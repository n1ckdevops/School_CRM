from django.urls import path
from .views import *


app_name = 'students'

urlpatterns = [
    path('', student_list),
    path('<pk>/', student_detail),


]
