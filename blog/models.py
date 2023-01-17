from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    #title = models.CharField(max_length=100)
    #content = models.TextField()
    #date_posted = models.DateTimeField(default=timezone.now)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    last_name = models.CharField('Last Name', max_length=100, blank= True, null = True)
    first_name = models.CharField('First Name', max_length=100, blank= True, null = True)
    middle_name = models.CharField('Middle Name', max_length=100, blank= True, null = True)

    sex_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    sex = models.CharField('Sex', max_length=100, choices = sex_choices, blank= True, null = True)

    date_of_birth = models.DateField('Date of Birth', auto_now_add = False, auto_now = False, blank = True, null = True)
    
    email_address = models.EmailField ('Email Address', blank= True, null = True)
    contact_number = models.CharField('Contact Number', blank= True, null = True, max_length=12)
    requesting_physician = models.CharField('Requesting Physician', max_length=100, blank= True, null = True)

    site_choices = (
        ('Hospital A', 'Hospital A'),
        ('Hospital B', 'Hospital B'),
        ('Hospital C', 'Hospital C'),
    )
    hospital_site = models.CharField('Select site', max_length=100, choices = site_choices, blank= True, null = True)
    preferred_date = models.DateField('Preferred Date', auto_now_add = False, auto_now = False, blank = True, null = True)

    
    exam_type_choices = (
        ('Computed Radiography', 'Computed Radiography'),
        ('Ultrasound', 'Ultrasound'),
        ('Magnetic Resonance Imaging', 'Magnetic Resonance Imaging'),
        ('Computerized Tomography', 'Computerized Tomography'),
    )
    exam_type = models.CharField('Examination Type', max_length=100, blank= True, null = True, choices = exam_type_choices)


    procedure_choices = (
        ('Procedure 1', 'Procedure 1'),
        ('Procedure 2', 'Procedure 2'),
    )
    procedure = models.CharField('Procedure', max_length=100, choices = procedure_choices, blank= True, null = True)

    doctors_request = models.TextField('Link of doctors request', default = '', blank= True, null = True)
    radiologist_name = models.CharField('Radiologist', max_length=100, blank= True, null = True)
    radtech_name = models.CharField('Radiologic Technologist', max_length=100, blank= True, null = True)

    status_choices = (
        ('Booked', 'Booked'),
        ('Confirmed', 'Confirmed'),
        ('Served', 'Served'),
    )
   
    status = models.CharField('Status', default='Booked', max_length=100, choices = status_choices, blank= True, null = True)
    
    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
            return reverse('post-detail', kwargs = {'pk': self.pk})