from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from ..loginreg.models import User
import datetime

# Create your models here.

class itemManager(models.Manager):
    def itemvalidate(self, data):
        errors = []
        if data['item.name'] == '':
            errors.append("Please enter an item")
        return errors
    def createitem (self, data, user):
        self.create(name=data['item.name'], users=User.objects.get(id=user))
    def join (self, trip_id, user_id):
        self.get(id=trip_id).join.add(user_id)
    def delete (self, trip_id, user_id):
        self.get(id=trip_id).join.remove(user_id)
class item(models.Model):
    name = models.CharField(max_length = 30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    join = models.ManyToManyField(User, related_name="Users")
    users = models.ForeignKey(User)
    objects=itemManager()
