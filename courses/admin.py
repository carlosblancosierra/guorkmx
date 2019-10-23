from django.contrib import admin

from .models import Lesson, Module, Course, Document

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Module)
admin.site.register(Course)
admin.site.register(Document)
