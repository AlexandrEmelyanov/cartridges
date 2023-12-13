from django.shortcuts import render


def main(request):
    context = {
        'title': 'Cartridges status',
    }

    return render(request=request, template_name='app/index.html', context=context)
