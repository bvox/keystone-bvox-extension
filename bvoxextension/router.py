# vim: tabstop=4 shiftwidth=4 softtabstop=4

from keystone.common import wsgi

import bvoxextension.core as core


class BvoxExtension(wsgi.ExtensionRouter):
    """
    BVOX Keystone extension extends Keystone's API adding all functionality
    we need but don't fit into Keystone core.
    """

    def add_routes(self, mapper):
        bvox_controller = core.BvoxController()

        # User operations
        mapper.connect('/BVOX/users', controller=bvox_controller,
                action='get_user',
                conditions=dict(method=['GET']))
        # Tenant operations
        mapper.connect('/BVOX/tenants', controller=bvox_controller,
                action='get_tenant',
                conditions=dict(method=['GET']))
