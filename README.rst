BVOX Keystone extension
=======================
BVOX extension for Openstack Keystone right now just implements a get_by_name
API for both, the Keystone client and server. The server can be requested at
"/users/by_name/{user_name}" once the extension is enabled editing keystone.conf
(a sample is provided at tools/keystone.conf) admin API::

   $ curl http://localhost:35357/v2.0/BVOX/users?name=admin
   $ curl http://localhost:35357/v2.0/BVOX/tenants?name=admin

In order to use the client a monkey patch is provided::

   >>> from bvoxetension import monkey_patch
   >>> monkey_patch.client()
   >>> cli = client.Client(username='admin', password='secrete', tenant_name='admin', auth_url='http://localhost:35357/v2.0')
   >>> cli.users.get_by_name('demo')
   <User {u'id': u'74439b8d264545a19f76a0c0d379457e', u'tenantId': u'', u'enabled': True, u'name': u'demo', u'email': u'admin@example.com'}>
