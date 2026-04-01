from django.db import models

class Edition(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    place = models.CharField(max_length=50)
    date = models.DateField()
    portrait = models.ImageField(
        upload_to='editions/portraits/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} - {self.date.year}"