from django.db import models
from jobposting.models import JobRequirement
from registration.models import User
from django.utils import timezone

# Create your models here.
class Proposal(models.Model):
    job = models.ForeignKey(JobRequirement, on_delete = models.CASCADE , related_name = 'jobreqjob')
    worker = models.ForeignKey(User, on_delete = models.CASCADE , related_name = 'jobreqworker')
    price = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length = 30, default = "applied")
    accepted_at = models.CharField(null = True, max_length = 100)
    paymethod = models.CharField(max_length = 10, null= True)
    amountPayed = models.IntegerField(null = True)
