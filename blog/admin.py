from django.contrib import admin
from .models import Post, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'image', 'short_description')
    prepopulated_fields = {'slug': ('name',)}

    def short_description(self, obj):
        return obj.description[:20] + '...' if obj.description and len(obj.description) > 20 else obj.description
    short_description.short_description = 'Description' 
    
    
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'content')

admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
 