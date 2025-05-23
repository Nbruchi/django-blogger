from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='theme/media/profiles',blank=True,null=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',  # Custom name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to. A user can belong to multiple groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',  # Custom name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']