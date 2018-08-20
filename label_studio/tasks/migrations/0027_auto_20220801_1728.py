# Generated by Django 3.2.14 on 2022-08-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0026_auto_20220725_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationdraft',
            name='was_postponed',
            field=models.BooleanField(db_index=True, default=False, help_text='User postponed this draft (clicked a forward button) in the label stream', verbose_name='was postponed'),
        ),
    ]
