from django.conf.urls import url
import landslide_a_ua.views
from landslide import  settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', landslide_a_ua.views.first_ua, name="first_ua"),
    url(r'^новини/(?P<article_title>.*)/$',landslide_a_ua.views.article_ua,name = "article_ua"),
    url(r'^про нас/$',landslide_a_ua.views.about_ua,name="about_ua"),
    url(r'^новини/$',landslide_a_ua.views.news_ua,name="news_ua"),
    url(r'^контакти/$',landslide_a_ua.views.contact_ua,name="contact_ua"),
    url(r'^дослідження/$',landslide_a_ua.views.case_studies_ua,name="case_studies_ua"),
    url(r'^partners/(?P<partners_title>.*)/$',landslide_a_ua.views.partners_detail_ua, name="partners_detail_ua"),
    url(r'^команда/$',landslide_a_ua.views.team_ua, name="our team_ua"),
    url(r'^sitemap/$',landslide_a_ua.views.sitemap,name="sitemap"),
    url(r'^пошук/$', landslide_a_ua.views.search.as_view(), name="search_ua"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)