from django.shortcuts import render, get_object_or_404
from landslide_a.models import Articles, About, main_block, outputs,person,event
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import View

# Create your views here.

def first_ua(request):
    articles = Articles.objects.order_by('id').reverse()[:4]
    about = About.objects.all()[:3]
    main_blocks = main_block.objects.all()
    return render(request, "home_ua.html", locals())


def article_ua(request, article_title):
    article = get_object_or_404(Articles, title=article_title)
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    return render(request, 'article_ua.html', locals())


def about_ua(request):
    return render(request, "about_ua.html", locals())


def news_ua(request):
    outputs_item = Articles.objects.order_by('id').reverse()
    paginator = Paginator(outputs_item, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    articles = Articles.objects.order_by('id').reverse()
    article_all = articles[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    return render(request, "news_ua.html", locals())


def output_ua(request, output_title):
    outputs_item = outputs.objects.all()
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    output_item = get_object_or_404(outputs, title=output_title)
    return render(request, "outputs.html", locals())


def contact_ua(request):
    outputs_item = outputs.objects.all()
    return render(request, "contact_ua.html", locals())


def case_studies_ua(request):
    partner = About.objects.all()[1:]
    return render(request, "case_studies_ua.html", locals())


def partners_detail_ua(request, partners_title):
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    partner_detailed = get_object_or_404(About, title=partners_title)
    return render(request, 'partners_detail_ua.html', locals())
def team_ua(request):
    team_person = person.objects.all()
    return render(request,"team_ua.html",locals())
def events_ua(request):
    event1 = event.objects.order_by("id").reverse()
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    return render(request,"events_ua.html",locals())


def specialevent_ua(request, event_title):
    even = get_object_or_404(event,title=event_title)
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    return render(request,"events_detail_ua.html",locals())
def sitemap(request):
    return render(request,"sitemap.xml",locals())


class search(View):

    def get(self, request, *args, **kwargs):
        context = {}

        q = request.GET.get('q')
        if q is not None:
            query_set = []
            q = request.GET.get('q')
            if q:
              # Общий QuerySet

                # Ищем по всем моделям
                article = Articles.objects.search_ua(query=q)
                events =event.objects.search_ua(query=q)
                count_fin = article.count()+events.count()
                # и объединяем выдачу


        return render(request, "search_ua.html",locals())


