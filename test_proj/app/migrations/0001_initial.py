# Generated by Django 4.2.4 on 2023-08-13 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('video_url', models.URLField(verbose_name='УРЛ видео')),
                ('shows_number', models.IntegerField(default=0, verbose_name='Количество показов')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название страницы')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='Идентификатор')),
                ('position', models.IntegerField(verbose_name='Порядок')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='PageBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Порядок')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.block', verbose_name='Блок')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.page', verbose_name='Страница')),
            ],
        ),
    ]
