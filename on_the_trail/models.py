from django.db import models
from login_app.models import User

class Trail(models.Model):
    trail_id = models.IntegerField()
    user = models.ForeignKey(User, related_name = "favorite_trails", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)