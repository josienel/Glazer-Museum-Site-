from django.db import models

# Create models here.
#Activity model
class Activity(models.Model):
    activity_ID = models.IntegerField(primary_key=True)
    activity_name = models.CharField(max_length=100)
    act_desc = models.TextField()
    activity_extend = models.TextField()
    whats_learned = models.TextField()

    def __str__(self):
        return self.activity_name


#Play model
class Play(models.Model):
    play_id = models.AutoField(primary_key=True)
    play_type = models.CharField(max_length=100)
    play_desc = models.TextField()
    Physical = models.TextField(blank=True, null=True)
    Social_Emotional = models.TextField(blank=True, null=True)
    Sensory = models.TextField(blank=True, null=True)
    Cognitive = models.TextField(blank=True, null=True)
    Communication = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.play_type
    


class ExhibitManager(models.Manager):
    pass

class Exhibit(models.Model):
    exhibit_id = models.IntegerField(primary_key=True)
    ex_name = models.CharField(max_length=255)
    ex_desc = models.TextField()

    objects = ExhibitManager()  # Custom manager

    def __str__(self):
        return self.ex_name
    
#Connections model
class Connection(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Connection: Activity {self.activity_id}, Play {self.play_id}, Exhibit {self.exhibit_id}"

