# Generated by Django 4.2.9 on 2024-02-07 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0121_auto_20240207_0344'),
        ('stock', '0106_auto_20240207_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockitemtestresult',
            name='test',
        ),
        migrations.AlterField(
            model_name='stockitemtestresult',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to='part.parttesttemplate'),
        ),
    ]