from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib import messages
from gen.mixins import MainPageMixin
from users.models.user_profile import UserProfile
from gen.users.forms.new_user import NewUserForm


class Register(MainPageMixin, TemplateView):
    template_name = 'users/templates/register.html'

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['form'] = NewUserForm()

        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = NewUserForm(request.POST)

        if context['form'].is_valid():
            new_user = context['form'].save()
            profile = UserProfile.objects.create(user=new_user, phone=request.POST.get('phone'))
            profile.save()

            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            messages.success(request, u'%s, Добро пожаловать!' % request.user.username, )

            return HttpResponseRedirect(reverse('home'))

        return render(request, self.template_name, context)
