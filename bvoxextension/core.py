# vim: tabstop=4 shiftwidth=4 softtabstop=4

from keystone import exception
from keystone import identity
from keystone import policy
from keystone import token
from keystone.common import wsgi


class BvoxController(wsgi.Application):
    def __init__(self):
        self.identity_api = identity.Manager()
        self.token_api = token.Manager()
        self.policy_api = policy.Manager()
        super(BvoxController, self).__init__()

    def get_user_by_name(self, context, user_name):
        self.assert_admin(context)
        user_ref = self.identity_api.get_user_by_name(context, user_name)
        if not user_ref:
            raise UserNotFound(user_name=user_name)
        return {'user': user_ref}


class UserNotFound(exception.NotFound):
    """Could not find user by name: %(user_name)s"""
