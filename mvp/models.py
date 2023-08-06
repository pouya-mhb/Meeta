from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Meeting(models.Model):
    interrupt_choices = (
        ('interruption', 'دارای تایم استراحت'),
        ('nointerruption', 'بدون وقفه')
    )
    host = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='برگزار کننده', related_name='meetings')
    attendance = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='حضار')
    subject = models.CharField(max_length=200, verbose_name='موضوع')
    date_time = models.DateTimeField(
        default=timezone.now, verbose_name='ساعت و تاریخ جلسه')
    status = models.CharField(
        max_length=100, choices=interrupt_choices, default='no-intrrupttion', verbose_name='وضعیت اتاق')

    class Meta:
        ordering = ('-date_time',)

    def __str__(self):
        return self.subject
