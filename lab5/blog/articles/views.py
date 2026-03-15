from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST.get("text", ""),
                'title': request.POST.get("title", "")
            }
            
            if Article.objects.filter(title=form["title"]).exists():
                form['title_error'] = "Такое название уже существует"
                return render(request, 'lab5_create_post.html', {'form': form})

            if form["text"] and form["title"]:
                article = Article.objects.create(
                    text=form["text"],
                    title=form["title"],
                    author=request.user
                )
                return redirect('get_article', article_id=article.id)
            else:
                form['errors'] = "Не все поля заполнены"
                return render(request, 'lab5_create_post.html', {'form': form})
        else:
            return render(request, 'lab5_create_post.html', {})
    else:
        raise Http404
        
def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})