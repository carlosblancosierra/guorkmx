from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm


def blog_post_list_view(request):
    queryset = BlogPost.objects.all()

    paginator = Paginator(queryset, 6)

    page_request_var = "pagina"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    object_1 = queryset[:1]

    object_list_2 = queryset[0:2]

    object_list_3 = queryset[2:]

    template_name = 'blog/list.html'
    context = {
        "object_list": queryset,
        "object_1": object_1,
        "object_list_2": object_list_2,
        "object_list_3": object_list_3,
        "page_request_var": page_request_var,

    }

    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'blog/update.html'
    context = {
        "object": obj,
        "form": form
    }

    return render(request, template_name, context)


@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostForm()

    template_name = 'blog/create.html'
    context = {
        "form": form
    }

    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {
        "object": obj
    }

    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'

    if request.method == "POST":
        obj.delete()

    context = {
        "object": obj
    }

    return render(request, template_name, context)
