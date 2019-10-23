from django.shortcuts import render
from .models import Lesson, Module, Course
from django.shortcuts import render, get_object_or_404


# Create your views here.
def course_list_view(request):
    queryset = Course.objects.all()

    context = {
        "object_list": queryset
    }
    template_name = 'courses/home.html'
    return render(request, template_name, context)


def course_detail_view(request, slug):
    course_obj = get_object_or_404(Course, slug=slug)

    modules = Module.objects.filter(course=course_obj)

    template_name = 'courses/detail.html'

    context = {
        "course_obj": course_obj,
        "modules": modules,
    }

    return render(request, template_name, context)


def lesson_detail_view(request, course_slug, module_slug, lesson_slug):
    obj = get_object_or_404(Lesson, slug=lesson_slug)

    module_obj = obj.module
    course_obj = module_obj.course

    module_list = Module.objects.filter(course=course_obj)

    template_name = 'courses/lesson.html'

    context = {
        "object": obj,
        "course_obj": course_obj,
        'module_obj': module_obj,
        "module_list": module_list,
    }

    return render(request, template_name, context)
