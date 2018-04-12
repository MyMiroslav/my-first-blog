from django.shortcuts import render
from django.utils import timezone
from .models import Post,TelegraphArticle
from .logic import GetPageContentOfTelegraph
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
	
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html')
	
def new_telegraph_article_form(request):    
    return render(request, 'blog/new_telegraph_article_form.html')
	
	
def add_and_parse_new_telegraph_article(request):
    url_article=request.POST["field_tph"]
    page_content = GetPageContentOfTelegraph ( url_article )
    image_full_adres = "http://telegra.ph" + str(page_content["img"])
    insert_into_queryset = Post(title=page_content["h1"],image=image_full_adres,text=page_content["p"],url_adres_article=url_article,published_date = timezone.now())
    insert_into_queryset.save()	
   #parse new article
   #insert article data to post list
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})