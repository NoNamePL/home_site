# Generated by Django 4.0.3 on 2022-03-23 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', models.TextField(blank=True, null=True)),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
    ]
