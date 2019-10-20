from django.conf.urls import url
import landslide_a.views
from landslide import  settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', landslide_a.views.first, name="first"),
    url(r'^article/(?P<article_title>.*)/$',landslide_a.views.article,name = "article"),
    url(r'^about_project/$',landslide_a.views.about,name="about"),
    url(r'^news/$',landslide_a.views.news,name="news"),
    url(r'^output/(?P<output_title>.*)/$',landslide_a.views.output,name="output"),
    url(r'^contact/$',landslide_a.views.contact,name="contact"),
    url(r'^case_studies/$',landslide_a.views.case_studies,name="case_studies"),
    url(r'^partners/(?P<partners_title>.*)/$',landslide_a.views.partners_detail, name="partners_detail"),
    url(r'^team/$',landslide_a.views.team, name="our team"),
    url(r'^event/$',landslide_a.views.events, name="event"),
    url(r'^event/(?P<event_title>.*)/$',landslide_a.views.specialevent, name="detail"),
    url(r'^sitemap/$',landslide_a.views.sitemap,name="sitemap"),
    url(r'^search/$', landslide_a.views.search.as_view(), name="search"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)