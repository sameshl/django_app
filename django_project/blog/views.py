from django.shortcuts import render

posts = [
    {
        'author': 'Samesh Lakhotia',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 9,2019'
    },
    {
        'author': 'Harley Quinn',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 10,2019'
    }
]


# Create your views here.

def home(request):
    context = {
        'posts': posts,
        'title': "Home"
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': "About Us"})
