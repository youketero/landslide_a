from django.conf.urls import url
import landslide_a.views

urlpatterns = [
    url(r'^$', landslide_a.views.first, name="first"),

]