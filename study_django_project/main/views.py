from django.shortcuts import render

def index(request):
    data = {
        'title_h1': 'Главная страница',
        'values': ['red', 'black', 'orange'],
        'auto': {
            'car': 'BMW',
            'color': 'red',
            'year': '2022'
        }
    }

    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

