# myapp/middleware.py

from django.http import HttpResponseForbidden

class RestrictByIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = ['192.168.1.254']  # Reemplaza con la IP privada de tu router

    def __call__(self, request):
        ip = self.get_client_ip(request)
        if ip not in self.allowed_ips:
            return HttpResponseForbidden("Access denied.")
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
