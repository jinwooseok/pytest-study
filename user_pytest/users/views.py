from django.shortcuts import render
from django.http import JsonResponse
from .models import User
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User(username=username, password=password)
        user.save()
        return JsonResponse({'message': 'User created successfully!'}, status=201)
    elif request.method == 'GET':
        return render(request, 'sign_up.html')
    return 0