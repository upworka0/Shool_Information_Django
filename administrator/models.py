from django.db import models
from django.contrib.auth.models import User
from datetime import date
from PIL import Image
from django.urls import reverse
from django.utils import timezone
import os

# Create your models here.
GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
)
class Term(models.Model):
	title = models.CharField(max_length=25)
	start_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return self.title

	class Meta:
		get_latest_by = "-start_date"

class Section(models.Model):
	GRADE_CHOICES = (
		('0', 'Kinder'),
		('1', 'I'),
		('2', 'II'),
		('3', 'III'),
		('4', 'IV'),
		('5', 'V'),
		('6', 'VI'),
	)
	class Meta:
		unique_together = ("grade_level", "name", "term")

	grade_level = models.CharField(choices=GRADE_CHOICES, max_length=1)
	name = models.CharField(max_length=25)
	term = models.ForeignKey(Term, on_delete=models.CASCADE)

	def __str__(self):
		return f'{ self.get_grade_level_display() } - { self.name }'

class Student(models.Model):
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	middle_name = models.CharField(max_length=25, default=None, blank=True, null=True)

	lrn = models.CharField(max_length = 12, unique=True, null=True, blank=True, verbose_name='Learner Reference Number')
	section = models.ForeignKey(Section, on_delete=models.CASCADE)
	sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
	birthdate = models.DateField()

	home_address = models.TextField(null=True, blank=True)
	guardian_name = models.CharField(max_length=140, null=True, blank=True)
	contact_number = models.CharField(max_length=13, null=True, blank=True)
	remarks = models.CharField(max_length=70, null=True, blank=True)

	def calculate_age(self):
		today = date.today()
		return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

	def get_absolute_url(self):
		return reverse('student-update', kwargs={'pk': self.pk})

	def __str__(self):
		return f'{self.last_name}, {self.first_name} {self.middle_name}'

class Staff(models.Model):
	STATUS_CHOICES = (
	('SG', 'Single'),
	('M', 'Married'),
	('D', 'Divorced'),
	('SE', 'Separated'),
	('W', 'Widowed'),
	)

	school_id = models.CharField(verbose_name='Employee ID', max_length=9, help_text="Please follow the following format: 12-345678")
	image = models.ImageField(default='staff/img/default.jpg', upload_to='staff/img')
	first_name = models.CharField(max_length=25)
	last_name = models.CharField(max_length=25)
	middle_name = models.CharField(blank=True, null=True, max_length=25)

	email_address = models.EmailField()
	contact_number = models.CharField(max_length=13)

	birthdate = models.DateField()
	sex = models.CharField(max_length=2, choices=GENDER_CHOICES)
	civil_status = models.CharField(max_length=9, choices=STATUS_CHOICES)

	position = models.CharField(max_length=100)
	salary = models.PositiveIntegerField()
	advisory_section = models.OneToOneField(Section, on_delete=models.CASCADE, null=True, blank=True)

	appointment_file = models.FileField(blank=True, null=True, upload_to='staff/appointment')
	pds_file = models.FileField(blank=True, null=True, upload_to='staff/pds', verbose_name='Personal Data Sheet')
	prc_license_file = models.FileField(blank=True, null=True, upload_to='staff/prc_license', verbose_name= 'PRC License Copy')
	saln_file = models.FileField(blank=True, null=True, upload_to='staff/saln_file', verbose_name='SALN Form')

	def calculate_age(self):
		today = date.today()
		return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 200 or img.width > 200:
			output_size = (200, 200)
			img.thumbnail(output_size)
			img.save(self.image.path)

	def get_absolute_url(self):
		return reverse('staff-detail', kwargs={'pk': self.pk})

class Post(models.Model):
	title = models.CharField(max_length = 140)
	desc = models.TextField(verbose_name='Description')
	image = models.ImageField(upload_to='gallery/%Y/%m/%d')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('post-update', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

class Report(models.Model):
	title = models.CharField(max_length = 50)
	remarks = models.CharField(max_length= 30, blank=True, null=True)
	file = models.FileField(upload_to='reports/%Y/%m/%d')
	month_year = models.DateField(default=timezone.now)
	date_uploaded = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title} - {self.month_year.strftime("%B %Y")}'

	def thumbnail(self):
		name, extension = os.path.splitext(self.file.name)
		if extension == '.pdf':
			return 'file-pdf text-danger'
		elif extension == '.doc' or extension == '.docx':
			return 'file-word text-info'
		elif extension == '.xls' or extension == '.xlsx':
			return 'file-excel text-success'
		elif extension == '.ppt' or extension == '.pptx':
			return 'file-powerpoint text-warning'
		elif extension == '.jpg' or extension == '.png':
			return 'file-image text-primary'
		else:
			return 'file text-muted'

	def get_absolute_url(self):
		return reverse('report-update', kwargs={'pk': self.pk})
