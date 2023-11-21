from django.contrib import admin

from .models import User, Student, Teacher, UserProfile

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Student)
