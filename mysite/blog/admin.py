from django.contrib import admin
from .models import School, Student, Certificate, Faculty, Department, Grade

# Register your models here.
admin.site.register(School)
admin.site.register(Student)
admin.site.register(Certificate)
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Grade)