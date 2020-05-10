from django import forms
from catalog.models.product_comment import ProductComment
from gen.utils.abstract_forms import ABSCommentForm


class CommentForm(ABSCommentForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget = forms.HiddenInput()

        if 'initial' in kwargs.keys():
            obj = kwargs['initial']['obj']
            self.fields['product'].initial = obj

    class Meta:
        model = ProductComment
        exclude = ('is_show',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
