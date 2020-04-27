# Generated by Django 3.0.5 on 2020-04-27 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movimentacao',
            options={'ordering': ('datamovimentacao',), 'verbose_name': 'movimentação', 'verbose_name_plural': 'movimentações'},
        ),
        migrations.AlterField(
            model_name='movimentacao',
            name='categoria_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='movimentacao.Categoria'),
        ),
    ]
