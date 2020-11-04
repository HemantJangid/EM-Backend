from middleware.response import unauthorized
from core.models import User
from util.firebase_auth import get_firebase_user_id


def auth_required():
    def authenticator(func):
        def wrap(context, request, *args, **kwargs):
            if 'HTTP_AUTHORIZATION' not in request.META:
                return unauthorized({})

            auth_token = request.META['HTTP_AUTHORIZATION']

            firebase_id = get_firebase_user_id(auth_token)
            if not firebase_id:
                return unauthorized({})

            user = User.objects.filter(id=firebase_id).first()
            if not user:
                return unauthorized({})

            request.user = user
            return func(context, request, *args, **kwargs)

        wrap.__name__ = func.__name__
        return wrap
    return authenticator
