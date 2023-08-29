# Generated by Django 4.0 on 2023-08-28 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_log_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clients.user', verbose_name='Пользователь (Создатель)'),
            preserve_default=False,
        ),
    ]