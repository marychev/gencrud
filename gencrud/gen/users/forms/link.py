from django import forms
from django.forms.formsets import BaseFormSet


class LinkForm(forms.Form):
    anchor = forms.CharField(
        max_length=100, required=False,
        widget=forms.TextInput(attrs={'placeholder':  ':Название', 'class': 'form-control'}), )
    url = forms.URLField(
        required=False, widget=forms.URLInput(attrs={'placeholder': ':URL / полнуй путь к странице', 'class': 'form-control'}))


class BaseLinkFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two links have the same anchor or URL
        and that all links have both an anchor and URL.
        """
        if any(self.errors):
            return

        anchors = []
        urls = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                anchor = form.cleaned_data['anchor']
                url = form.cleaned_data['url']

                # Check that no two links have the same anchor or URL
                if anchor and url:
                    if anchor in anchors:
                        duplicates = True
                    anchors.append(anchor)

                    if url in urls:
                        duplicates = True
                    urls.append(url)

                if duplicates:
                    raise forms.ValidationError('Ссылки должны иметь уникальные наименования и URL-адреса.', code='duplicate_links')
                # Check that all links have both an anchor and URL
                if url and not anchor:
                    raise forms.ValidationError('Все ссылки должны иметь наименование.', code='missing_anchor')
                elif anchor and not url:
                    raise forms.ValidationError('Все ссылки должны иметь URL-адрес.', code='missing_URL')

