# Generated by Django 4.2.2 on 2023-06-18 08:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservations', '0004_alter_sonstimes_options_alter_sonstimes_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sonstimes',
            options={'ordering': ['time'], 'verbose_name': 'Sons Time', 'verbose_name_plural': 'Sons Times'},
        ),
        migrations.AlterField(
            model_name='sonstimes',
            name='holiday_price',
            field=models.DecimalField(decimal_places=0, help_text='قیمت را به <strong>تومان</strong> وارد کنید.', max_digits=10),
        ),
        migrations.AlterField(
            model_name='sonstimes',
            name='price',
            field=models.DecimalField(decimal_places=0, help_text='قیمت را به <strong>تومان</strong> وارد کنید.', max_digits=10),
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('authority', models.CharField(max_length=200)),
                ('RfID', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sons_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sons_time_reserves', to='reservations.sonstimes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reserves', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ReserveSystem_reservations',
            },
        ),
    ]
