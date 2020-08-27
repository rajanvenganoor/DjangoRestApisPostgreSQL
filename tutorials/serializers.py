from rest_framework import serializers
from tutorials.models import Tutorial, Homehead, Children, Transaction, Exphead, Expdetail, Event

class TutorialSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'name',
                  'address',
                  'mobileno',
                  'active')


class HomeheadSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Homehead
        fields = ('id',
                  'name',
                  'gender',
                  'dob',
                  'marital_stat',
                  'husband_code',
                  'children_no',
                  'job_stat',
                  'mobile_no',
                  'email_id',
                  'house_name',
                  'address',
                  'city',
                  'state',
                  'created_on',
                  'active')


class ChildrenSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Children
        fields = ('id',
                  'name',
                  'gender',
                  'dob',
                  'marital_stat',
                  'job_stat',
                  'mobile_no',
                  'email_id',
                  'house_name',
                  'address',
                  'city',
                  'state',
                  'created_on',
                  'active')


class TransactionSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Transaction
        fields = ('id',
                  'trn_no',
                  'trn_date',
                  'trn_type',
                  'trn_head',
                  'trn_amt',
                  'created_on',
                  'edited_on')
class ExpheadSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Exphead
        fields = ('id',
                  'exp_head',
                  'db_cr',
                  'created_on',
                  'edited_on')


class ExpdetailSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Expdetail
        fields = ('id',
                  'exp_head',
                  'exp_details',
                  'created_on',
                  'edited_on')

class EventSerializer ( serializers.ModelSerializer ):
    class Meta:
        model = Event
        fields = ('id',
                  'event_desc',
                  'event_venue',
                  'event_date',
                  'event_closing',
                  'created_on',
                  'edited_on')


