from django.db import models

# Create models here.
#Activity model
class Activity(models.Model):
    activity_id = models.IntegerField(primary_key=True)
    exhibit_id = models.IntegerField()
    play_id = models.IntegerField()
    act_name = models.CharField(max_length=100)
    act_desc = models.TextField()
    activity_extend = models.TextField(blank=True, null=True)
    whats_learned = models.TextField(blank=True, null=True)

#Exhibit model
class Exhibit:
    def __init__(self, exhibit_id, ex_name, ex_desc):
        self.exhibit_id = exhibit_id
        self.ex_name = ex_name
        self.ex_desc = ex_desc

    def __str__(self):
        return f"Exhibit ID: {self.exhibit_id}\nName: {self.ex_name}\nDescription: {self.ex_desc}"
# Creating instances for each exhibit
exhibits = [
    Exhibit("Art Smart", "Art Smart", "Get inspired"),
    Exhibit("Big John", "Big John", "Travel back to the Cretaceous period"),
    Exhibit("Central Bank", "Central Bank", "Master money"),
    Exhibit("Engineers' Workshop", "Engineers' Workshop", "Build and create"),
    Exhibit("Farm", "Farm", "Learn your food's origins"),
    Exhibit("Firehouse", "Firehouse", "Save the day"),
    Exhibit("Global Café", "Global Café", "Explore the world around us"),
    Exhibit("Ice Cream Parlor", "Ice Cream Parlor", "Scoop sweets"),
    Exhibit("KidsPort", "KidsPort", "Splash and explore"),
    Exhibit("Light Cloud", "Light Cloud", "Create sound and color"),
    Exhibit("Pizza Place", "Pizza Place", "Cook up something delicious"),
    Exhibit("Publix", "Publix", "Grocery shop"),
    Exhibit("St. John's Children's Hospital", "St. John's Children's Hospital", "Try healthcare roles"),
    Exhibit("Tugboat Tots", "Tugboat Tots", "Toddle and play"),
    Exhibit("Twinkle Stars Theater", "Twinkle Stars Theater", "Put on a show"),
    Exhibit("Vet Clinic", "Vet Clinic", "Care for cuddly critters"),
    Exhibit("Water's Journey", "Water's Journey", "Climb to the clouds")
]
# Printing each exhibit
for exhibit in exhibits:
    print(exhibit)
    print("=" * 30)

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