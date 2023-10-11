from django.db import models

SOURCE_CHOICES = (
    ('YouTube', 'YouTube'),
    ('Google', 'Google'),
    ('NewsLetter', 'NewsLetter'),
)


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)

    paid = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_pic = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)


