from django import forms

from .models import BlogPost

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(
        widget=CKEditorUploadingWidget()
    )


class BlogPostModelForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = ['title',
                  'slug',
                  'publish',
                  'image'
                  ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['publish'].widget.attrs.update({'class': 'datepicker'})

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')

        qs = BlogPost.objects.filter(title__iexact=title)

        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Este ya titulo existe, pruebe con otro")
        return title

    def clean_slug(self, *args, **kwargs):
        instance = self.instance
        slug = self.cleaned_data.get('slug')

        qs = BlogPost.objects.filter(slug__iexact=slug)

        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Este ya slug existe, pruebe con otro")
        return slug
