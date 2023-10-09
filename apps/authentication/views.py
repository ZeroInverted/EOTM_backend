from django.http import JsonResponse
from django.views import View
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.db import transaction
from apps.management.models import Employee
import json
import jwt

class EmployeeLogin(View):
    
    def get(self, request):
        csrf_token = get_token(request)
        return JsonResponse({"X-CSRFToken": csrf_token})
    
    def post(self, request):
        request_data = json.loads(request.body)
        username = request_data.get("username")
        password = request_data.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user and user.is_authenticated:
            login(request, user)
            user_id = user.id         
        else:
            return JsonResponse({
                "access_token": None,
            })
        token = jwt.encode({"id": user_id}, settings.SECRET_KEY)
        return JsonResponse({"access_token": token})
    
class EmployeeLogout(View):
    
    def get(self, request):
        csrf_token = get_token(request)
        return JsonResponse({"X-CSRFToken": csrf_token})
    
    def post(self, request):
        try:
            logout(request)
            return JsonResponse({"success":"True"})
        except Exception as e:
            return JsonResponse({"success":"False"})
        
class EmployeePasswordReset(View):
    
    def get(self, request):
        csrf_token = get_token(request)
        return JsonResponse({"X-CSRFToken": csrf_token})
    
    def post(self, request):
        try:
            request_data = json.loads(request.body)
            user_username = request_data.get("username")
            new_password = request_data.get("password")
            user = Employee.objects.get(username = user_username)
            if not user:
                return JsonResponse({"success":"False"})
            else:
                with transaction.atomic():
                    user.set_password(new_password)
                    user.save()
                return JsonResponse({"success":"True"})
        except Exception as e:
            return JsonResponse({"success":"False"})