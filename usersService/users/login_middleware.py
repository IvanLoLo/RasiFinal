from django.http import JsonResponse
import os

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.excluded_paths = [('/users', 'GET'), ('/users/', 'GET'), ('/users/pacientes', 'POST'), ('/users/pacientes/', 'POST')]

    def __call__(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if (request.path, request.method) in self.excluded_paths:
            return self.get_response(request)

        if auth_header and auth_header.startswith('Bearer '):
            try: auth_header.split(' ')[1]
            except Exception as e:
                return JsonResponse({'error': 'Forbidden - Invalid token'}, status=403)
        else:
            # No token provided, access denied
            return JsonResponse({'error': 'An access token is required to proceed'}, status=401)
        
        return self.get_response(request)