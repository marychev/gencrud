from django.views.generic.base import TemplateView
from django.forms.formsets import formset_factory
from gen.mixins import MainPageMixin
from order.models.order import Order
from gen.users.forms import LinkForm, BaseLinkFormSet


class Orders(MainPageMixin, TemplateView):
    template_name = 'users/templates/orders.html'
    # Create the formset, specifying the form and formset we want to use.
    LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

    def get_context_data(self, **kwargs):
        context = super(Orders, self).get_context_data(**kwargs)
        context['orders'] = Order.objects.filter(user=context['request'].user)
        return context

