import django.db
from django.contrib.auth.models import User

from manager import models
from manager.models import State, groups_of_work
from django.db import models


# Create your models here.
def uknown_user():
    id = 777
    return id


class UserProfile(models.Model):
    # Эта строка обязательна. Она связывает UserProfile с экземпляром модели User.
    user = models.OneToOneField('auth.User',on_delete=models.DO_NOTHING)
    id_state = models.ForeignKey(State,on_delete=models.DO_NOTHING)
    group_of_work = models.ForeignKey(groups_of_work, default=uknown_user,on_delete=models.DO_NOTHING)

    # user_edit = models.ForeignKey('auth.User')
    class Meta:
        verbose_name = 'Список пользователей'
        verbose_name_plural = 'Списки пользователей'

    def __str__(self):
        return self.user.username
