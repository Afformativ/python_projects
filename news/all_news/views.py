from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView,UpdateView,DeleteView



def news_home(request):
    #news=Articles.objects.order_by('-date')[:1]    one article
    news=Articles.objects.order_by('-date') 
    return render(request,'all_news/news_home.html',{'news':news})

class NewsDetailView(DetailView):
    model=Articles
    template_name='all_news/details_views.html'
    context_object_name='article'

class NewsUpdateView(UpdateView):
    model=Articles
    template_name='all_news/create.html'
    
    form_class=ArticlesForm

class NewsDeleteView(DeleteView):
    model=Articles
    template_name='all_news/news_delete.html'
    success_url='/news/'

def create(request):
    if request.method=='POST':
        form=ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error='Form was incorrect'
    
    form=ArticlesForm()
    
    data={
        'form':form,
        'error':error
    }
    return render(request,'all_news/create.html',data)