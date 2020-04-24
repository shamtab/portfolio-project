from django.db import models

# Create A blog models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add blog app to the settings

# Create a migration

# Migrate

# Add to the admin
