from django.db import models
from gig.models import gig
from registration.models import User
from category.models import Category
from jobposting.models import JobRequirement

# Create your models here.
class GigProposal(models.Model):
    worker = models.ForeignKey(User,on_delete = models.CASCADE , related_name = 'worker_gigProposal')
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'usergig_Proposal')
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'gigp_roposalcategory')
    worktitle = models.TextField()
    workdescription = models.TextField()
    location = models.CharField(max_length=50)
    latitude = models.TextField()
    longitude = models.TextField()
    status = models.CharField(max_length=50, default = "applied")
    image = models.ImageField( upload_to='image/gigProposal', null = True)
    payamount = models.IntegerField(null = True)
    paymethod = models.CharField(max_length = 50, null = True)
    acceptedate = models.DateField(null = True)


class Rating(models.Model):
    rateuser = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'userratingwork')
    gigproposal = models.ForeignKey(GigProposal, on_delete = models.CASCADE, related_name = 'gig_Proposalwork', null = True)
    jobproposal = models.ForeignKey(JobRequirement, on_delete = models.CASCADE, related_name = 'job_workratingwork', null = True)
    rateduser = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'userratedwork')
    rate = models.IntegerField()
