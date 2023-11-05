from django.contrib import admin
from .models import Category, PhotoPost

class CategoryAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class PhotoPostAdmin(admin.ModelAdmin):
        # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')
    
admin.site.register(Category, CategoryAdmin)

admin.site.register(PhotoPost, PhotoPostAdmin)
# Register your models here.
