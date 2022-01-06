from django.views import View
from django.http import JsonResponse


class BaseView(View):
    @staticmethod
    def response(response, message, status_code=200):
        result = {
            'result': response,
            'message': message,
        }
        return JsonResponse(result, status=status_code)