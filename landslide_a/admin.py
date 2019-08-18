from django.contrib import admin
from landslide_a.models import Articles,About,main_block
# Register your models here.

class article_fil(admin.ModelAdmin):
    list_display = ["title",'date']
    list_filter = ['date']
    class Meta:
        model = Articles


admin.site.register(Articles)
admin.site.register(About)
admin.site.register(main_block)