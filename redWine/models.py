from django.db import models
from django.db.models import Count
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

class Penalty(models.Model):
    
    to = models.ForeignKey(get_user_model(), related_name='penalties')
    giver = models.ForeignKey(get_user_model(), related_name='penaltygiver')
    amount = models.PositiveIntegerField()
    committee = models.CharField(default="dotKom", max_length=30)
    reason = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    def __unicode__(self):
        return u'%s - %s' % (self.amount, self.to)
    class Meta:
        ordering = ['-date']
        get_latest_by = 'date'


