from django.contrib import admin
from .models import User
from blog.models import Post, Comment

# Register your models here.


class PostInLine(admin.TabularInline):
    model = Post
    fk_name = 'user'


class CommentsInLine(admin.TabularInline):
    model = Comment
    fk_name = 'user'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'account_name', 'role',
                    'date_joined', 'is_staff', 'is_active')
    list_filter = ('role', 'date_joined', 'is_staff', 'is_active')
    fieldsets = (
        ('Основная информация',
         {'fields': ('account_name', 'role')}),
        ('Дополнительная информация',
         {'fields': ('date_joined', 'is_staff', 'is_active')})
    )
    inlines = [PostInLine, CommentsInLine]
