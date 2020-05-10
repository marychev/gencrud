from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic.base import TemplateView

from gen.mixins import MainPageMixin
from gen.order.forms import ClaimCallerForm
from order.models import Claim


class ClaimCallerView(MainPageMixin, TemplateView):
    form_class = ClaimCallerForm
    model = Claim
    # template_name = 'home/home.html'

    def post(self, request, *args, **kwargs):
        Claim.objects.create(
            fio=request.POST.get('fio'),
            phone=request.POST.get('phone'),
            typeof=Claim.CALLER
        )
        form = ClaimCallerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка оформлена!')
        else:
            messages.error(request, '(: Произошла ошибка при отправке оформелнии...')
        return redirect('/')
