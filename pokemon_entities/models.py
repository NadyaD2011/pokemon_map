from django.db import models


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    photo = models.ImageField(upload_to="media/",
                            blank=True,
                            verbose_name="Фото покемона"
                            )

    def __str__(self):
        return self.title