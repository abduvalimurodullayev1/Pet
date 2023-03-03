import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from app import models as app_models
from app import models as app_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_app_Pet(**kwargs):
    defaults = {}
    defaults["title"] = ""
    defaults["description"] = ""
    defaults["image"] = ""
    defaults["price"] = ""
    defaults.update(**kwargs)
    return app_models.Pet.objects.create(**defaults)
def create_app_Service(**kwargs):
    defaults = {}
    defaults["description"] = ""
    defaults["imege"] = ""
    defaults["service_title"] = ""
    defaults.update(**kwargs)
    return app_models.Service.objects.create(**defaults)
def create_app_Our_team(**kwargs):
    defaults = {}
    defaults["full_name"] = ""
    defaults["image"] = ""
    defaults["age"] = ""
    defaults["information"] = ""
    defaults.update(**kwargs)
    return app_models.Our_team.objects.create(**defaults)
