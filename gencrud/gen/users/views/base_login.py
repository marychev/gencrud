from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth import login, logout, authenticate
from gen.mixins import MainPageMixin
from gen.users.forms.custom_authentication import CustomAuthenticationForm


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


class BaseLoginView(MainPageMixin, TemplateView):
    template_name = 'users/templates/login.html'

    def get_context_data(self, **kwargs):
        context = super(BaseLoginView, self).get_context_data(**kwargs)

        context['form'] = CustomAuthenticationForm()

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = CustomAuthenticationForm(request, request.POST)

        if context['form'].is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)

            return HttpResponseRedirect(reverse('home'))

        return render(request, self.template_name, context)
