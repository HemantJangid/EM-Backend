from middleware.response import unauthorized
from core.models import User


def auth_required():
    def authenticator(func):
        def wrap(context, request, *args, **kwargs):
            # if 'HTTP_AUTHORIZATION' not in request.META:
            #     return unauthorized({})
            #
            # auth_token = request.META['HTTP_AUTHORIZATION']

            user = User.objects.filter(id="1").first()
            if not user:
                return unauthorized({})

            request.user = user
            return func(context, request, *args, **kwargs)

        wrap.__name__ = func.__name__
        return wrap
    return authenticator
