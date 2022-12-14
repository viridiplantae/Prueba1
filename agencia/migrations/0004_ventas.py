# Generated by Django 4.1.3 on 2022-11-24 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agencia', '0003_inventario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_venta', models.PositiveIntegerField(null=True)),
                ('venta_valida', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cod_inventario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agencia.inventario')),
            ],
        ),
    ]
