from django.conf import settings
from django.db import models

from imagekit.models import ImageSpecField
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from ckeditor_uploader.fields import RichTextUploadingField

from django.utils.text import slugify
from django.db.models.signals import pre_save

User = settings.AUTH_USER_MODEL


def upload_location(instance, filename):
    return "blog_posts/%s/%s" % (instance.id, filename)


# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    content = RichTextUploadingField(null=True, blank=True)
    image = ProcessedImageField(upload_to=upload_location, null=True, blank=True,
                                processors=[ResizeToFill(730, 487)],
                                format='JPEG',
                                options={'quality': 90})
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(384, 256)],
                                 format='JPEG',
                                 options={'quality': 90})

    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-publish", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    qs = BlogPost.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance=slug, new_slug=new_slug)

    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=BlogPost)
