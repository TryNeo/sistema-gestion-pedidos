from django.db import models
from django.contrib.auth.models import AbstractUser
from SistemaGestionPedidos.settings.base import MEDIA_URL,STATIC_URL


class User(AbstractUser):
    image = models.ImageField(upload_to="users/%Y/%m/%d",blank=True, null=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL,self.image)
        return '{}{}'.format(STATIC_URL,'images/user.png')

    def save(self, *args, **kwargs):
        if self.pk is None:
           self.set_password(self.password)
        else:
            user = User.objects.get(pk=self.pk)
            if user.password != self.password:
                self.set_password(self.password)
        super().save(*args, **kwargs)