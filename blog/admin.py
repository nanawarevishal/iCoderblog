from django.contrib import admin

from .models import blog,Category,blogComment,ContactUS,Profile

# Register your models here.



admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(blogComment)
admin.site.register(ContactUS)
@admin.register(blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)
        



