# Generated by Django 4.1.1 on 2022-12-14 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_remove_post_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="exam_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Computed Radiography", "Computed Radiography"),
                    ("Ultrasound", "Ultrasound"),
                    ("Magnetic Resonance Imaging", "Magnetic Resonance Imaging"),
                    ("Computerized Tomography", "Computerized Tomography"),
                ],
                max_length=100,
                null=True,
                verbose_name="Examination Type",
            ),
        ),
    ]
