from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Position(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class CV(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Template(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Respond(models.Model):
    resp_date = models.DateField()
    company = models.ForeignKey(
        Company,
        null=True,
        on_delete=models.SET_NULL,
        related_name='responds',
    )
    position = models.ForeignKey(
        Position,
        null=True,
        on_delete=models.SET_NULL,
        related_name='responds',
    )
    cv = models.ForeignKey(
        CV,
        null=True,
        on_delete=models.SET_NULL,
        related_name='responds',
    )
    template = models.ForeignKey(
        Template,
        null=True,
        on_delete=models.SET_NULL,
        related_name='responds',
    )
