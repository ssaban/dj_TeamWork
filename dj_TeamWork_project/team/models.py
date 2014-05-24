from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Member(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)


    def __unicode__(self):
        return self.last + ' ' + self.first
    
    
    
class Proficiency(models.Model):
    
    GURU_STATUS = 4
    EXPERT_STATUS = 3
    INTERMEDIATE_STATUS= 2
    NOVICE_STATUS =1
    NA_STATUS = 0
    
    PROFICIENCY_CHOICES = (
       (GURU_STATUS, 'Guru'),
       (EXPERT_STATUS, 'Expert'),
       (INTERMEDIATE_STATUS, 'Intermediate'),
       (NOVICE_STATUS, 'Novice'),
       (NA_STATUS, 'NA')
    )
    
    c = models.IntegerField(choices=PROFICIENCY_CHOICES, default=NA_STATUS)
    cpp = models.IntegerField(choices=PROFICIENCY_CHOICES, default=NA_STATUS)
    java = models.IntegerField(choices=PROFICIENCY_CHOICES, default=NA_STATUS)
    perl = models.IntegerField(choices=PROFICIENCY_CHOICES, default=NA_STATUS)
    python = models.IntegerField(choices=PROFICIENCY_CHOICES, default=NA_STATUS)
    ruby = models.IntegerField(choices=PROFICIENCY_CHOICES, default=NA_STATUS)
    git = models.IntegerField(choices=PROFICIENCY_CHOICES, default=NA_STATUS)
    
    member = models.ForeignKey(Member)

    def __unicode__(self):
        return self.member.first
    
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
