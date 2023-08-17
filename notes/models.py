from django.db import models

class Note(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'НОВАЯ'),
        ('IN_PROGRESS', 'В РАБОТЕ'),
        ('COMPLETED', 'ЗАВЕРШЕНА'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
