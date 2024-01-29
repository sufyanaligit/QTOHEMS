from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Assuming a simple string for phone number
    city = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    
    # Assuming you want 'email' field to be unique, but you can adjust based on your requirements
    class Meta:
        unique_together = ['email']

    def __str__(self):
        return f'{self.name} - {self.email}'

class GetQuote(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Assuming a simple string for phone number
    address = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    number_of_drawings = models.PositiveIntegerField(default=0)
    target_number_of_days = models.PositiveIntegerField(default=0)
    specification_files = models.FileField(upload_to='quote_specifications/', null=True, blank=True, help_text='Only PDF files allowed')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'
