from django.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re


def validate_phone(value):  
    rule = re.compile(r'(^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$)')
    if not rule.search(value):
        raise ValidationError(
            _('%(value)s Invalid mobile number.'),
            params={'value': value})
    
class Posts(models.Model):
    post_name = models.CharField(verbose_name='Название должности', max_length=255)
    
    history = HistoricalRecords()

    def __str__(self):
        return self.post_name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'     

class Statuses(models.Model):
    name = models.CharField(verbose_name='name',max_length=50)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Projects(models.Model):
    project_name = models.CharField(verbose_name='Название проекта', max_length=255)
    
    history = HistoricalRecords()

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Executors(models.Model):
    executor_name = models.CharField(verbose_name='Имя', max_length=255)
    post_name = models.ForeignKey(Posts, related_name='Должность', on_delete=models.PROTECT, null=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=30, validators=[validate_phone])

    history = HistoricalRecords()

    def __str__(self):
        return self.executor_name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class Tasks(models.Model):
    TaskDesc = models.TextField(verbose_name='Описание задачи')
    DateStart = models.DateField(verbose_name='Дата начала работы')
    DateEnd = models.DateField(verbose_name='Дата окончания работы')
    ProjectName = models.ForeignKey(Projects, related_name='ProjectName', on_delete=models.PROTECT, null=True)
    ExecutorName = models.ForeignKey(Executors, related_name='ExecutorName', on_delete=models.PROTECT, null=True)
    StatusName = models.ForeignKey(Statuses, related_name='StatusName', on_delete=models.PROTECT, null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.TaskDesc

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

