
from django.shortcuts import render
from django.views import generic
from .models import course, teacher, faculty

def index(request):

	num_course=course.objects.all().count()
	num_teacher=teacher.objects.count()
	num_faculty=faculty.objects.all().count()
	return render(
		request, 
		'index.html',
		context={'num_course':num_course,'num_teacher':num_teacher, 'num_faculty':num_faculty},
		)
class courseListView(generic.ListView):
    model = course
class courseDetailView(generic.DetailView):
    model = course
class teacherListView(generic.ListView):
    model = teacher
class teacherDetailView(generic.DetailView):
    model = teacher