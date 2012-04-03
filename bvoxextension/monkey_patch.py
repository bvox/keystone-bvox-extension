# vim: tabstop=4 shiftwidth=4 softtabstop=4

import keystoneclient.v2_0.users as users


def client():
   users.UserManager.get_by_name = __get_by_name 


def __get_by_name(self, user_name):
    return self._get("/users/by_name/{user_name}".format(
        user_name=user_name), "user")
