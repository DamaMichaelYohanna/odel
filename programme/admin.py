from django.contrib import admin

from programme.models import Programme, Faculty, Department, Session, Semester, Course

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Programme)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Course)
