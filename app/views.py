from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import OrderCreateForm, SuperUserLoginForm
from .models import Orders


def main(request):
    if request.method == 'POST':
        info = request.POST.get('status')
        if info:
            data = info.split(' ')
            status = int(data[0])
            order = Orders.objects.get(id=int(data[1]))
            if order and status:
                order.status = status
                order.save()
                messages.success(request, 'Данные успешно изменены!')
                return HttpResponseRedirect(reverse('index:cartridges'))
        else:
            messages.error(request, 'Данный статус уже применен!')

    orders = Orders.objects.filter(status__lte=2)
    context = {
        'title': 'Статус заказов',
        'orders': orders,
    }

    return render(request=request, template_name='app/index.html', context=context)


def login(request):
    if request.method == 'POST':
        form = SuperUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request=request, user=user)
                return HttpResponseRedirect(reverse('index:cartridges'))

    else:
        form = SuperUserLoginForm()

    context = {
        'form': form,
        'title': 'Авторизация'
    }
    return render(request=request, template_name='app/login.html', context=context)


def create_order(request):
    if request.method == 'POST':
        form_create = OrderCreateForm(data=request.POST)
        if form_create.is_valid():
            new_order = Orders.objects.create(department=request.POST['department'])
            new_order.save()
            messages.success(request, 'Заказ успешно добавлен!')
            return HttpResponseRedirect(reverse('index:cartridges'))

    else:
        form_create = OrderCreateForm()

    context = {
        'form_create': form_create,
        'title': 'Создание заказа'
    }
    return render(request=request, template_name='app/create-order.html', context=context)
