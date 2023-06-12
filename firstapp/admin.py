#from itertools import count
from django.contrib import admin
from .models import teacher, faculty, course

# Register your models here.

#admin.site.register(course)
#admin.site.register(teacher)
#admin.site.register(faculty)

class teacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
admin.site.register(teacher, teacherAdmin)
admin.site.register(faculty)

class courseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'display_faculty')
admin.site.register(course, courseAdmin)