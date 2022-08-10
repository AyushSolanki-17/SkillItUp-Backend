from django.db import models
from mainapp.models import User
# Create your models here.


# Domain Model
class Domain(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# SubDomain Model
class SubDomain(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Topic Model
class Topic(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    subdomain = models.ForeignKey(SubDomain, on_delete=models.CASCADE)
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Educational Institutes
class EducationalInstitute(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    subdomains = models.ManyToManyField(SubDomain, blank=True)
    students = models.ManyToManyField(User, blank=True)
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Event Model
class Event(models.Model):
    name = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    place = models.CharField(max_length=100)
    date = models.DateField()
    attendees = models.ManyToManyField(User)

    def __str__(self):
        return self.name


# TrendingTech IT
class TrendingTechIT(models.Model):
    name = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    companies = models.TextField()
    popularity = models.FloatField()
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# Profession
class Profession(models.Model):
    role = models.CharField(max_length=100)
    description = models.TextField()
    responsibilites = models.TextField()
    expected_salary = models.IntegerField()
    technologies = models.ManyToManyField(TrendingTechIT)
    img = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.role


# Courses Model
class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    certificate = models.BooleanField(default=False)
    url = models.TextField(null=True, blank=True)
    img = models.TextField(null=True, blank=True)
    technologies = models.ManyToManyField(TrendingTechIT)
    professions = models.ManyToManyField(Profession)

    def __str__(self):
        return self.name


# Reccomendation Test
class ReccomendationTest(models.Model):
    LEARNER = 0
    INTERMEDIATE = 1
    PROFICIENT = 2
    EXPERT = 3
    GRADE_CHOICES = (
        (LEARNER, 'Learner'),
        (INTERMEDIATE, 'Intermediate'),
        (PROFICIENT, 'Proficient'),
        (EXPERT, 'Expert')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate = models.CharField(max_length=200)
    data_structure = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    operating_system = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    database_management = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    computer_networks = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    cryptography = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    object_oriented_programming = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    computer_graphics = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    digital_electronics = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    engineering_mathematics = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    statistics = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    communication = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    english = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    creativity = models.SmallIntegerField(choices=GRADE_CHOICES, default=LEARNER)
    hackathon = models.BooleanField(default=False)
    hackathon_role = models.BooleanField(default=False)
    creative_critical = models.BooleanField(default=False)
    self_learning = models.BooleanField(default=False)
    management_technical = models.BooleanField(default=False)
    gaming = models.BooleanField(default=False)
    art = models.BooleanField(default=False)
    literature = models.BooleanField(default=False)
    business = models.BooleanField(default=False)
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE)
