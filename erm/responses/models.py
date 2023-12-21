from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Employer(models.Model):
    """Данные о потенциальном работодателе."""
    name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name='Компания',
        help_text='Укажите название компании-работодателя',
    )
    website = models.URLField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Сайт',
        help_text='Введите название сайта',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'

    def __str__(self):
        return f'{self.name}'


class Agency(models.Model):
    """Данные о кадровом агентстве."""
    name = models.CharField(
        unique=True,
        max_length=100,
        verbose_name='Агентство',
        help_text='Укажите название кадрового агентства',
    )
    website = models.URLField(
        unique=True,
        blank=True,
        null=True,
        verbose_name='Сайт',
        help_text='Введите название сайта',
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Агентство'
        verbose_name_plural = 'Агентства'

    def __str__(self):
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
        Employer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='contacts',
        verbose_name='Компания',
        help_text=('Укажите компанию, которую представляет данное контактное '
                   'лицо'),
    )
    agency = models.ForeignKey(
        Agency,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='contacts',
        verbose_name='Агентство',
        help_text=('Укажите кадровое агентство, которое представляет данное '
                   'контактное лицо'),
    )

    class Meta:
        ordering = ['last_name', 'first_name']
        constraints = [
            models.UniqueConstraint(
                fields=['first_name',
                        'last_name',
                        'phone'],
                name='unique_person_phone',
            ),
            models.UniqueConstraint(
                fields=['first_name',
                        'last_name',
                        'email'],
                name='unique_person_email',
            ),
            models.UniqueConstraint(
                fields=['first_name',
                        'last_name',
                        'telegram'],
                name='unique_person_telegram',
            )
        ]
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

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
        Employer,
        on_delete=models.CASCADE,
        related_name='responses',
        verbose_name='Работодатель',
        help_text='Укажите компанию-работодателя',
    )
    agency = models.ForeignKey(
        Agency,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='responses',
        verbose_name='Агентство',
        help_text='Укажите кадровое агентство',
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

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        if self.agency:
            return f'{self.position} в {self.employer} через {self.agency}'
        return f'{self.position} в {self.employer}'
