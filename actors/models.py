from django.db import models


NATIONALITY_CHOICES = (
    ('USA', 'American'),
    ('ENGLAND', 'British'),
    ('CANADA', 'Canadian'),
    ('FRANCE', 'French'),
    ('GERMANY', 'German'),
    ('INDIA', 'Indian'),
    ('JAPAN', 'Japanese'),
    ('BRAZIL', 'Brazilian'),
    ('CHINA', 'Chinese'),
    ('ITALY', 'Italian'),
    ('SPAIN', 'Spanish'),
    ('RUSSIA', 'Russian'),
    ('MEXICO', 'Mexican'),
    ('KOREA', 'Korean'),
    ('AUSTRALIA', 'Australian'),
    ('AFRICA', 'African'),
    ('ARGENTINA', 'Argentinian'),
    ('OTHER', 'Other'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, 
                                    choices=NATIONALITY_CHOICES, 
                                    null=True,
                                    blank=True)

