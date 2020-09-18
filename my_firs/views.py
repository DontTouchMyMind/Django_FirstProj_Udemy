from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is about page')


def home(request):
    return render(request, 'home.html', {'greeting': 'Hello!'})


def reverse(request):
    user_text = request.GET['message']
    words = len(user_text.split())
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'message': user_text,
                                            'reversed': reversed_text,
                                            'number_of_words': words})
