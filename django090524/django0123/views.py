from django.shortcuts import render, HttpResponse

def page_index1(request):
    a = 10
    return render(request, 'django0123/home.html', {'obj': request})

