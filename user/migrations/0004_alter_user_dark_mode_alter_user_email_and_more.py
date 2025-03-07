# Generated by Django 5.1.2 on 2024-11-25 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_contact_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dark_mode',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='wallpaper',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
