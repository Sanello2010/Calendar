from django.db import models
from django.contrib.auth.models import User


class RemindTime(models.Model):
    class Meta:
        verbose_name = "Remind time"
        verbose_name_plural = "Remind times"
        db_table = "remindtime"

    remind_time = models.PositiveIntegerField()

    def __str__(self):
        return self.remind_time.__str__()


class Event(models.Model):
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        db_table = "event"

    name = models.CharField(max_length=150, blank=True, null=True)
    description_event = models.TextField(blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='event'
    )
    remind_time = models.ForeignKey(
        RemindTime, on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if self.end_time is None:
            self.end_time = self.start_time
            self.end_time = self.start_time.replace(
                hour=23,
                minute=59,
                second=59
            )
        super().save(*args, *kwargs)  # add time

    def __str__(self):
        return self.name if self.name else self.start_time.__str__()
