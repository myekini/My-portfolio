from django.db import models

# Create your models here.

class Name(models.Model):
    """ the name of the person contacting """
    text = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ string representation of name"""
        return self.text


class Email(models.Model):
    """ email address of person"""
    text = models.CharField(max_length=200)
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'emails'

    def __str__(self):
        """ string representation of email"""
        return self.text


class Message(models.Model):
    """ enquiry message of the person"""
    text = models.TextField()
    name = models.ForeignKey(Name, on_delete=models.CASCADE)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'messages'

    def __str__(self):
        """ string representation of message"""
        return self.message[:50]
