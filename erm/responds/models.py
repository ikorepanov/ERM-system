from django.db import models


class Company(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.TextField("Описание", null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    position = models.CharField(
        "Название позиции в вакансии", max_length=200, default="SOME POSITION"
    )
    description = models.TextField("Описание", null=True, blank=True)

    def __str__(self):
        return f"{self.position}"


class CV(models.Model):
    version = models.CharField(
        "Версия резюме",
        max_length=200,
        default="SOME VERSION"
    )
    # ссылка на сохранённый где-то в БД файл резюме

    def __str__(self):
        return f"{self.version}"


class Template(models.Model):
    name = models.CharField("Шаблон резюме", max_length=200)
    # ссылка на сохранённый где-то в БД файл шаблона
    # изображение шаблона в миниатюре

    def __str__(self):
        return f"{self.name}"


class Respond(models.Model):
    resp_date = models.DateField("Дата отклика / отправки резюме")
    company = models.ForeignKey(
        Company,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responds",
        verbose_name="Компания",
    )
    position = models.ForeignKey(
        Position,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responds",
        verbose_name="Позиция",
    )
    cv = models.ForeignKey(
        CV,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responds",
        verbose_name="Версия резюме",
    )
    template = models.ForeignKey(
        Template,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responds",
        verbose_name="Шаблон резюме",
    )
    letter = models.TextField(
        "Текст сопроводительного письма", max_length=500, default="SOME STRING"
    )
