from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import csv

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
    

@receiver(post_save, sender=Activity)
def update_csv(sender, instance, created, **kwargs):
    file_path = '/Users/danny/Desktop/Django/DjangoProject/hello/csv_files/activities.csv'
    
    # Open the file in read mode to check content and then append/update accordingly
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row
        data = list(reader)

    updated_data = []
    found = False
    for row in data:
        if int(row[0]) == instance.activity_ID:
            # Update the row if the activity_ID matches
            row = [str(instance.activity_ID), instance.activity_name, instance.act_desc, instance.activity_extend, instance.whats_learned]
            found = True
        updated_data.append(row)

    if not found and created:
        # Append new entry if not found and the instance is newly created
        updated_data.append([str(instance.activity_ID), instance.activity_name, instance.act_desc, instance.activity_extend, instance.whats_learned])

    # Write updated data back to CSV including the header
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header first
        writer.writerows(updated_data)


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
    
@receiver(post_save, sender=Exhibit)
def update_exhibit_csv(sender, instance, created, **kwargs):
    file_path = '/Users/danny/Desktop/Django/DjangoProject/hello/csv_files/DBexhibits.csv'
    with open(file_path, mode='r+', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = [row for row in reader if row[0] != str(instance.exhibit_id)]
    
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
        writer.writerow([str(instance.exhibit_id), instance.ex_name, instance.ex_desc])

    
#Connections model
class Connection(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Connection: Activity {self.activity_id}, Play {self.play_id}, Exhibit {self.exhibit_id}"

