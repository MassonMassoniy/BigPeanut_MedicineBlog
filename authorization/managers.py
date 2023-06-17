from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, account_name, password=None):
        user = self.model(account_name=account_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, account_name, password):
        user = self.create_user(account_name=account_name, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.role_id = 1
        user.save(using=self._db)
        return user
