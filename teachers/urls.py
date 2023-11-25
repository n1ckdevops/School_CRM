from django.urls import path
from .views import TeacherListView, TeacherCreateView,TeacherDetailView


app_name = 'teachers'

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher-list'),
    path('create/', TeacherCreateView.as_view(), name='teacher-create'),
    path('<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    # path('<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    # path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
]