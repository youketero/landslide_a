from django.shortcuts import render, get_object_or_404

from landslide_a.forms import form_user
from landslide_a.models import Articles, About, main_block, person, main_object, geological_background, \
    geological_objects, foto_news, form_user1
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
    foto = foto_news.objects.filter(type__title=article_title)
    articles = Articles.objects.order_by('id').reverse()[:8]
    return render(request, 'article_ua.html', locals())


def about_ua(request):
    return render(request, "about_ua.html", locals())


def news_ua(request):
    outputs_item = Articles.objects.order_by('id').reverse()
    paginator = Paginator(outputs_item, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    articles = Articles.objects.order_by('id').reverse()[:8]
    article_all = articles[:5]
    return render(request, "news_ua.html", locals())


def contact_ua(request):
    if request.method == "POST":
        form = form_user(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            last_name = request.POST.get("last_name")
            mail = request.POST.get("mail")
            phone = request.POST.get("phone")
            f = form_user1(name=name,last_name=last_name,mail=mail,phone=phone)
            f.save()
            return render(request, "contact_ua.html", locals())
    else:
        form = form_user()
        return render(request, "contact_ua.html", locals())


def case_studies_ua(request):
    partner = About.objects.all()[1:]
    return render(request, "case_studies_ua.html", locals())


def partners_detail_ua(request, partners_title):
    articles = Articles.objects.order_by('id').reverse()[:8]
    partner_detailed = get_object_or_404(About, title=partners_title)
    return render(request, 'partners_detail_ua.html', locals())

def team_ua(request):
    team_person = person.objects.all()
    return render(request,"team_ua.html",locals())


def team_detailed_ua(request,team_id):
    team = get_object_or_404(person, id = team_id)
    return render(request,"team_detailed_ua.html",locals())

def events_ua(request):
    articles = Articles.objects.order_by('id').reverse()[:8]
    return render(request,"events_ua.html",locals())


def specialevent_ua(request, event_title):
    articles = Articles.objects.order_by('id').reverse()[:8]
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
                count_fin = article.count()
                # и объединяем выдачу


        return render(request, "search_ua.html",locals())


def case_study_ua(request):
    main = main_object.objects.all()
    return render(request,"case_studies_ua.html",locals())

def geological_object_ua(request,type):
    geol = geological_objects.objects.filter(type_id__type_ua=type)
    titl = main_object.objects.filter(type_ua = type)
    return render(request, "geological_objects_ua.html",locals())

def geological_backgrounds_ua(request,type):
    geol = geological_background.objects.filter(type_id__type_ua=type)
    titl = main_object.objects.filter(type_ua = type)
    return render(request, "geological_background_ua.html",locals())