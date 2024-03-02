from django.db import models
from jobposting.models import JobRequirement
from registration.models import Worker

# Create your models here.
class Proposal(models.Model):
    job = models.ForeignKey(JobRequirement, on_delete = models.CASCADE , related_name = 'jobapp_job')
    worker = models.ForeignKey(Worker, on_delete = models.CASCADE , related_name = 'jobapp_worker')
    price = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length = 30, default = "applied")
