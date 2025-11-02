from django.contrib import admin
from django.shortcuts import get_object_or_404

from .models import Category, Article, ArticleImage
from .forms import ArticleImageForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    fieldsets = (
        ('', {
            'fields': ('category','slug'),
        }),
    )
    prepopulated_fields = {'slug':('category',)}

admin.site.register(Category, CategoryAdmin)


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 0
    form = ArticleImageForm
    fieldsets = (
        ('', {
            'fields': ('title', 'image',),
        }),
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'slug', 'main_page', 'category')
    inlines = [ArticleImageInline]
    multiupload_form = True
    multiupload_list = False
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('', {
            'fields': ('pub_date', 'title', 'description',
                       'main_page', 'category'),
        }),
        (u'Додатково', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('slug',),
        }),
    )

    def delete_file(self, pk, request):
        obj = get_object_or_404(ArticleImage, pk=pk)
        return obj.delete()


admin.site.register(Article, ArticleAdmin)
