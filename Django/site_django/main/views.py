from django.shortcuts import render

# Create your views here.
data = {
    'title':'Головна сторінка',
    'values':['some', 'hello', '123'],
    'obj':{
        'car':'Mercedes',
        'age': 18,
        'hobby': 'football'
    }
}

def index(request):
    return render(request, 'main/index.html', data)
def about(request):
    return render(request, 'main/about.html')
