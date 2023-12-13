from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Orders


def main(request):
    if request.method == 'POST':
        info = request.POST.get('status').split(' ')
        if info:
            status = int(info[0])
            order = Orders.objects.get(id=int(info[1]))
            if order and status:
                order.status = status
                order.save()
                return HttpResponseRedirect(reverse('index:cartridges'))

    orders = Orders.objects.filter(status__lte=2)
    context = {
        'title': 'Cartridges status',
        'orders': orders,
    }

    return render(request=request, template_name='app/index.html', context=context)
