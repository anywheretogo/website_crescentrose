from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    #fields = []
    list_display = ['name', "last_update",'finished','author', 'publisher']
    list_filter = ['finished', 'publisher']
    search_fields = ['name', 'author', 'num']

admin.site.register(Article, ArticleAdmin)
