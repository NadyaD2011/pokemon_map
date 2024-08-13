from django.db import models
from django.utils import timezone


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название покемона")
    photo = models.ImageField(upload_to="media/",
                            blank=True,
                            verbose_name="Фото покемона"
                            )

    def __str__(self):
        return self.title
    

class PokemonEntity(models.Model):
    latitude = models.FloatField(verbose_name="Широта")
    longtitude = models.FloatField(verbose_name="Долгота")
    pokemon = models.ForeignKey(
                            Pokemon,
                            on_delete=models.CASCADE,
                            verbose_name="Покемон",
                            related_name='entities'
                                )
    appeared_at = models.DateTimeField(
                                    default=timezone.now,
                                    verbose_name="Время появления"
                                    )
    disappeared_at = models.DateTimeField(
                                          default=timezone.now,
                                          verbose_name="Время исчезновения"
                                          )
    level = models.IntegerField(blank=True, verbose_name="Уровень")
    health = models.IntegerField(null=True,
                                 blank=True,
                                 verbose_name="Здоровье"
                                 )
    strength = models.IntegerField(null=True, blank=True, verbose_name="Сила")
    defence = models.IntegerField(null=True, blank=True, verbose_name="Защита")
    stamina = models.IntegerField(null=True,
                                  blank=True,
                                  verbose_name="Выносливость"
                                  )