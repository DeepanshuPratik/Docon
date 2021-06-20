from django.db import models


# Model for contact storing details
class Contact(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
        
# Model for storing profile details
class UserDetails(models.Model):
    name = models.CharField(max_length=100, default=" ")
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    key = models.CharField(max_length=100, default=" ")
    profession = models.CharField(max_length=100, default="PATIENT" )
    data = models.CharField(max_length=100, default=" ")

    def __str__(self):
        return self.email

# Model for storing holding booking details
class Book(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    problem = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name+" "+self.problem

# Model for storing reports for glitch related or issues details
class Report(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name

# Model for storing booking diagnostic details
class Diagnostic(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    tests = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name