from django.contrib import messages
from django.http import JsonResponse
from django.views.generic.base import TemplateView

from gen.mixins import MainPageMixin
from gen.order.forms import FastClaimForm
from order.models.fast_claim import FastClaim


class BaseFastClaimFormView(MainPageMixin, TemplateView):
    form_class = FastClaimForm
    model = FastClaim

    def post(self, request, *args, **kwargs):
        form = FastClaimForm(request.POST).form

        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка оформлена!')

            return JsonResponse({
                'success': 'Заявка оформлена!',
                'data': form.data,
            })
        else:
            messages.error(request, '(: Произошла ошибка при отправке оформелнии...')
            return JsonResponse({'errors': form.errors})
