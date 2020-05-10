from gen.order.forms.fast_claim import FastClaimForm
from gen.tests.order.forms.mixins import AnonymousUserMixinTest


class ClaimFormModelAnonymousUserTest(AnonymousUserMixinTest):
    @property
    def valid_data(self):
        return {
            'user': self.user.pk,
            'email': 'anonymous@mail.com',
            'typeof': 0,
            'comment': 'Hello'
        }

    def test_valid(self):
        form = FastClaimForm(self.valid_data).form
        self.assertTrue(form.is_valid())

    def test_no_valid(self):
        post = self.valid_data.copy()
        post.update({'typeof': ''})
        form = FastClaimForm(post).form
        self.assertFalse(form.is_valid())

        post = self.valid_data.copy()
        post.update({'email': 'emailemail.com'})
        form = FastClaimForm(post).form
        self.assertFalse(form.is_valid())

        form = FastClaimForm({}).form
        self.assertFalse(form.is_valid())
