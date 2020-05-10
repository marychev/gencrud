from django import forms
from ..models.post_comment import Comment
from gen.utils.abstract_forms import ABSCommentForm


class CommentForm(ABSCommentForm):
    class Meta:
        model = Comment
        exclude = ('is_show', )
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['post'].widget = forms.HiddenInput()

        if 'initial' in kwargs.keys():
            obj = kwargs['initial']['obj']
            self.fields['post'].initial = obj
