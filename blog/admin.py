from django.contrib import admin

from blog.models import Post, Theme

from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# admin.site.register(Post)
admin.site.register(Theme)


class TextAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = TextAdminForm