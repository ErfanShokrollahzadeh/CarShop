# Generated by Django 4.0.2 on 2022-02-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_footer'),
    ]

    operations = [
        migrations.AddField(
            model_name='footer',
            name='url',
            field=models.CharField(default='erfan', max_length=2083),
            preserve_default=False,
        ),
    ]
