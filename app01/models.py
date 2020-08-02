from django.db import models
import mongoengine


# Create your models here.
class Student(mongoengine.Document):
    name = mongoengine.StringField(max_length=30)
    # 0 表示男 1 表示女
    gender = mongoengine.IntField(default=0)
    age = mongoengine.IntField(default=0)
    address = mongoengine.StringField(max_length=64)
