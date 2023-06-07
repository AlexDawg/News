from django.contrib import admin
from .models import Post, PostCategory, Category, CategorySubscribe, Author


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)
    nullfy_quantity.short_description = 'Обнулить товары'


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_in', 'text')
    list_filter = ('title', 'time_in', 'categories')
    search_fields = ('title', 'time_in', 'categories')
    actions = [nullfy_quantity]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
# Register your models here.
