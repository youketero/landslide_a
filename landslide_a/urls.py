from django.conf.urls import url
import landslide_a.views
from landslide import  settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', landslide_a.views.first, name="first"),
    url(r'^article/(?P<article_title>.*)/$',landslide_a.views.article,name = "article"),
    url(r'^about_project/$',landslide_a.views.about,name="about"),
    url(r'^news/$',landslide_a.views.news,name="news"),
    url(r'^contact/$',landslide_a.views.contact,name="contact"),
    url(r'^case_studies/$',landslide_a.views.case_studies,name="case_studies"),
    url(r'^partners/(?P<partners_title>.*)/$',landslide_a.views.partners_detail, name="partners_detail"),
    url(r'^team/$',landslide_a.views.team, name="our team"),
    url(r'^team/(?P<team_id>.*)$',landslide_a.views.team_detailed, name="each_team"),
    url(r'^sitemap/$',landslide_a.views.sitemap,name="sitemap"),
    url(r'^search/$', landslide_a.views.search.as_view(), name="search"),
    url(r'сase_study',landslide_a.views.case_study,name="case_study"),
    url(r'geological_objects/(?P<type>.*)/$',landslide_a.views.geological_object, name="geological_object"),
    url(r'geological_backgrounds/(?P<type>.*)/$',landslide_a.views.geological_backgrounds, name="geological_background")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)