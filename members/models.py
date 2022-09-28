from django.db import models

# Create your models here.
class Members(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

#the SQl statement created from the model is
# CREATE TABLE "members_members" (
# "id" INT NOT NULL PRIMARY KEY AUTOINCREMENT,
# "firstname" varchar(255) NOT NULL,
# "lastname" varchar(255) NOT NULL);    
