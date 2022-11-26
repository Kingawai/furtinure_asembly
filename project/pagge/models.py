from django.db import models


class Navigation(models.Model):
    title = models.CharField(max_length=150)
    href = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Main(models.Model):
    title = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Galary(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=255)
    descriotion = models.TextField(blank=True)

    def __str__(self):
        return self.title


class AdvantageBody(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.title


class introduction(models.Model):
    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.title


class contact(models.Model):
    title = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    telegram_link = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    viber_contact = models.CharField(max_length=255)

    def __str__(self):
        return self.title
