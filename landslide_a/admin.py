from django.contrib import admin
from landslide_a.models import Articles,About,main_block,person,foto_news,geological_background,geological_objects,main_object,form_user1
# Register your models here.
@admin.register(Articles)
class article_fil(admin.ModelAdmin):
    list_display = ['title','date']
    list_filter = ['date']

@admin.register(About)
class about_fill(admin.ModelAdmin):
    list_display = ["title"]
admin.site.register(main_block)

@admin.register(person)
class person(admin.ModelAdmin):
    list_display = ["first_name","last_name"]

@admin.register(geological_background)
class person(admin.ModelAdmin):
    list_display = ["name","type"]

@admin.register(geological_objects)
class geolgical_objects(admin.ModelAdmin):
    list_display = ["name","x_coord","y_coord"]
admin.site.register(main_object)


@admin.register(foto_news)
class person(admin.ModelAdmin):
    list_display = ["foto_header"]

admin.site.register(form_user1)