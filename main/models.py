from typing import Any
from django.db import models
from django.contrib.auth import models as AuthModel
# Create your models here.

class EmployeAccountManager(models.BaseUserManager):

    def create_user(self, **kwargs: Any) -> Any:
        return

    def create_superuser(self,**kwargs):
        return 
class Employe(AuthModel.AbstractBaseUser):

    pass