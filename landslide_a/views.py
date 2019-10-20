from django.shortcuts import render, get_object_or_404
from landslide_a.models import Articles, About, main_block, outputs,person,event
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import View

# Create your views here.

def first(request):
    articles = Articles.objects.order_by('id').reverse()[:4]
    about = About.objects.all()[:3]
    main_blocks = main_block.objects.all()
    return render(request, "home.html", locals())


def article(request, article_title):
    article = get_object_or_404(Articles, title=article_title)
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    return render(request, 'article.html', locals())


def about(request):
    return render(request, "about.html", locals())


def news(request):
    outputs_item = Articles.objects.order_by('id').reverse()
    paginator = Paginator(outputs_item, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    articles = Articles.objects.order_by('id').reverse()
    article_all = articles[:5]
    outputs_item = outputs.objects.all()
    events_1 = event.objects.order_by("id").reverse()[:5]
    return render(request, "news.html", locals())


def output(request, output_title):
    outputs_item = outputs.objects.all()
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    output_item = get_object_or_404(outputs, title=output_title)
    return render(request, "outputs.html", locals())


def contact(request):
    outputs_item = outputs.objects.all()
    return render(request, "contact.html", locals())


def case_studies(request):
    partner = About.objects.all()[1:]
    return render(request, "case_studies.html", locals())


def partners_detail(request, partners_title):
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    partner_detailed = get_object_or_404(About, title=partners_title)
    return render(request, 'partners_detail.html', locals())
def team(request):
    team_person = person.objects.all()
    return render(request,"team.html",locals())
def events(request):
    event1 = event.objects.order_by("id").reverse()
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    return render(request,"events.html",locals())


def specialevent(request, event_title):
    even = get_object_or_404(event,title=event_title)
    articles = Articles.objects.order_by('id').reverse()[:5]
    events_1 = event.objects.order_by("id").reverse()[:5]
    return render(request,"events_detail.html",locals())
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
                article = Articles.objects.search(query=q)
                events =event.objects.search(query=q)
                count_fin = article.count()+events.count()
                # и объединяем выдачу


        return render(request, "search.html",locals())


