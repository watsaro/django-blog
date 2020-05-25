from django.contrib import admin
from blogging.models import Post, Category
# Register your models here.
# and a new admin registration


class CategoryAdmin(admin.ModelAdmin):
    # Fill me
    exclude = ('posts',)

class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    # Fill me
    inlines = [
        CategoryInline,
    ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)