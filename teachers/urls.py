from django.urls import path
from .views import (
    TeacherListView, TeacherCreateView,
    TeacherDetailView, TeacherUpdateView, TeacherDeleteView
)


app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher-list'),
    path('create/', TeacherCreateView.as_view(), name='teacher-create'),
    path('<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update'),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
]