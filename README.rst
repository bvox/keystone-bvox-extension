BVOX Keystone extension
=======================
BVOX extension for Openstack Keystone right now just implements a user/tenant
query by name API for OpenStack Keystone server. The server can be requested at
"/BVOX/[users|tenants]?name={name}" once the extension is enabled editing keystone.conf
(a sample is provided at tools/keystone.conf) admin API::

   $ curl http://localhost:35357/v2.0/BVOX/users?name=admin
   $ curl http://localhost:35357/v2.0/BVOX/tenants?name=admin

Client API
----------

This server extension has Keystone client companion, providing the client
part. See `keystoneclient-bvox-ext at GitHub
<https://github.com/bvox/keystoneclient-bvox-extension>`.

Working with code
-----------------

See HACKING.rst for guidelines while working with this code. Please *do not
update HACKING.rst directly*, but edit
`HACKING.rst Gist <https://gist.github.com/3945275>`_ instead and then
re-import here.
