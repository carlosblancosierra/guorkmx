from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.db.models.signals import pre_save

from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from .validators import validate_file_size


def course_upload_location(instance, filename):
    return "courses/%s/%s" % (instance.id, filename)


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    image = ProcessedImageField(upload_to=course_upload_location, null=True, blank=True,
                                processors=[ResizeToFill(730, 487)],
                                format='JPEG',
                                options={'quality': 90})
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(384, 256)],
                                 format='JPEG',
                                 options={'quality': 90})
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    overview = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/workshops/{self.slug}"

    def modules(self):
        modules = Module.objects.filter(courses=self)
        return modules


class Module(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def lessons(self):
        lessons = Lesson.objects.filter(module=self)
        return lessons


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return f"/workshops/{self.module.course.slug}/{self.module.slug}/{self.slug}"

    def __str__(self):
        return self.title


def create_slug_course(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    qs = Course.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug_course(instance=slug, new_slug=new_slug)

    return slug


def pre_save_course_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_course(instance)


pre_save.connect(pre_save_course_receiver, sender=Course)


def file_upload_location(instance, filename):
    return "courses/document/%s/%s" % (instance.course.slug, filename)


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=file_upload_location, validators=[validate_file_size])
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
