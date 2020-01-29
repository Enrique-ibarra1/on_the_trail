from django.db import models
import re
# from datetime import datetime

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        try:
            user = User.objects.get(email = post_data['email'])
            errors['email'] = "Email is already taken"
        except:
            pass 
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "Your name must be longer than two characters"
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Your last name must be longer than two characters."
        if not EMAIL_REGEX.match(post_data['email']):
            errors['invalid_email'] = "Your email is invalid"
        if len(post_data['password']) < 8:
            errors['password'] = "Your password is too short, must be at least 8 characters"
        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Your passwords do not match"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=384)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
