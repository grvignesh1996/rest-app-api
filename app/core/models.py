from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UserManager(BaseUserManager):
     
     def create_user(self, email, password = None, **exrta_fields):
     	"""Creates and saves a new user"""
     	user = self.model(email=self.normalize_email(email), **exrta_fields)
     	user.set_password(password)
     	user.save(using = self._db)

     	return user

class User(AbstractBaseUser, PermissionsMixin):
	"""Custtom user model that supports using email instead of username"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=True)

	objects = UserManager()

	USERNAME_FIELD = 'email'