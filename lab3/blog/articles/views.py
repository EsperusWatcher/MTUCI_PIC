from .models import Article
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import Http404

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

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
                'title': request.POST.get("title", ""),
                'text': request.POST.get("text", "")
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
        
def registration(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        password_confirm = request.POST.get("password_confirm", "")
        
        form = {
            'username': username,
            'email': email
        }
        
        errors = []
        
        if not username:
            form['username_error'] = "Введите имя пользователя"
            errors.append('username_error')
        else:
            try:
                User.objects.get(username=username)
                form['username_error'] = "Пользователь с таким именем уже существует"
                errors.append('username_error')
            except User.DoesNotExist:
                pass
        
        if not email:
            form['email_error'] = "Введите email"
            errors.append('email_error')
        elif '@' not in email:
            form['email_error'] = "Введите корректный email"
            errors.append('email_error')
        
        if not password:
            form['password_error'] = "Введите пароль"
            errors.append('password_error')
        
        if password != password_confirm:
            form['password_confirm_error'] = "Пароли не совпадают"
            errors.append('password_confirm_error')
        
        if not errors:
            try:
                user = User.objects.create_user(username, email, password)
                login(request, user)
                return redirect('archive')
            except Exception as e:
                form['errors'] = f"Ошибка при создании пользователя: {str(e)}"
                return render(request, 'lab6_registration_form.html', {'form': form})
        else:
            form['errors'] = "Исправьте ошибки в форме"
            return render(request, 'lab6_registration_form.html', {'form': form})
    
    return render(request, 'lab6_registration_form.html', {})

def authentication(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        
        form = {
            'username': username,
            'password': password
        }
        
        errors = []
        
        if not username:
            form['username_error'] = "Введите имя пользователя"
            errors.append('username_error')
        
        if not password:
            form['password_error'] = "Введите пароль"
            errors.append('password_error')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('archive')
        else:
            form = {'errors': "Неверное имя пользователя или пароль"}
            return render(request, 'lab6_auth_form.html', {'form': form})
        
    return render(request, 'lab6_auth_form.html', {})

def user_logout(request):
    logout(request)
    return redirect("archive")