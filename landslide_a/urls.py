from django.conf.urls import url
import landslide_a.views
from landslide import  settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', landslide_a.views.first, name="first"),
    url(r'^article/(?P<article_title>\D+)/$',landslide_a.views.article,name = "article"),
    url(r'about_project/$',landslide_a.views.about,name="about"),
    url(r'^news/$',landslide_a.views.news,name="news"),
    url(r'^output/(?P<output_title>\D+)/$',landslide_a.views.output,name="output"),
    url(r'^contact/$',landslide_a.views.contact,name="contact")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)