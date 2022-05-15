from django.db import models



    

    

class person(models.Model):
    
    name=models.CharField(max_length=25)
    surname=models.CharField(max_length=25)
    age=models.IntegerField()
    


    def __str__(self):

        return f"{self.name} {self.surname} "
