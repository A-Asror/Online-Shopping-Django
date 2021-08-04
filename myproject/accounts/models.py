from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    image = models.ImageField(upload_to='avatars')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
