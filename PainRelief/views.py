from django.shortcuts import render

def pain_relief(request):
    return render(request, 'PainRelief/PainRelief.html')