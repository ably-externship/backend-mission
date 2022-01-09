from .forms import HelpForm
from ..views import BaseView
from django.shortcuts import render, redirect
from missions.week_1.back.crud.sql.meta.user import UserCrud
from missions.week_1.back.crud.sql.help.help import HelpCrud


class HelpBaseView(BaseView):
    pass


def help_list_view(request):
    parameter = BaseView.get_parameter(request)

    page = int(parameter.get('page') or 1)
    display_cnt = int(parameter.get('display_cnt') or 10)
    help_type = parameter.get('help_type') or None

    help_list = HelpCrud.get_help_list(page, display_cnt, help_type)

    data = {'helpList': help_list}

    return render(request, 'page/help_list.html', data)


def help_form_view(request):
    return render(request, 'page/create_help.html', {})


def create_help(request):
    if not request.session.get('user'):
        return redirect('/users/login')

    form = HelpForm(request.POST)
    if form.is_valid():
        user_id = request.session.get('user')
        user = UserCrud.get_user(user_id)
        help_form = {
            'title': form.cleaned_data['title'],
            'contents': form.cleaned_data['contents'],
            'user': user[0].get('user_id')
        }
        HelpCrud.create_help(help_form)
        return redirect('/board/list')

    return render(request, 'board_write.html', {'form': form})

