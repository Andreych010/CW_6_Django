# Generated by Django 4.2.4 on 2023-08-28 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0008_alter_newsletter_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('body', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog_post/', verbose_name='изображение')),
                ('date_creation', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('sign_publication', models.BooleanField(verbose_name='признак публикации')),
                ('number_views', models.IntegerField(blank=True, null=True, verbose_name='количество просмотров')),
                ('newsletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='clients.newsletter', verbose_name='рассылка для блога')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'ordering': ('id',),
            },
        ),
    ]
