from django.shortcuts import render,get_object_or_404
from landslide_a.models import Articles,About,main_block,outputs
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def first(request):
    articles = Articles.objects.order_by('id').reverse()[:3]
    about = About.objects.all()
    main_blocks = main_block.objects.all()
    outputs_item = outputs.objects.all()
    return render(request, "home.html",locals())
def article(request,article_title):
    article = get_object_or_404(Articles, title=article_title)
    articles = Articles.objects.order_by('id').reverse()[:5]
    outputs_item = outputs.objects.all()
    return render(request, 'article.html', locals())
def about(request):
    outputs_item = outputs.objects.all()
    return render(request, "about.html",locals())
def news(request):
    outputs_item = Articles.objects.order_by('id').reverse()
    paginator  = Paginator(outputs_item,10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    articles = Articles.objects.order_by('id').reverse()
    article_all = articles[:5]
    return render(request, "news.html",locals())
def output(request,output_title):
    outputs_item = outputs.objects.all()
    articles = Articles.objects.order_by('id').reverse()[:5]
    output_item = get_object_or_404(outputs, title = output_title)
    return render(request,"outputs.html",locals())
def contact(request):
    return render(request, "contact.html",locals())