from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'index.html', {})

def cookies(request):
    return render(request, 'cookies.html', {})
