from django.urls import path

from .views import (
    course_list_view,
    course_detail_view,
    lesson_detail_view
)

app_name = 'courses'

urlpatterns = [

    path('', course_list_view),
    path('<str:slug>', course_detail_view),
    path('<str:course_slug>/<str:module_slug>/<str:lesson_slug>', lesson_detail_view),

]
