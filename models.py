import datetime
import os
from mongoengine import connect

import mongoengine_goodjson as gj
from mongoengine.fields import DateTimeField, StringField, IntField, EmailField
from mongoengine import ValidationError

#  Read key-value pairs from a .env file and set them as environment variables
# load_dotenv()
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
database_name = os.getenv("DATABASE_NAME")
host = os.getenv("DB_HOST")

# Connecting to MongoDB
host = f"mongodb+srv://{user}:{password}@{host}/{database_name}"
connect(host=host)


def not_null(name):
    if not name:
        raise ValidationError("Name can not be empty")


class DefaultAttributes:
    meta = {"allow_inheritance": True}
    creation_date = DateTimeField()
    modified_date = DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(DefaultAttributes, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.modified_date = datetime.datetime.now()
        return super(DefaultAttributes, self).save(*args, **kwargs)


class User(DefaultAttributes, gj.Document):
    name = StringField(max_length=200, required=True, validation=not_null)
    age = IntField(max_value=100, min_value=0, required=True)
    email = EmailField(required=True)
    phone = StringField(required=True)
    address = StringField()
