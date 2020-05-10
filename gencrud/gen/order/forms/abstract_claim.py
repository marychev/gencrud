from django.contrib.auth.models import User


class AbstractClaimForm:
    def __init__(self, post):
        self.post = post
        self.form = self.init_form()

        self.user_form = None
        self.anonymous_form = None

    def init_form(self):
        if self.post.get('user') and self.post.get('user') != 'None':
            user = User.objects.get(pk=int(self.post.get('user')))

            if user and user.is_authenticated:
                return self.user_form(self.post)
        else:
            return self.anonymous_form(self.post)
