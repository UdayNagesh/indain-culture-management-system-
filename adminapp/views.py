from django.shortcuts import render


# Create your views here.
def adminhome(request):
    return render(request, 'adminhome.html')


def logout(request):
    return render(request, 'login.html')
