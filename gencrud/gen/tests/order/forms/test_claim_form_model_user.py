from gen.order.forms.fast_claim import FastClaimForm
from gen.tests.order.forms.mixins import AuthUserMixinTest


class ClaimFormModelAuthUserTest(AuthUserMixinTest):
    @property
    def valid_data(self):
        return {
            'user': self.user.pk,
            'email': self.user.email,
            'typeof': 0,
            'comment': 'Hello'
        }

    def test_valid(self):
        form = FastClaimForm(self.valid_data).form
        self.assertTrue(form.is_valid())

    def test_start_valid_data(self):
        post = self.valid_data.copy()
        del post['comment']
        post.update({'user': None})
        form = FastClaimForm(post).form
        self.assertTrue(form.is_valid())

    def test_no_valid_typeof_with_authorization(self):
        post = self.valid_data.copy()
        post.update({'user': None, 'email': 'emailgmail.com'})
        form = FastClaimForm(post).form
        self.assertFalse(form.is_valid())

        post = self.valid_data.copy()
        post.update({'typeof': None})
        form = FastClaimForm(post).form
        self.assertFalse(form.is_valid())

        post = self.valid_data.copy()
        post.update({'typeof': 0, 'email': '124312432143'})
        form = FastClaimForm(post).form
        self.assertFalse(form.is_valid())
