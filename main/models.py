from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail.to_email import To

class Contact(models.Model):
    company = models.CharField(max_length=200)
    person = models.CharField(max_length=100)
    desc = models.TextField()
    email = models.EmailField()
    number = models.CharField(max_length=15)
    status = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.company
    
    def get_absolute_url(self):
        return reverse('main:contact-detail', kwargs={'pk': self.pk})

    def save(self,*args,**kwargs):
        try:
            old = Contact.objects.get(pk = self.pk)
            if old:
                if old.status!=self.status:
                    old_status = old.status
                    new_status = self.status
                    company = self.company
                    to = self.author.email
                    message = Mail(
                    from_email='samriddhasinha@gmail.com',
                    to_emails = To(to),
                    subject='Nirmaan CSR | Status Update',
                    html_content='Status of contact '+company+' has been changed from <b>'+old_status+'</b> to <b>'+new_status+'</b>')
                    try:
                        sg = SendGridAPIClient('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')
                        response = sg.send(message)
                        print(response.status_code)
                        print(response.body)
                        print(response.headers)
                        
                    except Exception as e:
                        print(e)
        except Exception as e:
            print(e)
                    
        super(Contact,self).save(*args,**kwargs)