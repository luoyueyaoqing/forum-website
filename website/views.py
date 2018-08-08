from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from .models import User, Article, Plate, Comment
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def index_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not User.objects.filter(username=username).exists():
            if password1 == password2:
                User.objects.create_user(username=username, password=password1)
                messages.success(request, '注册成功')
                return redirect(to='login')
            else:
                messages.warning(request, '两次密码输入不一致')
        else:
            messages.warning(request, "账号已存在")
    return render(request, 'register.html')


def index_login(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if next_url:
                return redirect(next_url)
            return redirect('index')
        return HttpResponseRedirect(request.get_full_path())
    return render(request, 'login.html', {'next_url': next_url})


def index_logout(request):
    logout(request)
    return redirect(to=index)


def index(request):
    plates = Plate.objects.all()
    return render(request, 'index.html', {'plates': plates})


def articles(request, id):
    plate = Plate.objects.get(id=id)
    articles = Article.objects.all()
    return render(request, 'articles.html', locals())


def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'detail.html', {'article': article})


@login_required
def add_article(request, id):
    if request.method == "POST":
        plate = Plate.objects.get(id=id)
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article.objects.create(title=title, content=content, author=request.user, column=plate)
        return redirect(to='articles', id=id)
    else:
        return render(request, 'add_article.html')


@login_required
def comment(request, id):
    article = Article.objects.get(id=id)
    content = request.POST.get('content')
    # user = request.user
    # Comment.objects.create(content=content, user=user, article=article)
    article.comment_this(user=request.user, content=content)
    messages.success(request, '评论成功')
    return redirect(to='detail', id=article.id)


@login_required
def edit(request, id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(to=detail, id=id)
    return render(request, 'edit.html', {'article': article})


@login_required
def del_article(request, id):
    if request.method == "GET":
        article = Article.objects.get(id=id)
        column = article.column
        article.delete()
    return redirect(to=articles, id=column.id)


@login_required
def del_comment(request, id):
    if request.method == "GET":
        comment = Comment.objects.get(id=id)
        comment.delete()
        article = comment.article
        messages.success(request, "评论已删除")
    return redirect(to=detail, id=article.id)