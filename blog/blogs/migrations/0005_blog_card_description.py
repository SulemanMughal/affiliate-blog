# Generated by Django 2.2.4 on 2021-06-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_popularblogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='card_description',
            field=models.TextField(default="<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled i</p>"),
            preserve_default=False,
        ),
    ]
