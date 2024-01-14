from django.db import models
from django.core.mail import send_mail

class Dht11(models.Model):
    temp = models.FloatField(null=True)
    hum = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True, null=True)

    def send_warning_email(self):
        if self.temp is not None and self.temp > 36.0:
            subject = 'IOT, Avertissement de température'
            message = f'Attention!! La température est supérieure à 36 degrés : {self.temp}°C'
            from_email = 'ozitech.solution@gmail.com'
            recipient_list = ['oussamainfo54@gmail.com']

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_warning_email()
