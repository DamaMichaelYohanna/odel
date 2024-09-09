from django.db import models


class Faculty(models.Model):
    """database model for faculty"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Department(models.Model):
    """database model for the various departments"""
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"


class Programme(models.Model):
    """Database model for programme found under a particular
    department since one department can be offering more than a single
    programme."""
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name}"


class Session(models.Model):
    """Database model for keeping track of session"""
    session = models.CharField(max_length=10, null=True, blank=True)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.session}"


class Semester(models.Model):
    """Database model for keeping track of session"""
    name = models.CharField(choices=(("First", "First"), ("Second", "Second")), max_length=6, null=True, blank=True)
    session = models.ForeignKey(Session, on_delete=models.DO_NOTHING)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"


class Course(models.Model):
    """Database model for keeping track of session"""
    name = models.CharField( max_length=10, null=True, blank=True)
    code = models.CharField(max_length=50)
    credit = models.IntegerField()
    programme = models.ForeignKey(Programme, on_delete=models.DO_NOTHING)
    level = models.CharField(max_length=50)
    semester = models.CharField(choices=(("First", "First"), ("Second", "Second")),max_length=6)

    def __str__(self):
        return f"{self.name}"
