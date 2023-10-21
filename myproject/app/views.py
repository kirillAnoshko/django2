from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django import forms

users = ['Вася Питонов', 'Петя Гадюкин']


class UserForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        min_length=5,
        label='Имя'
    )
    last_name = forms.CharField(
        max_length=100,
        min_length=5,
        label='Фамилия'
    )


def index(request):
    context = {
        'users': users
    }
    return render(request, 'app/index.html', context)


def add(request):
    if request.method == 'GET':
        form_fields = UserForm()
        context = {
            'form_fields': form_fields
        }
        return render(request, 'app/add.html', context)
    elif request.method == 'POST':
        form_fields = UserForm(request.POST)
        if form_fields.is_valid():
            first_name = form_fields.cleaned_data['first_name']
            last_name = form_fields.cleaned_data['last_name']
            user = first_name + ' ' + last_name
            users.append(user)
            return redirect('app:index')
        else:
            return render(request, 'app/add.html', context)
    else:
        return HttpResponseNotAllowed(
            ['POST', 'GET'],
            content='Ошибка Этот метод не разрешен!'
        )
