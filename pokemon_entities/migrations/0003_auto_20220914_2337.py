# Generated by Django 3.1.14 on 2022-09-14 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_entities", "0002_auto_20220914_2331"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pokemon",
            name="img_url",
        ),
        migrations.AlterField(
            model_name="pokemonentity",
            name="pokemon",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entities",
                to="pokemon_entities.pokemon",
                verbose_name="Покемон",
            ),
        ),
    ]
