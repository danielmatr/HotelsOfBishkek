from django.contrib import admin

# Register your models here.
from main.models import *

admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Saved)
class PostImageInline(admin.TabularInline):
    model = Image
    max_num = 5
    min_num = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline, ]


