from django.contrib import admin
from .models import Post,Category,Tag


# class TagInline(admin.StackedInline):
#     model = Tag
#     extra = 3
# class CategoryInline(admin.TabularInline):
#     model = Category
#     extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time']

    # fieldsets = [
    #     (None, {'fields': ['title']}),
    #     # ('Date information', {'fields': ['created_time', 'modified_time']})
    #     ('Content information',{'fields':['content','excerpt']})
    # ]

    # inlines = [CategoryInline]
    # inlines=[TagInline]

# Register your models here.
admin.site.register(Post,PostAdmin)

admin.site.register(Tag)
admin.site.register(Category)