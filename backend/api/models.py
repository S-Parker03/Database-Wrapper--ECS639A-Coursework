from django.db import models
from django.urls import reverse


class Technology(models.Model):
    """Model for technology used in projects"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    description = models.TextField()
    version = models.IntegerField()

    def __str__(self):
        """String representation of the model id"""
        return str(self.id)

    def as_dict(self):
        """Return the model as a dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'version': self.version,
            'api': reverse('technology api', args=[self.id]),
        }

    def get_id(self):
        """Return the model id"""
        return self.id


class Project(models.Model):
    """Model for projects"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    type = models.CharField(max_length=64)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, through="Uses")
    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """String representation of the model id"""
        return self.id

    def get_id(self):
        """Return the model id"""
        return self.id

    def as_dict(self):
        """Return the model as a dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'api': reverse('project api', args=[self.id]),
            'type': self.type,
            'description': self.description,
            'date': self.date,
            'completed': self.completed,
            'technologies': [technology.as_dict() for technology in
                             self.technologies.all()]
        }


class Uses(models.Model):
    """Model for the relationship between projects and technologies"""
    id = models.AutoField(primary_key=True)
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the model id"""
        return str(self.id)

    def as_dict(self):
        """Return the model as a dictionary"""
        return {
            'id': self.id,
            'api': reverse('project api', args=[self.id]),
            'technology': self.technology.get_id(),
            'project': self.project.get_id(),
        }
