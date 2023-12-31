# Generated by Django 4.1.7 on 2023-04-25 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_id_amin_admin_id_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskdelivery',
            old_name='barang',
            new_name='id_barang',
        ),
        migrations.AlterField(
            model_name='taskdelivery',
            name='bukti_pod',
            field=models.ImageField(blank=True, null=True, upload_to='static/bukti_pod/'),
        ),
        migrations.AlterField(
            model_name='taskdelivery',
            name='bukti_pos',
            field=models.ImageField(blank=True, null=True, upload_to='static/bukti_pos/'),
        ),
    ]
