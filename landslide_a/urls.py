from django.conf.urls import url
import landslide_a.views
from landslide import  settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', landslide_a.views.first, name="first"),
    url(r'^article/(?P<article_title>\D+)/$',landslide_a.views.article,name = "article")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)