from django.http import JsonResponse
import os

class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Bearer '):
            try: auth_header.split(' ')[1]
            except Exception:
                return JsonResponse({'error': 'Forbidden - Invalid token'}, status=403)
        else:
            # No token provided, access denied
            return JsonResponse({'error': 'An access token is required to proceed'}, status=401)
        
        return self.get_response(request)