from django.shortcuts import render

def cold_and_flu(request):
    return render(request, 'ColdAndFlu/ColdAndFlu.html')