from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Employer(models.Model):
    name = models.CharField('Название', max_length=100)
    website = models.URLField('Сайт', null=True, blank=True)  # null - поле может быть пустым в БД; blank - поле может быть пустым в форме.

    def __str__(self):
        return self.name


class Position(models.Model):
    position = models.CharField(
        'Название позиции в вакансии', max_length=100)

    def __str__(self):
        return self.position


class EmployerContact(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    second_name = models.CharField('Фамилия', max_length=100)
    role = models.CharField('Роль (должность)', max_length=100)
    email = models.EmailField('email', null=True, blank=True)
    linkedin = models.CharField('Аккаунт в LinkedIn', max_length=100, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=100, null=True, blank=True)
    company = models.ForeignKey('Компания', Employer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name}"


class Response(models.Model):
    resp_date = models.DateField("Дата отклика / отправки резюме")
    company = models.ForeignKey(
        Company,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responses",
        verbose_name="Компания",
    )
    position = models.ForeignKey(
        Position,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responses",
        verbose_name="Позиция",
    )
    cv = models.ForeignKey(
        CV,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responses",
        verbose_name="Версия резюме",
    )
    template = models.ForeignKey(
        Template,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responses",
        verbose_name="Шаблон резюме",
    )
    letter = models.TextField(
        "Текст сопроводительного письма", max_length=500, default="SOME STRING"
    )

    def __str__(self):
        return f"{self.position}"
