from django.contrib import admin
from landslide_a.models import Articles,About,main_block,outputs,event,person
# Register your models here.
@admin.register(Articles)
class article_fil(admin.ModelAdmin):
    list_display = ['title','date']
    list_filter = ['date']

@admin.register(About)
class about_fill(admin.ModelAdmin):
    list_display = ["title"]
admin.site.register(main_block)

@admin.register(outputs)
class output_fill(admin.ModelAdmin):
    list_display = ['title']

@admin.register(event)
class events(admin.ModelAdmin):
    list_display = ["title"]

@admin.register(person)
class person(admin.ModelAdmin):
    list_display = ["first_name","last_name"]