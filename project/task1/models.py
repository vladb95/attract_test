from __future__ import unicode_literals

from django.db import models

# Create your models here.
class People(models.Model):
    class Meta:
        db_table="people"
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Document(models.Model):
    class Meta:
        db_table="document"
    education=models.CharField(max_length=255)
    people=models.ForeignKey(People)
    def __str__(self):
        return self.people.name +' has '+ self.education+' in education list'
