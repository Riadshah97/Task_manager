from django.db import models
#from django.utils import timezone

"""
class PriorityChoices(models.TextChoices):
    LOW = 'LOW'
    MEDIUM = 'MEDIUM'
    HIGH = 'HIGH'

class TaskStatus(models.TextChoices):
    INCOMPLETE = 'INCOMPLETE'
    COMPLETED = 'COMPLETED'
"""
PRIORITY=(
    ('Select','Select'),
    ('Low','Low'),
    ('Medium','Medium'),
    ('High','High')
    
)

TaskStatus=(
    ('Select','Select'),
    ('incomolete','incomolete'),
    ('comolete','comolete')
    
)

class TaskImage(models.Model):
    #p_k=models.AutoField(primary_key=True)
    size = models.CharField(max_length=255, null=True, blank= True)
    image = models.ImageField(upload_to='task-images/')

    def __str__(self):
        return str('self.size')
    

    


# Create your models here.
class Task(models.Model):
    #p_k=models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=True, blank= True)
    description= models.TextField(null=True, blank= True)
    due_date = models.DateField()
    priority = models.CharField(max_length=1000, choices=PRIORITY, default='Select')
    status = models.CharField(max_length=1000, choices=TaskStatus, default='Select')
    image = models.ManyToManyField(TaskImage, blank= True)

    def __str__(self):
        return self.title



    
