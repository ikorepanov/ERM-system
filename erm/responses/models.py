from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Company(models.Model):
    """Данные о потенциальном работодателе или кадровом агентстве."""
    name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name='Компания',
        help_text=('Укажите название компании-работодателя или кадрового '
                   'агентства'),
    )
    website = models.URLField(
        blank=True,
        null=True,
        verbose_name='Сайт',
        help_text='Введите название сайта',
    )
    is_agency = models.BooleanField(
        default=False,
        verbose_name='Агентство',
        help_text='Отметьте, если компания является кадровым агентством',
    )

    def __str__(self):
        if self.is_agency:
            return f'{self.name} (агентство)'
        return f'{self.name}'


class Contact(models.Model):
    """
    Данные о контактном лице в компании-работодателе или кадровом агентстве.
    """
    first_name = models.CharField(
        max_length=100,
        verbose_name='Имя',
        help_text='Укажите имя контактного лица',
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Фамилия',
        help_text='Укажите фамилию контактного лица',
    )
    role = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Должность',
        help_text='Укажите должность контактного лица',
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name='Телефон',
        help_text='Укажите телефон контактного лица',
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name='E-mail',
        help_text='Укажите E-mail контактного лица',
    )
    telegram = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Telegram',
        help_text='Укажите телеграм контактного лица',
    )
    company = models.ForeignKey(
        Company,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='contacts',
        verbose_name='Компания',
        help_text=('Укажите компанию, которую представляет данное контактное'
                   'лицо'),
    )

    def __str__(self):
        if self.last_name:
            return f'{self.first_name} {self.last_name}'
        return f'{self.first_name}'


class Response(models.Model):
    """Данные об откликах на те или иные вакансии."""
    user = models.ForeignKey(
        User,
        # auto_now_add=True,
        on_delete=models.CASCADE,
        related_name='responses',
        verbose_name='Автор',
    )
    employer = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='employer_responses',
        verbose_name='Работодатель',
        help_text='Укажите компанию-работодателя',
    )
    agency = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='agency_responses',
        verbose_name='Агентство',
        help_text='Укажите компанию - кадровое агентство',
    )
    position = models.CharField(
        max_length=100,
        verbose_name='Вакансия',
        help_text='Укажите вакансию',
    )
    link = models.URLField(
        blank=True,
        null=True,
        verbose_name='Ссылка',
        help_text='Укажите ссылку на вакансию',
    )
    contacts = models.ManyToManyField(
        Contact,
        # blank=True,
        # null=True,
        related_name='responses',
        verbose_name='Контакты',
        help_text='Укажите контакты по вакансии',
    )
    cv = models.FileField(
        # upload_to='cv/',
        blank=True,
        null=True,
        verbose_name='Резюме',
        help_text='Приложите файл резюме',
        )
    letter = models.TextField(
        # upload_to='covering_letters/',
        blank=True,
        null=True,
        verbose_name='Сопроводительное',
        help_text='Напишите сопроводительное письмо',
    )
    created_at = models.DateTimeField(
        # auto_now=True,
        verbose_name='Создан',
    )
    updated_at = models.DateTimeField(
        # auto_now=True,
        verbose_name='Отредактирован',
    )
    notes = models.TextField(
        blank=True,
        null=True,
        verbose_name='Заметки',
        help_text='Оставьте любые заметки здесь',
    )
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
    )

    def __str__(self):
        if self.agency:
            return f'{self.position} в {self.employer} через {self.agency}'
        return f'{self.position} в {self.employer}'


# class JobApplication(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_applied = models.DateField()
#     company_name = models.CharField(max_length=255)
#     resume = models.FileField(upload_to='resumes/')
#     cover_letter = models.TextField()

#     def __str__(self):
#         return self.company_name


# class Employer(models.Model):
#     name = models.CharField(
#         max_length=100,
#         verbose_name='Employer Name'
#     )
#     website = models.URLField(
#         null=True,  # поле может быть пустым в БД
#         blank=True,  # поле может быть пустым в форме
#         verbose_name='Employer Website',
#         help_text='Enter the employer website URL'
#     )

#     def __str__(self):
#         return self.name


# class Position(models.Model):
#     position = models.CharField(
#         max_length=100,
#         verbose_name='Position Name'
#     )

#     def __str__(self):
#         return self.position


# class EmployerContact(models.Model):
#     first_name = models.CharField(
#         max_length=100,
#         verbose_name='First Name'
#     )
#     last_name = models.CharField(
#         max_length=100,
#         verbose_name='Last Name'
#     )
#     role = models.CharField(
#         max_length=100,
#         verbose_name='Role (Position)'
#     )
#     email = models.EmailField(
#         null=True,
#         blank=True,
#         verbose_name='Email'
#     )
#     linkedin = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True,
#         verbose_name='LinkedIn Account'
#     )
#     phone = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True,
#         verbose_name='Phone'
#     )
#     company = models.ForeignKey(
#         Employer,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name='employer_contacts',
#         verbose_name='Employer'
#     )

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


# class ThirdPartyCompany(models.Model):
#     name = models.CharField(
#         max_length=100,
#         verbose_name='Company Name'
#     )
#     website = models.URLField(
#         null=True,
#         blank=True,
#         verbose_name='Company Website',
#         help_text='Enter the third-party company website URL'
#     )

#     def __str__(self):
#         return self.name


# class ThirdPartyContact(models.Model):
#     first_name = models.CharField(
#         max_length=100,
#         verbose_name='First Name'
#     )
#     last_name = models.CharField(
#         max_length=100,
#         verbose_name='Last Name'
#     )
#     role = models.CharField(
#         max_length=100,
#         verbose_name='Role (Position)'
#     )
#     email = models.EmailField(
#         null=True,
#         blank=True,
#         verbose_name='Email'
#     )
#     linkedin = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True,
#         verbose_name='LinkedIn Account'
#     )
#     phone = models.CharField(
#         max_length=100,
#         null=True,
#         blank=True,
#         verbose_name='Phone'
#     )
#     company = models.ForeignKey(
#         ThirdPartyCompany,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name='thirdpartycontact_contacts',
#         verbose_name='Third-Party Company'
#     )

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'


# class Response(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='user_responses',
#         verbose_name='User'
#     )
#     date = models.DateField(
#         auto_now_add=True,
#         verbose_name='Response Date'
#     )
#     employer = models.ForeignKey(
#         Employer,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name='employer_responses',
#         verbose_name='Employer'
#     )
#     position = models.ForeignKey(
#         Position,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name='position_responses',
#         verbose_name='Position'
#     )
#     employercontact = models.ForeignKey(
#         EmployerContact,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name='employercontact_responses',
#         verbose_name='Employer Contact'
#     )
#     thirdpartycontact = models.ForeignKey(
#         ThirdPartyContact,
#         on_delete=models.SET_NULL,
#         null=True,
#         related_name='thirdpartycontact_responses',
#         verbose_name='Third-Party Contact'
#     )
#     status = models.CharField(
#         max_length=100,
#         verbose_name='Response Status',
#         help_text='Enter or update response status'
#     )

#     def __str__(self):
#         return f'{self.position}, {self.employer}'
