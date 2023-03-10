# Generated by Django 4.1.1 on 2022-12-07 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_post_exam_type_alter_post_procedure_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="exam_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Examination 1", "Examination 1"),
                    ("Examination 2", "Examination 2"),
                    ("Examination 3", "Examination 3"),
                    ("Examination 4", "Examination 4"),
                    ("Examination 5", "Examination 5"),
                    ("Examination 6", "Examination 6"),
                    ("Examination 7", "Examination 7"),
                    ("Examination 8", "Examination 8"),
                    ("Examination 9", "Examination 9"),
                    ("Examination 10", "Examination 10"),
                    ("Examination 11", "Examination 11"),
                    ("Examination 12", "Examination 12"),
                    ("Examination 13", "Examination 13"),
                    ("Examination 14", "Examination 14"),
                    ("Examination 15", "Examination 15"),
                    ("Examination 16", "Examination 16"),
                    ("Examination 17", "Examination 17"),
                    ("Examination 18", "Examination 18"),
                    ("Examination 19", "Examination 19"),
                    ("Examination 20", "Examination 20"),
                ],
                max_length=100,
                null=True,
                verbose_name="Examination Type",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="procedure",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Procedure 1", "Procedure 1"),
                    ("Procedure 2", "Procedure 2"),
                    ("Procedure 3", "Procedure 3"),
                    ("Procedure 4", "Procedure 4"),
                    ("Procedure 5", "Procedure 5"),
                    ("Procedure 6", "Procedure 6"),
                    ("Procedure 7", "Procedure 7"),
                    ("Procedure 8", "Procedure 8"),
                    ("Procedure 9", "Procedure 9"),
                    ("Procedure 10", "Procedure 10"),
                ],
                max_length=100,
                null=True,
                verbose_name="Procedure",
            ),
        ),
    ]
