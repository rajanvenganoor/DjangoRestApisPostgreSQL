from django.db import models
import datetime
# from six import python_2_unicode_compatible
# from django.urls import reverse
# from tastypie.api import Api
import re


class Tutorial ( models.Model ):
    #  title = models.CharField(max_length=70, blank=False, default='')
    #  description = models.CharField(max_length=200, blank=False, default='')
    #  published = models.BooleanField(default=False)
    name = models.CharField ( max_length=70, blank=False, default='' )
    address = models.CharField ( max_length=200, blank=False, default='' )
    mobileno = models.CharField ( max_length=20, blank=False, default='' )
    active = models.BooleanField ( default=False )


def __str__(self):
    return '%s %s' % (self.name, self.address)


class Homehead ( models.Model ):
    name = models.CharField ( max_length=70, blank=False, default='' )
    gender = models.CharField ( max_length=1, default='F' )
    dob = models.DateField ( null=True, blank=True )
    marital_stat = models.CharField ( max_length=1, blank=False, default='S' )
    husband_code = models.CharField ( max_length=2, blank=False, default=' ' )
    children_no = models.CharField ( max_length=2, blank=False, default='0' )
    job_stat = models.CharField ( max_length=1, blank=False, default='S' )
    mobile_no = models.CharField ( max_length=15, blank=False, default='' )
    email_id = models.CharField ( max_length=100, blank=False, default='' )
    house_name = models.CharField ( max_length=100, blank=False, default='' )
    address = models.CharField ( max_length=200, blank=False, default='' )
    city = models.CharField ( max_length=100, blank=False, default='' )
    state = models.CharField ( max_length=200, blank=False, default='' )
    created_on = models.DateTimeField ( auto_now=True )
    active = models.BooleanField ( default=False )


def __str__(self):
    return '%s %s' % (self.name, self.gender)


class Children ( models.Model ):
    name = models.CharField ( max_length=70, blank=False, default='' )
    gender = models.CharField ( max_length=1, default='F' )
    dob = models.DateField ( null=True, blank=True )
    marital_stat = models.CharField ( max_length=1, blank=False, default='S' )
    job_stat = models.CharField ( max_length=1, blank=False, default='S' )
    mobile_no = models.CharField ( max_length=15, blank=False, default='' )
    email_id = models.CharField ( max_length=100, blank=False, default='' )
    house_name = models.CharField ( max_length=100, blank=False, default='' )
    address = models.CharField ( max_length=200, blank=False, default='' )
    city = models.CharField ( max_length=100, blank=False, default='' )
    state = models.CharField ( max_length=200, blank=False, default='' )
    created_on = models.DateTimeField ( auto_now=True )
    active = models.BooleanField ( default=False )


def __str__(self):
    return '%s %s' % (self.name, self.gender)


class Transaction ( models.Model ):
    trn_no = models.CharField ( max_length=70, blank=False, default='' )
    trn_date = models.DateField ( null=False, auto_now=True )
    trn_type = models.CharField ( max_length=2, blank=False, default='DB' )
    trn_head = models.IntegerField ( blank=False, default=0 )
    trn_amt = models.FloatField ( blank=True, default=0.0 )
    created_on = models.DateTimeField ( auto_now=True )
    edited_on = models.DateTimeField ( null=True, blank=True )


def __str__(self):
    return '%s %s' % (self.trn_type)


class Exphead ( models.Model ):
    fields = ('id',
              'exp_head',
              'db_cr'
              'created_on',
              'edited_on')

    exp_head = models.CharField ( max_length=70, blank=False, default='' )
    db_cr = models.CharField ( blank=True, max_length=2, default='DB' )
    created_on = models.DateTimeField ( auto_now=True, null=True )
    edited_on = models.DateTimeField ( null=True, blank=True )


def __str__(self):
    return '%s %s' % (self.exp_head)


class Expdetail ( models.Model ):
    exp_head = models.IntegerField ( blank=False, default=1 )
    exp_details = models.CharField ( max_length=200, blank=True, default='' )
    created_on = models.DateTimeField ( auto_now=True, null=True )
    edited_on = models.DateTimeField ( null=True, blank=True )


def __str__(self):
    return '%s %s' % (self.exp_details)

class Event ( models.Model ):
    event_desc = models.TextField ( max_length= 500, blank=False, default=" " )
    event_venue = models.CharField ( max_length=200, blank=True, default='' )
    event_date = models.DateField ( null=True, blank=True )
    event_closing = models.DateField ( null=True, blank=True )
    created_on = models.DateTimeField ( auto_now=True )
    edited_on = models.DateTimeField ( null=True, blank=True )
def __str__(self):
    return '%s %s' % (self.event_venue)

