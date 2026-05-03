from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField('image')
    github_link = models.URLField(blank=True, null=True)
    execution_link = models.URLField(blank=True, null=True)
    features = models.JSONField(blank=True, null=True, default=list)
    tech_stack = models.ManyToManyField('Technologies', blank=True)
    short_description = models.CharField(max_length=300, blank=True, null=True)
    DOMAIN_CHOICES = [
        ("Web Dev", "Web Development"),
        ("Python", "Python Development"),
        ("ML", "Machine Learning"),
        ("AI", "Artificial Intelligence"),
        ("Java", "Java Development"),
    ]
    domain = models.CharField(max_length=100, blank=True, null=True, choices=DOMAIN_CHOICES)

    def __str__(self):
        return self.title

class ProjectScreenshot(models.Model):
    name = models.CharField(max_length=200, default='Screenshot')
    project = models.ForeignKey(Project, related_name='screenshots', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return f"Screenshot for {self.project.title}"
    
class Technologies(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
