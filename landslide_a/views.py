from django.shortcuts import render,get_object_or_404
from landslide_a.models import Articles,About,main_block
# Create your views here.
def first(request):
    articles = Articles.objects.order_by('id').reverse()[:3]
    about = About.objects.all()
    main_blocks = main_block.objects.all()
    return render(request, "home.html",locals())

def article(request,article_title):
    article =  get_object_or_404(Articles, title=article_title)
    articles = Articles.objects.order_by('id').reverse()[:10]
    return render(request, 'article.html', locals())

