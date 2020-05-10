from django.views.generic.base import ContextMixin

from gen.cart.cart import Cart
from home.models.home import Home
from gen.order.forms import FastClaimForm, ProductClaimForm
from settings_template.models.footer import Footer
from settings_template.models.main_menu import MainMenu
from settings_template.models.settings_template import SettingsTemplate
from site_info.models.social_network import SocialNetwork


class MainMenuMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(MainMenuMixin, self).get_context_data(**kwargs)
        context['current_url'] = self.request.path
        context['mainmenu'] = MainMenu.queryset_not_cloned()
        return context


class HomeMixin(MainMenuMixin):
    def get_context_data(self, **kwargs):
        context = super(HomeMixin, self).get_context_data(**kwargs)
        context['setting_template'] = get_settings_template()
        try:
            if context['setting_template'] and context['setting_template'].home:
                context['home'] = Home.objects.get(id=context['setting_template'].home.id, is_show=True)
        except Home.DoesNotExist:
            context['home'] = None
        context['social_network'] = SocialNetwork.objects.all()
        return context


class FooterMixin(HomeMixin):
    def get_context_data(self, **kwargs):
        context = super(FooterMixin, self).get_context_data(**kwargs)
        context['footer'] = Footer.objects.filter(is_show=True).first()
        return context


class MainPageMixin(FooterMixin):
    def get_context_data(self, **kwargs):
        context = super(MainPageMixin, self).get_context_data(**kwargs)

        context['request'] = self.request
        context['cart'] = Cart(self.request).get()
        context['profile'] = get_profile_request(self.request)
        context['fast_claim_form'] = FastClaimForm(self.request.POST)
        context['product_claim_form'] = ProductClaimForm(self.request.POST)

        return context


def get_settings_template():
    return SettingsTemplate.objects.filter(is_included=True).first()


def get_profile_request(request):
    from users.models.user_profile import UserProfile

    if request.user and request.user.is_authenticated:
        try:
            return UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            from gen.utils.todo import create_bug_issue
            create_bug_issue("[war]: User: {} doesn't have a self `profile`!".format(request.user))

