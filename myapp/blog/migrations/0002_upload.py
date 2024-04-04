# Generated by Django 5.0.2 on 2024-04-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('pcat', models.CharField(max_length=100)),
                ('psubcat', models.CharField(max_length=100)),
                ('pprice', models.IntegerField(default=0)),
                ('pdate', models.DateField()),
                ('pimage', models.ImageField(default='', upload_to='blog/image')),
            ],
        ),
    ]