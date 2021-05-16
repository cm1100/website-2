from django.contrib import admin
from .models import Tutorial,Tutorial_Category,Tutorial_Series
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutorial_Category)
admin.site.register(Tutorial_Series)
admin.site.register(Tutorial,TutorialAdmin)
