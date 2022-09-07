from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

# def testimonal(request):
#     return render(request, 'testimonal.html', {})