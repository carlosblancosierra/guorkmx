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


class Category(models.Model):
    title = models.CharField(max_length=120)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


def upload_location(instance, filename):
    return "blog_posts/%s/%s" % (instance.id, filename)


class BlogPostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(BlogPostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

    def get_3_random_by_category(self, category, *args, **kwargs):
        all_post_of_category = self.active().filter(category__title=category)
        count = len(all_post_of_category)
        random_post_list = []

        if count > 1:

            i = count - 1

            if count > 3:
                i = 3

            while len(random_post_list) < i:

                random_index = randint(0, count - 1)
                random_post = all_post_of_category[random_index]

                if random_post not in random_post_list:
                    random_post_list.append(random_post)

        return random_post_list

    def get_3_random_by_instance_category(self, current, *args, **kwargs):
        all_post_of_category = self.active().filter(category__title=current.category)
        count = len(all_post_of_category)
        random_post_list = []

        if count > 1:

            i = count - 1

            if count > 3:
                i = 3

            while len(random_post_list) < i:

                random_index = randint(0, count - 1)
                random_post = all_post_of_category[random_index]

                if (current != random_post) and (random_post not in random_post_list):
                    random_post_list.append(random_post)

        return random_post_list

    def get_3_random(self, *args, **kwargs):
        all_post_of_category = self.active()
        count = len(all_post_of_category)
        random_post_list = []

        if count > 1:

            i = count

            if count > 3:
                i = 3

            while len(random_post_list) < i:

                random_index = randint(0, count - 1)
                random_post = all_post_of_category[random_index]

                if random_post not in random_post_list:
                    random_post_list.append(random_post)

        return random_post_list


# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, max_length=255)
    content = RichTextUploadingField(null=True, blank=True)
    image = ProcessedImageField(upload_to=upload_location, null=True, blank=True,
                                processors=[ResizeToFill(1200, 628)],
                                format='JPEG',
                                options={'quality': 90})
    image_small = ImageSpecField(source='image',
                                 processors=[ResizeToFill(800, 419)],
                                 format='JPEG',
                                 options={'quality': 90})

    meta_description = models.CharField(max_length=120, blank=True)
    seo_title = models.CharField(max_length=100, blank=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    reading_time = models.IntegerField(default=10)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    objects = BlogPostManager()

    class Meta:
        ordering = ["-publish", "-updated"]

    def get_absolute_url(self):
        return f"/blog/{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"


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
