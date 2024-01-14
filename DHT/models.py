from django.db import models
from django.core.mail import send_mail
from twilio.rest import Client


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

    def send_warning_sms(self):
        if self.temp is not None and self.temp > 36.0:
            account_sid = 'AC0e9c7b4c63e09d248d696d2234f47fab'
            auth_token = '90723a483c40ee9e58903ec2b957652d'
            from_phone_number = '+16468323886'
            to_phone_number = '+212641463885'  # Replace with the recipient's phone number

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f'Attention!! La température est supérieure à 36 degrés : {self.temp}°C',
                from_=from_phone_number,
                to=to_phone_number
            )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_warning_email()
        self.send_warning_sms()
