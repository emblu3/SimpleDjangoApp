from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.CharField(max_length=400)

    def __str__(self):
        return self.type

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    graduation_year = models.IntegerField()

    def __str__(self):
        return self.full_name


