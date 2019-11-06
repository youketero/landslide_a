from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from landslide_a.forms import form_user
from landslide_a.models import Articles, About, main_block, outputs, person, geological_objects, main_object, foto_news, \
    geological_background,form_user1
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views import View

# Create your views here.

def first(request):
    articles = Articles.objects.order_by('id').reverse()[:4]
    about = About.objects.all()[:3]
    main_blocks = main_block.objects.all()
    return render(request, "home.html", locals())


def article(request, article_title):
    article = get_object_or_404(Articles, title = article_title)
    foto = foto_news.objects.filter(type__title = article_title)
    articles = Articles.objects.order_by('id').reverse()[:8]
    return render(request, 'article.html', locals())


def about(request):
    team_person = person.objects.all()
    return render(request, "about.html", locals())


def news(request):
    outputs_item = Articles.objects.order_by('id').reverse()
    paginator = Paginator(outputs_item, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    articles = Articles.objects.order_by('id').reverse()
    article_all = articles[:5]
    return render(request, "news.html", locals())

def contact(request):
    if request.method == "POST":
        form = form_user(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            last_name = request.POST.get("last_name")
            mail = request.POST.get("mail")
            phone = request.POST.get("phone")
            f = form_user1(name=name,last_name=last_name,mail=mail,phone=phone)
            f.save()
            return render(request, "contact.html", locals())
    else:
        form = form_user()
        return render(request, "contact.html", locals())

def case_studies(request):
    partner = About.objects.all()[1:]
    geol = geological_objects.objects.all()
    return render(request, "case_studies.html", locals())


def partners_detail(request, partners_title):
    articles = Articles.objects.order_by('id').reverse()[:8]
    partner_detailed = get_object_or_404(About, title=partners_title)
    return render(request, 'partners_detail.html', locals())
def team(request):
    team_person = person.objects.all()
    return render(request,"team.html",locals())

def team_detailed(request,team_id):
    team = get_object_or_404(person, id = team_id)
    return render(request,"team_detailed.html",locals())

def events(request):
    articles = Articles.objects.order_by('id').reverse()[:8]
    return render(request,"events.html",locals())

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
                count_fin = article.count()
                # и объединяем выдачу


        return render(request, "search.html",locals())


def case_study(request):
    main = main_object.objects.all()
    return render(request,"case_stud.html",locals())

def geological_object(request,type):
    geol = geological_objects.objects.filter(type_id__type=type)
    titl = main_object.objects.filter(type = type)
    return render(request, "geological_objects.html",locals())

def geological_backgrounds(request,type):
    geol = geological_background.objects.filter(type_id__type=type)
    titl = main_object.objects.filter(type = type)
    return render(request, "geological_background.html",locals())