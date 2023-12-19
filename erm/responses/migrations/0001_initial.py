# Generated by Django 4.2.4 on 2023-12-19 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Agency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название кадрового агентства",
                        max_length=100,
                        unique=True,
                        verbose_name="Агенство",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True,
                        help_text="Введите название сайта",
                        null=True,
                        verbose_name="Сайт",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        help_text="Укажите имя контактного лица",
                        max_length=100,
                        verbose_name="Имя",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True,
                        help_text="Укажите фамилию контактного лица",
                        max_length=100,
                        null=True,
                        verbose_name="Фамилия",
                    ),
                ),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        help_text="Укажите должность контактного лица",
                        max_length=100,
                        null=True,
                        verbose_name="Должность",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="Укажите телефон контактного лица",
                        max_length=20,
                        null=True,
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        help_text="Укажите E-mail контактного лица",
                        max_length=254,
                        null=True,
                        verbose_name="E-mail",
                    ),
                ),
                (
                    "telegram",
                    models.CharField(
                        blank=True,
                        help_text="Укажите телеграм контактного лица",
                        max_length=100,
                        null=True,
                        verbose_name="Telegram",
                    ),
                ),
                (
                    "agency",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите кадровое агентство, которое представляет данное контактное лицо",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contacts",
                        to="responses.agency",
                        verbose_name="Агентство",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Укажите название компании-работодателя",
                        max_length=100,
                        unique=True,
                        verbose_name="Компания",
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True,
                        help_text="Введите название сайта",
                        null=True,
                        verbose_name="Сайт",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Response",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "position",
                    models.CharField(
                        help_text="Укажите вакансию",
                        max_length=100,
                        verbose_name="Вакансия",
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        help_text="Укажите ссылку на вакансию",
                        null=True,
                        verbose_name="Ссылка",
                    ),
                ),
                (
                    "cv",
                    models.FileField(
                        blank=True,
                        help_text="Приложите файл резюме",
                        null=True,
                        upload_to="",
                        verbose_name="Резюме",
                    ),
                ),
                (
                    "letter",
                    models.TextField(
                        blank=True,
                        help_text="Напишите сопроводительное письмо",
                        null=True,
                        verbose_name="Сопроводительное",
                    ),
                ),
                ("created_at", models.DateTimeField(verbose_name="Создан")),
                ("updated_at", models.DateTimeField(verbose_name="Отредактирован")),
                (
                    "notes",
                    models.TextField(
                        blank=True,
                        help_text="Оставьте любые заметки здесь",
                        null=True,
                        verbose_name="Заметки",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Accepted", "Accepted"),
                            ("Rejected", "Rejected"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "agency",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите кадровое агентство",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responses",
                        to="responses.agency",
                        verbose_name="Агентство",
                    ),
                ),
                (
                    "contacts",
                    models.ManyToManyField(
                        help_text="Укажите контакты по вакансии",
                        related_name="responses",
                        to="responses.contact",
                        verbose_name="Контакты",
                    ),
                ),
                (
                    "employer",
                    models.ForeignKey(
                        help_text="Укажите компанию-работодателя",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responses",
                        to="responses.employer",
                        verbose_name="Работодатель",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="responses",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contact",
            name="company",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите компанию, которую представляет данное контактное лицо",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="contacts",
                to="responses.employer",
                verbose_name="Компания",
            ),
        ),
    ]
