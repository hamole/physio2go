from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Program, ProgramEntry, Exercise, ExerciseEntry

# Create your views here.
@login_required
def program_list(request):
	programs = Program.objects.filter(user=request.user)
	return render(request,'exercises/program_list.html',{'programs':programs})

@login_required
def program_detail(request, program_slug):
	program = Program.objects.get(slug=program_slug)
	exercises = Exercise.objects.filter(program=program)
	return render(request,'exercises/program_detail.html',{'program':program,'exercises': exercises})

@login_required
def program_entry(request, program_slug, program_entry_id):
	program = Program.objects.get(slug=program_slug)
	program_entry = ProgramEntry.objects.get(id=program_entry_id)
	exercises = Exercise.objects.filter(program=program)
	return render(request,'exercises/program_entry.html',{'program_entry':program_entry})

@login_required
def exercise_detail(request, program_slug, exercise_slug):
	program = Program.objects.get(slug=program_slug)
	exercise = Exercise.objects.get(program=program, slug=exercise_slug)
	return render(request,'exercises/exercise_detail.html',{'program':program,'exercise': exercise})

@login_required
def exercise_entry(request, program_slug, program_entry_id, exercise_slug, excerise_entry_id):
	program = Program.objects.get(slug=program_slug)
	exercises = Exercise.objects.filter(program=program)
	return render(request,'exercises/program_detail.html',{'program':program,'exercise': exercises})