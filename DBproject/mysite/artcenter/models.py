from django.db import models
from datetime import date, timedelta
from django.utils import timezone

class Program (models.Model):
    # need a foreignkey of type
    title = models.CharField(max_length = 200)

    MUSIC = 'Music'
    SPEECH = 'Speech'
    PHOTO = 'Photo'
    DRAMA = 'Drama'

    TYPE_OF_PROGRAM = (
        (MUSIC, 'Music'),
        (SPEECH, 'Speech'),
        (PHOTO, 'Photo'),
        (DRAMA, 'Drama'),
    )

    program_type = models.CharField(
        max_length = 200,
        choices = TYPE_OF_PROGRAM,
        default = MUSIC,
    )

    cost = models.IntegerField(default = 0,blank=True)
    audience_number = models.IntegerField(default = 0, blank=True)
    program_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.title

class Time_of_program (models.Model):
    program = models.ForeignKey(Program, on_delete = models.CASCADE)
    date = models.DateField(default=date.today)
    start_time = models.TimeField(default = timezone.now)
    duration = models.DurationField(default =timedelta (hours =1))

    def __str__(self):
        return self.program.title

class Employee (models.Model):
    name = models.CharField(max_length = 200)
    age = models.IntegerField(default = 0)

    FEMALE = 'female'
    MALE = 'male'
    OTHERS = 'others'

    TYPE_OF_GENDER = (
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHERS, 'Others'),
    )
    gender = models.CharField(
        max_length = 200,
        choices = TYPE_OF_GENDER,
        default = OTHERS,
    )
    start_date = models.DateField(default = date.today)

    employee_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class Job (models.Model):
    MANAGER = "Manager"
    RECEPTIONIST = "Receptionist"
    TECH = "Technician"
    PHOTOGRAPHER = "Photographer"
    ASSISTENCE = "Assistence"

    TYPE_OF_JOB = (
        (MANAGER, 'Manager'),
        (RECEPTIONIST, 'Receptionist'),
        (TECH, 'Technician'),
        (PHOTOGRAPHER, 'Photographer'),
        (ASSISTENCE, 'Assistence'),
    )

    job_type = models.CharField(
        max_length = 200,
        choices = TYPE_OF_JOB,
        default = ASSISTENCE,
        primary_key=True
    )

    work = models.TextField(blank = False)
    salary_per_hour = models.IntegerField(default = 120)
    job_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.job_type

class Works_on(models.Model):
    program = models.ForeignKey(Program, on_delete = models.CASCADE)
    employee = models.ForeignKey (Employee , on_delete = models.CASCADE)
    job_type = models.ForeignKey(Job, on_delete = models.CASCADE)

    working_hours = models.DurationField(default =timedelta (hours =1),blank=True)

    def __str__ (self):
        message = self.employee.name + " works on " + self.program.title
        return message

class Equipment(models.Model):
    equipment_type = models.CharField(max_length = 200)
    model = models.CharField (max_length=200,blank = True)
    buying_date = models.DateField(default = date.today,blank = True)
    condition = models.TextField(blank = True)
    equipment_photo = models.ImageField(blank=True)

    def __str__ (self):
        return self.equipment_type +" " +self.model

class Ticket(models.Model):
    program = models.ForeignKey(Program, on_delete = models.CASCADE)

    NORMAL =  "Normal"
    STUDENT = "Student"
    DISCOUNT = "Discount"

    TYPE_OF_TICKET = (
        (NORMAL, 'Normal'),
        (STUDENT, 'Student'),
        (DISCOUNT, 'Discount'),
    )
    ticket_type = models.CharField (
        max_length = 200,
        choices = TYPE_OF_TICKET,
        default = NORMAL,
    )
    price = models.IntegerField (default = 0)
    amount = models.IntegerField (default = 0,blank = True)

    class Meta:
         unique_together = ('program' , 'ticket_type')

    def __str__(self):
        message = self.program.title + " "+ self.ticket_type
        return message

class Use (models.Model):
    program = models.ForeignKey(Program, on_delete = models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete = models.CASCADE)

    def __str__(self):
        message = self.program.title + " use "+ self.equipment.equipment_type + " " + self.equipment.model
        return message

class Questionnaire(models.Model):
    program = models.ForeignKey(Program, on_delete = models.CASCADE)
    #!!!!!!!!!!!!
    #question_id = models.id
    audience_name = models.CharField (max_length = 40)
    audience_email = models.EmailField (max_length = 100,blank = True)
    comment = models.CharField (max_length = 800,blank = True)

    ONE =  "1"
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"

    TYPE_OF_Rating= (
        (ONE, 'One'),
        (TWO, 'Two'),
        (THREE, 'Three'),
        (FOUR,'Four'),
        (FIVE, 'Five'),
    )

    rating = models.CharField (
        max_length = 200,
        choices = TYPE_OF_Rating,
        default = THREE,
    )

    #class Meta:
    #   unique_together = ('program' , 'question_id')

    def __str__(self):
        #message = program + " "+ question_id
        return self.program.title

class Performer(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200,blank = True)
    phone_number = models.IntegerField(default = 0,blank = True)

    def __str__(self):
        return self.name

class Perform(models.Model):
    performer = models.ForeignKey(Performer, on_delete = models.CASCADE)
    program = models.ForeignKey(Program, on_delete = models.CASCADE)

    def __str__(self):
        message = self.performer.name + " performs " + self.program.title
        return message


class Manager(models.Model):
    employee = models.ForeignKey (Employee, on_delete = models.CASCADE)

    MUSIC = 'Music'
    SPEECH = 'Speech'
    PHOTO = 'Photo'
    DRAMA = 'Drama'

    TYPE_OF_PROGRAM = (
        (MUSIC, 'Music'),
        (SPEECH, 'Speech'),
        (PHOTO, 'Photo'),
        (DRAMA, 'Drama'),
    )

    program_type = models.CharField(
        max_length = 200,
        choices = TYPE_OF_PROGRAM,
        default = MUSIC,
    )

    salary_per_month = models.IntegerField(default = 0,blank = True)

    class Meta:
        unique_together = ('employee', 'program_type')

    def __str__(self):
        return self.employee.name

class Do(models.Model):
    employee = models.ForeignKey (Employee, on_delete = models.CASCADE)
    job = models.ForeignKey (Job, on_delete = models.CASCADE)

    def __str__(self):
        message = self.employee.name + " do " + self.job.job_type
        return message
