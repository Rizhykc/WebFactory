from django.shortcuts import render


def index(request):

    template = 'main/index.html'
    context = {
        'title':'Web Factory',
        'context':'',
    }
    return render(request, template, context)
