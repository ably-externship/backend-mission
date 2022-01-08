import json
from django.views import View
from django.shortcuts import render


class BaseView(View):
    @staticmethod
    def response(request, html, data):
        return render(request, html, data)

    @classmethod
    def get_parameter(cls, request):
        parameter = {}
        method = request.method
        if method == 'GET':
            query_dict = request.GET.copy()
            parameter = cls.query_dict_to_dict(query_dict)
        elif method == 'PUT':
            pass
        elif method == 'DELETE':
            print('DELETE')
        elif method == 'POST':
            body = json.loads(request.body)
            parameter = cls.query_dict_to_dict(body)

        return parameter

    @classmethod
    def query_dict_to_dict(cls, query_dict):
        res = {}
        for key in query_dict:
            res[key] = query_dict[key]

        return res