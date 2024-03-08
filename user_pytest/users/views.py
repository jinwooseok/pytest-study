from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['GET','POST'])
def sign_up(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = User(username=username, password=password)
        user.save()
        return JsonResponse({'message': 'User created successfully!'}, status=201)
    else:
        return render(request, 'sign_up.html')