# Generated by Django 4.2.4 on 2023-10-03 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_try_time', models.DateTimeField(verbose_name='Дата и время последней рассылки')),
                ('status', models.CharField(max_length=20, verbose_name='Статус попытки')),
                ('mail_server_callback', models.TextField(verbose_name='Ответ почтового сервера, если он был')),
            ],
            options={
                'verbose_name': 'Лог рассылки',
                'verbose_name_plural': 'Логи рассылки',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_theme', models.CharField(max_length=150, verbose_name='Тема')),
                ('mail_body', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение для рассылки',
                'verbose_name_plural': 'Сообщения для рассылки',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('daily', 'Раз в день'), ('weekly', 'Раз в неделю'), ('monthly', 'Раз в месяц')], max_length=10, verbose_name='Периодичность')),
                ('starting_at', models.TimeField(verbose_name='время начала рассылки')),
                ('ending_at', models.TimeField(verbose_name='время окончания рассылки')),
                ('mailing_status', models.CharField(max_length=20, verbose_name='Статус рассылки')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]