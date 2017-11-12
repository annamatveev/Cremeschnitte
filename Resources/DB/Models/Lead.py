from Resources.DB.Models.Activity import Activity
from Resources.DB.Models.User import User
from mongoengine import *
import datetime


class Lead(Document):
    username = StringField(required=True, max_length=200)
    activity = ListField(EmbeddedDocumentField(Activity))
    user = EmbeddedDocumentField(User)
    date_inserted = DateTimeField(default=datetime.datetime.utcnow)
    date_updated = DateTimeField(default=datetime.datetime.utcnow)
