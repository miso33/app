from allauth.account.adapter import DefaultAccountAdapter


class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        path = "/"
        return path.format(username=request.user.username)
