from django.shortcuts import render

# Create your views here.


def index(request):
    """ display page"""
    return render(request, 'portfolio_app/index.html')



def About_me(request):
    """ About me page """
    return render(request, 'portfolio_app/About_me.html')


def Blog(request):
    """ blog posts """
    return render(request, 'portfolio_app/Blog.html')


def contact(request):
    """ contact me page """
    return render(request, 'portfolio_app/contact.html')

def portfolio(request):
    """ display full portfolio """
    return render(request, 'portfolio_app/portfolio.html')

