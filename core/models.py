from django.db import models


class Guild(models.Model):
    name = models.CharField(max_length=100, unique=True)
    region = models.CharField(max_length=100, blank=True)
    founded_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(default=1)
    character_class = models.CharField(max_length=100, blank=True)
    guild = models.ForeignKey(Guild, related_name='characters', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Lv. {self.level})"
