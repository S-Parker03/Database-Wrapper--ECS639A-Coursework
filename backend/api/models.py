from django.db import models
from django.urls import reverse

# Create your models here.
class Technology(models.Model):  
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    description = models.TextField()
    version = models.CharField(max_length=64)

    def __str__(self):
        return str(self.id)
    
    def as_dict(self):
        return {
            'id': self.id,
            'name':self.name,
            'type':self.type,
            'description':self.description,
            'version':self.version,
            'api': reverse('technology api', args=[self.id]),
        }
        
    def get_id(self):
        return self.id


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, through="Uses")
    date = models.DateField()
    

    def __str__(self):
        return self.id
    
    def get_id(self):
        return self.id
    
    def as_dict(self):
        return {
            'id': self.id,
            'name':self.name,
            'api': reverse('project api', args=[self.id]),
            'type':self.type,
            'description':self.description,
            'date':self.date,
            'technologies':[technology.as_dict() for technology in self.technologies.all()]
        }
        
   


class Uses(models.Model):
    id = models.AutoField(primary_key=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    
    def as_dict(self):
        return {
            'id': self.id,
            'api': reverse('project api', args=[self.id]),
            'technology':self.technology.get_id(),
            'project':self.project.get_id(),
        }