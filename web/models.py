from django.db import models
from django.forms import ModelChoiceField

class Console(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=8)
    release_year = models.IntegerField()


class Domain(models.Model):
    name = models.CharField(max_length=32)
    console_id = models.ForeignKey(
        "Console", on_delete=models.CASCADE, null=False)


class Game(models.Model):
    name = models.CharField(max_length=64)
    release_year = models.IntegerField()
    source = models.CharField(max_length=99)
    console_id = models.ForeignKey(
        "Console", on_delete=models.CASCADE, null=False)


class Cheat(models.Model):
    domain_id = models.ForeignKey(
        "Domain", on_delete=models.CASCADE, null=False)
    address = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    notes = models.TextField()
    game_id = models.ForeignKey(
        "Game", on_delete=models.CASCADE, null=False)

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        if type(obj) is Console:
            return obj.short_name
        elif type(obj) is Domain:
            return obj.console_id.short_name + ' ' + obj.name
        elif type(obj) is Game:
            return obj.name
        elif type(obj) is Cheat:
            return obj.domain_id + '/' + obj.address
        else:
            return "Object #%i" % obj.id