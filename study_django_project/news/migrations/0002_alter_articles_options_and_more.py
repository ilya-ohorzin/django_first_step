# Generated by Django 4.0.3 on 2022-11-19 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='articles',
            old_name='fill_text',
            new_name='full_text',
        ),
    ]
