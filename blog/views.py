from django.shortcuts import render

# Create your views here.


posts = [
    {
        'title': 'blog post 1',
        'author': 'coreyms',
        'date_posted': 'august 27, 2018',
        'content': 'first post content',
    },
    {
        'title': 'blog post 2',
        'author': 'jane',
        'date_posted': 'august 29, 2018',
        'content': 'second post content',
    }

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
