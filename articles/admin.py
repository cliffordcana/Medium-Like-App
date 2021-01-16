from django.contrib import admin
from .models import Articles

admin.site.register(Articles)

'''
class ChoiceInline(admin.TabularInline):
    model = Comment
    extra = 5

class ArticlesAdmin(admin.ModelAdmin):
    :fieldsets = [
        (None,                  {'fields': ['title']}),
        ('Date Information',    {'fields': ['date_posted'], 'classes':
        ['collapse']}),
    ]
    
    inlines = [ChoiceInline]
    list_display = (
        'was_posted_recently',
        'title',
        'date_posted',
        'date_updated',
        'image',
        'article_choices',
        'author'
    )
    list_filter = ['date_posted']
    search_fields = ['title', 'content']'''