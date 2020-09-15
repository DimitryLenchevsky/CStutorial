from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import FormBase


def submit(request):
    data = dict()

    if request.method == 'POST':
        form_a = FormBase(request.POST)

        if form_a.is_valid():
            base = form_a.save()
            base.type = 'Type A'
            base.type_id = base.id
            base.save()
            data['is_valid'] = True
        else:
            form_a = FormBase()

    else:
        data['is_valid'] = True

    context = {'form_a': form_a}
    data['html_form'] = render_to_string(
        'templates/form.html', context, request=request)
    return JsonResponse(data)
