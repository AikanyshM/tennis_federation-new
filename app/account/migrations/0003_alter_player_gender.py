# Generated by Django 3.2 on 2023-01-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_player_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=100, verbose_name='Пол'),
        ),
    ]
