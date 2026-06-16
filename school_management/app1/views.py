from django.shortcuts import render

# Create your views here.
import logging
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

logger = logging.getLogger('school_logger')

def student_list(request):
    students = Student.objects.all()
    logger.info("Student list viewed")
    return render(request, 'students/student_list.html', {'students': students})


def add_student(request):
    form = StudentForm(request.POST or None)

    if form.is_valid():
        form.save()
        logger.info("Student added")
        return redirect('student_list')

    return render(request, 'students/add_student.html', {'form': form})
# import logging
# from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm

# logger = logging.getLogger('school_logger')

def teacher_list(request):
    teachers = Teacher.objects.all()
    logger.info("Teacher list viewed")
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})


def add_teacher(request):
    form = TeacherForm(request.POST or None)

    if form.is_valid():
        form.save()
        logger.info("Teacher added")
        return redirect('teacher_list')

    return render(request, 'teachers/add_teacher.html', {'form': form})
    