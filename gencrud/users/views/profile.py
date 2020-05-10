from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.db import IntegrityError, transaction
from gen.mixins import MainPageMixin
from gen.users.forms.link import LinkForm, BaseLinkFormSet
from gen.users.forms.profile import ProfileForm
from users.models.user_link import UserLink


class Profile(MainPageMixin, TemplateView):
    """
    Allows a user to update their own profile.
    """
    template_name = 'users/templates/profile.html'
    # Create the formset, specifying the form and formset we want to use.
    LinkFormSet = formset_factory(LinkForm, formset=BaseLinkFormSet)

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        user = context['request'].user
        # Get our existing link data for this user.  This is used as initial data.
        user_links = UserLink.objects.filter(user=user).order_by('anchor')
        link_data = [{'anchor': l.anchor, 'url': l.url} for l in user_links]
        context['profile_form'] = ProfileForm(user=user)
        context['link_formset'] = self.LinkFormSet(initial=link_data)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        user = context['request'].user
        context['profile_form'] = ProfileForm(request.POST, user=user, initial={'email': user.email})
        context['link_formset'] = self.LinkFormSet(request.POST)

        if context['profile_form'].is_valid() and context['link_formset'].is_valid():
            # Save user info
            user.first_name = context['profile_form'].cleaned_data.get('first_name')
            user.last_name = context['profile_form'].cleaned_data.get('last_name')
            user.save()
            # todo: save for form development
            context['profile_form'].save()
            # Now save the data for each form in the formset
            new_links = []
            for link_form in context['link_formset']:
                anchor = link_form.cleaned_data.get('anchor')
                url = link_form.cleaned_data.get('url')
                if anchor and url:
                    new_links.append(UserLink(user=user, anchor=anchor, url=url))

            try:
                with transaction.atomic():
                    # Replace the old with the new
                    UserLink.objects.filter(user=user).delete()
                    UserLink.objects.bulk_create(new_links)
                    messages.success(request, 'Профиль обнавлен.')
            except IntegrityError:  # If the transaction failed
                messages.error(request, 'Ошибка в вашем профиле.')
            return HttpResponseRedirect(reverse('profile'))

        return render(request, self.template_name, context)
