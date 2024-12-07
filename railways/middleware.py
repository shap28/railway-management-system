from django.conf import settings

class AdminAPIMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin-api/'):
            api_key = request.headers.get('X-API-Key')
            if api_key != settings.ADMIN_API_KEY:
                return JsonResponse({"error": "Unauthorized"}, status=403)
        return self.get_response(request)
