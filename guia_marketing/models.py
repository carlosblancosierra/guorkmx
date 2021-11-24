from django.conf import settings
from django.db import models

from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone
from django.urls import reverse
from random import randint

User = settings.AUTH_USER_MODEL


def upload_location(instance, filename):
    return "capitulo/%s/%s" % (instance.id, filename)


class CapituloManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(CapituloManager, self).filter(draft=False)


# Create your models here.
class Capitulo(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    order = models.IntegerField(null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    meta_description = models.CharField(max_length=120, blank=True)
    seo_title = models.CharField(max_length=100, blank=True)
    draft = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    objects = CapituloManager()

    def get_absolute_url(self):
        return f"/guia_marketing_digital/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    qs = Capitulo.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance=slug, new_slug=new_slug)

    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Capitulo)
