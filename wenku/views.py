from django.shortcuts import render
from .models import Article
from django.views import generic

# Create your views here.
def index(request):

    if request.method == "POST":        
        key = request.POST['key']
        if key.isdigit():
            b = Article.objects.filter(num=int(key))
        else:
            b = []
        a = Article.objects.filter(author=key)        
        c = Article.objects.filter(name__contains=key)
        article_list = list(a) + list(b) + list(c)
    elif request.method == 'GET':
        article_list = Article.objects.order_by('-last_update')[:50]

    context = {
    'article_list':article_list,
    }
    return render(request, 'wenku/index.html', context)

'''class IndexView(generic.ListView):
    template_name = 'wenku/index.html'
    context_object_name = 'article_list'
    defaul_lsit = Article.objects.order_by('-last_update')[:50]

    def get_queryset(self):
        return self.defaul_lsit'''

