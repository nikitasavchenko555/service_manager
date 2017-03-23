from django.db import models
from django.contrib.auth.models import User
from manager.models import State, groups_of_work

# Create your models here.
def uknown_user():
    id = 777
    return id

class UserProfile(models.Model):
    # Эта строка обязательна. Она связывает UserProfile с экземпляром модели User.
    user = models.OneToOneField('auth.User')
    id_state = models.ForeignKey(State)
    group_of_work = models.ForeignKey(groups_of_work, default=uknown_user)
    #user_edit = models.ForeignKey('auth.User')
    class Meta:
        verbose_name = 'Список пользователей'
        verbose_name_plural = 'Списки пользователей'
    def __str__(self):
        return self.user.username

