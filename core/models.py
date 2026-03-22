from django.db import models


class EldenCharacter(models.Model):
    """Personagens de Elden Ring"""
    name = models.CharField(max_length=100, unique=True)
    race = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)
    quote = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Personagem Elden Ring"
        verbose_name_plural = "Personagens Elden Ring"

    def __str__(self):
        return self.name


class EldenWeapon(models.Model):
    """Armas de Elden Ring"""
    name = models.CharField(max_length=100, unique=True)
    weapon_type = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    physical_attack = models.PositiveIntegerField(default=0)
    magic_attack = models.PositiveIntegerField(default=0)
    fire_attack = models.PositiveIntegerField(default=0)
    lightning_attack = models.PositiveIntegerField(default=0)
    holy_attack = models.PositiveIntegerField(default=0)
    image_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Arma Elden Ring"
        verbose_name_plural = "Armas Elden Ring"

    def __str__(self):
        return self.name


class EldenBoss(models.Model):
    """Chefes de Elden Ring"""
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    health = models.PositiveIntegerField(default=0)
    rewards = models.TextField(blank=True, help_text="Recompensas separadas por vírgula")
    image_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Chefe Elden Ring"
        verbose_name_plural = "Chefes Elden Ring"

    def __str__(self):
        return self.name

    def get_rewards_list(self):
        """Retorna lista de recompensas"""
        return [reward.strip() for reward in self.rewards.split(',') if reward.strip()]
