# Generated by Django 2.1.4 on 2018-12-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendDjangoWelcome', '0002_remove_author_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorite',
            field=models.ManyToManyField(related_name='_author_favorite_+', to='backendDjangoWelcome.Recipe'),
        ),
    ]
