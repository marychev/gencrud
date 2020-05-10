from django.views.generic.base import TemplateView
from django.forms.formsets import formset_factory
from gen.mixins import MainPageMixin
from catalog.models import ProductComment
from gen.users.forms import LinkForm, BaseLinkFormSet


class ReviewProducts(MainPageMixin, TemplateView):
    """
    Все заказы пользователя в личном кабинете
    """
    template_name = 'users/templates/reviews.html'
    LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

    def get_context_data(self, **kwargs):
        context = super(ReviewProducts, self).get_context_data(**kwargs)
        # todo: [?] email: or id:
        context['review_products'] = ProductComment.objects.filter(email=self.request.user.email)
        return context
