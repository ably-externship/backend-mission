from datetime import datetime
from ..views import BaseView
from missions.week_1.back.crud.sql.help.help import HelpCrud
from django.shortcuts import render


class HelpBaseView(BaseView):
    pass


def get_help_list(request):
    parameter = BaseView.get_parameter(request)

    page = int(parameter.get('page') or 1)
    display_cnt = int(parameter.get('display_cnt') or 10)
    help_type = parameter.get('help_type') or None

    help_list = HelpCrud.get_help_list(page, display_cnt, help_type)

    data = {'helpList': help_list}

    return render(request, 'page/help.html', data)


def create_help(request):
    parameter = BaseView.get_parameter(request)
    help_form = parameter

    if not help_form.get('create_at'):
        help_form['created_at'] = datetime.now()
        help_form['updated_at'] = datetime.now()

    create, message = HelpCrud.create_help(help_form)

    help_list = HelpCrud.get_help_list(1, 10, None)
    if create:
        return render(request, 'page/help.html', {'helpList': help_list})

    return render(request, 'error.500.html', {'message': message})


