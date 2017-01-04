from django.contrib import admin
from .models import Category, Page


class PageAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_display = ('title', 'category', 'url')
    list_select_related = ('category',)
    list_filter = ('category',)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
