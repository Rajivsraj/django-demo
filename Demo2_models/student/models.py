from django.db import models


# Create your models here.
class Student(models.Model):
        computerBasic = 'CB'
        software = 'SW'
        Hardware = 'HW'
        MultiMedia = 'MM'
        webDesign = 'WD'

        YEAR_IN_SCHOOL_CHOICES = [
                (computerBasic, 'Computer Basic'),
                (software, 'Software'),
                (Hardware, 'Hardware Course'),
                (MultiMedia, 'Graphic Design'),
                (webDesign, 'Web Design & Development'),
        ]

        name = models.CharField(max_length=50, blank=True)
        city = models.CharField(max_length=30)
        fees = models.IntegerField()
        article = models.TextField()
        course = models.CharField(max_length=2, default=computerBasic, choices=YEAR_IN_SCHOOL_CHOICES)
        email = models.EmailField(max_length=60, unique=True, null=True, error_messages={
                "unique": "This Email ID Already Exists",
                "blank": "Cant be blank"
        }, db_column="student_email")


# create table Student(name varchar(50), course enum("IT", "SOFTWARE", "HARDWARE") default "IT",)