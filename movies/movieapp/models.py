from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Film(models.Model):
    name=models.CharField(max_length=50)
    starring=models.CharField(max_length=50)
    langauge=models.CharField(max_length=20)
    release_year=models.IntegerField()
    
    def __str__(self):
        return self.name
    


class Review(models.Model):
    date=models.DateField(null=True,auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    film=models.ForeignKey(Film,on_delete=models.CASCADE)
    review=models.CharField(max_length=50)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    class Meta:
        unique_together=('user','film')
