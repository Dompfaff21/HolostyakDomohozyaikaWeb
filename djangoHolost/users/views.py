from django.shortcuts import render

# Create your views here.
def create_user(request):
    return render(request, 'reg.html')