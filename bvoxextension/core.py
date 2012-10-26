'''BVOX extension controller.'''
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

    def get_user(self, context):
        '''Filters users by name (exact match only).'''
        self.assert_admin(context)
        user_name = context['query_string'].get('name')
        if user_name:
            return self._get_user_by_name(context, user_name)

        raise exception.ValidationError(
            attribute='name filter',
            target='querystring')

    def _get_user_by_name(self, context, user_name):
        user_ref = self.identity_api.get_user_by_name(context, user_name)

        if not user_ref:
            raise UserNotFound(user_name=user_name)
        return {'user': user_ref}

    def get_tenant(self, context):
        '''Filters tenants by name (exact match only).'''
        self.assert_admin(context)
        tenant_name = context['query_string'].get('name')
        if tenant_name:
            return self._get_tenant_by_name(context, tenant_name)

        raise exception.ValidationError(
            attribute='name filter',
            target='querystring')

    def _get_tenant_by_name(self, context, tenant_name):
        tenant_ref = self.identity_api.get_tenant_by_name(context, tenant_name)

        if not tenant_ref:
            raise TenantNotFound(tenant_name=tenant_name)
        return {'tenant': tenant_ref}


class UserNotFound(exception.NotFound):
    """Could not find user by name: %(user_name)s"""


class TenantNotFound(exception.NotFound):
    """Could not find tenant by name: %(tenant_name)s"""
