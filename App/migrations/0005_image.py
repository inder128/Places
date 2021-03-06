# Generated by Django 3.1.6 on 2021-02-04 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_delete_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('place', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='App.place')),
            ],
        ),
    ]
