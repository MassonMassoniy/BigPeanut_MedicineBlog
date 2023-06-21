from django.contrib import admin
from .models import Post, Comment, Ip

# Register your models here.

class CommentsInLine(admin.TabularInline):
    model = Comment
    fk_name = 'post'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text', 'date_comment')
    list_filter = ('user', 'date_comment')
    fieldsets = (
        ('Основная информация',{'fields':('user', 'post', 'date_comment')}),
        ('Содержание',{'fields':('text',)})
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'post_type', 'description', 'date_post')
    list_filter = ('user', 'date_post')
    fieldsets = (
        ('Основная информация',{'fields':('user', 'title', 'post_type', 'date_post')}),
        ('Содержание',{'fields':('description', 'text')})
    )
    inlines = [CommentsInLine]

#admin.site.register(Post)
#admin.site.register(Comment)
admin.site.register(Ip)