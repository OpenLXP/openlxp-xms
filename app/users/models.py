from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates a new user profile
        """

        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a new superuser with given details
        """

        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Model for a user
    """

    # fields
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # flags
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # managers
    objects = UserProfileManager()

    # override
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def __str__(self):
        """
        Returns the email.
        """
        return self.email

    def save(self, *args, **kwargs):
        """
        Overrides the save method to hash the password.
        """
        super(UserProfile, self).save(*args, **kwargs)
