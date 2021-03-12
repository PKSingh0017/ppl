from django.db import models

# Create your models here.
YEAR_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Pre-Final'),
    ('4', 'Final'),
    ('5', 'Alumni'),
]

ROLE_CHOICES = [
    ('Bowler', 'Bowler'),
    ('Batsman', 'Batsman'),
    ('Allrounder', 'Allrounder'),
    ('Keeper', 'Keeper'),
]

BLOCK_CHOICES = [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
]

class Player(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    whatsapp_no = models.CharField(max_length=15)
    year = models.CharField(choices=YEAR_CHOICES, max_length=6)
    branch = models.CharField(max_length=100)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)
    block = models.CharField(choices=BLOCK_CHOICES, max_length=6)
    room_number = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, max_length=100)
    profile_image = models.ImageField(upload_to='player_profile_pic', default='default.jpg')

    def __str__(self):
        return self.firstname
