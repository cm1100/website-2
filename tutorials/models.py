from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class Tutorial_Category(models.Model):
    tut_category = models.CharField(max_length=200)
    tut_summary = models.TextField()



    def __str__(self):
        return self.tut_category


class Tutorial_Series(models.Model):
    tut_series= models.CharField(max_length=200)
    tut_category = models.ForeignKey(Tutorial_Category,on_delete=models.SET_NULL,null=True)
    real_sum = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.tut_series


class Tutorial(models.Model):

    tut_title = models.CharField(max_length=200)
    tut_series = models.ForeignKey(Tutorial_Series,on_delete=models.SET_NULL,null=True)
    tut_content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.tut_title

