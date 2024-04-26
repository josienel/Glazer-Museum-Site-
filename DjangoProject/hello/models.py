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
    file_path = 'hello/csv_files/activities.csv'
    
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
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import csv

class Play(models.Model):
    play_id = models.AutoField(primary_key=True)
    play_type = models.CharField(max_length=100)
    play_desc = models.TextField()
    physical = models.TextField(blank=True, null=True)
    social_emotional = models.TextField(blank=True, null=True)
    sensory = models.TextField(blank=True, null=True)
    cognitive = models.TextField(blank=True, null=True)
    communication = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.play_type

@receiver(post_save, sender=Play)
def update_play_csv(sender, instance, created, **kwargs):
    file_path = 'hello/csv_files/play.csv'
    try:
        with open(file_path, mode='r+', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Ensure there is a header
            existing_data = [row for row in reader if row and row[0] != str(instance.play_id)]

        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(existing_data)
            if created or not any(row[0] == str(instance.play_id) for row in existing_data):
                # Write new or updated entry
                writer.writerow([
                    str(instance.play_id),
                    instance.play_type,
                    instance.play_desc,
                    instance.physical,
                    instance.social_emotional,
                    instance.sensory,
                    instance.cognitive,
                    instance.communication
                ])
    except Exception as e:
        print(f"Failed to update play CSV for {instance.play_type} with error: {e}")


    

#Exhibit Model
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
    file_path = 'hello/csv_files/DBexhibits.csv'
    try:
        with open(file_path, mode='r+', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)  # Ensure there is a header
            existing_data = [row for row in reader if len(row) > 0 and row[0] != str(instance.exhibit_id)]
            
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(existing_data)
            if created or not any(row[0] == str(instance.exhibit_id) for row in existing_data):
                writer.writerow([str(instance.exhibit_id), instance.ex_name, instance.ex_desc])
    except Exception as e:
        print(f"Failed to update exhibit CSV for {instance.ex_name} with error: {e}")


    
#Connections model
class Connection(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)

    def __str__(self):
        return f"Connection: Activity {self.activity_id}, Play {self.play_id}, Exhibit {self.exhibit_id}"

@receiver(post_save, sender=Connection)
def update_connections_csv(sender, instance, created, **kwargs):
    file_path = 'hello/csv_files/connections.csv'
    
    # Define the header for the CSV file
    header = ['activity_id', 'play_id', 'exhibit_id']

    # Prepare the data for the current instance
    new_data = [str(instance.activity_id), str(instance.play_id), str(instance.exhibit_id)]

    # Open the file and read existing data
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        # If the file doesn't exist, create it with the header
        data = [header]

    # If the instance is newly created, append the new data
    if created:
        data.append(new_data)
    else:
        # If the instance already exists, find and update the corresponding row
        for row in data:
            if row[0] == str(instance.activity_id):
                row[:] = new_data
                break
        else:
            # If no corresponding row is found, append the new data
            data.append(new_data)

    # Write the updated data back to the CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
