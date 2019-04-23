from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html', {})

def blog1(request):
    return render(request, 'blog1.html', {})

def blog2(request):
    return render(request, 'blog2.html', {})

def sitemap(request):
    return render(request, 'sitemap.xml', {})

def cookies(request):
    return render(request, 'cookies.html', {})

def restfreevzor(request):
    return render(request, 'restfreetemplate.html', {})

def eshopyfreevzor(request):
    return render(request, 'eshopyfreetemplate.html', {})

def realitkyfreevzor(request):
    return render(request, 'realitkyfreetemplate.html', {})
