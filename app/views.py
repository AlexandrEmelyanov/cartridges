from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from .models import Orders
from .forms import SuperUserLoginForm


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
        'title': 'Cartridges status',
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

    context = {'form': form}
    return render(request=request, template_name='app/login.html', context=context)
