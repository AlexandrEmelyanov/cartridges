from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

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
        'title': 'Cartridges status',
        'orders': orders,
    }

    return render(request=request, template_name='app/index.html', context=context)
