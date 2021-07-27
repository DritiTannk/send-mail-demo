from django.db import models


class ContactDetails(models.Model):
    email_id = models.EmailField('Email ID', null=False, blank=False)
    subject = models.TextField('Subject', max_length=100, null=False, blank=False)
    message = models.TextField('Message', max_length=250, null=False, blank=False)

    def __str__(self):
        return f'{self.pk} \t {self.email_id} \t {self.message}'
