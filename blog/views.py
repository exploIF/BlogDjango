from django.shortcuts import render

posts = [
    {
        'author': 'Igor Furgala',
        'title': 'My post',
        'content': 'blablabla',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Test user',
        'title': ' post',
        'content': 'ahahaha',
        'date_posted': 'August 27, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
