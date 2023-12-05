from django.contrib.auth import get_user_model
from django.db import models
import datetime

User = get_user_model()


class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_applied = models.DateField()
    company_name = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    def __str__(self):
        return self.company_name


class Employer(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Employer Name'
    )
    website = models.URLField(
        null=True,  # поле может быть пустым в БД
        blank=True,  # поле может быть пустым в форме
        verbose_name='Employer Website',
        help_text='Enter the employer website URL'
    )

    def __str__(self):
        return self.name


class Position(models.Model):
    position = models.CharField(
        max_length=100,
        verbose_name='Position Name'
    )

    def __str__(self):
        return self.position


class EmployerContact(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name'
    )
    role = models.CharField(
        max_length=100,
        verbose_name='Role (Position)'
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name='Email'
    )
    linkedin = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='LinkedIn Account'
    )
    phone = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Phone'
    )
    company = models.ForeignKey(
        Employer,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employer_contacts',
        verbose_name='Employer'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class ThirdPartyCompany(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Company Name'
    )
    website = models.URLField(
        null=True,
        blank=True,
        verbose_name='Company Website',
        help_text='Enter the third-party company website URL'
    )

    def __str__(self):
        return self.name


class ThirdPartyContact(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Last Name'
    )
    role = models.CharField(
        max_length=100,
        verbose_name='Role (Position)'
    )
    email = models.EmailField(
        null=True,
        blank=True,
        verbose_name='Email'
    )
    linkedin = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='LinkedIn Account'
    )
    phone = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Phone'
    )
    company = models.ForeignKey(
        ThirdPartyCompany,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='thirdpartycontact_contacts',
        verbose_name='Third-Party Company'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Response(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_responses',
        verbose_name='User'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Response Date'
    )
    employer = models.ForeignKey(
        Employer,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employer_responses',
        verbose_name='Employer'
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        null=True,
        related_name='position_responses',
        verbose_name='Position'
    )
    employercontact = models.ForeignKey(
        EmployerContact,
        on_delete=models.SET_NULL,
        null=True,
        related_name='employercontact_responses',
        verbose_name='Employer Contact'
    )
    thirdpartycontact = models.ForeignKey(
        ThirdPartyContact,
        on_delete=models.SET_NULL,
        null=True,
        related_name='thirdpartycontact_responses',
        verbose_name='Third-Party Contact'
    )
    status = models.CharField(
        max_length=100,
        verbose_name='Response Status',
        help_text='Enter or update response status'
    )

    def __str__(self):
        return f'{self.position}, {self.employer}'
