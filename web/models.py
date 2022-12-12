from django.db import models


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
    variations = models.JSONField()
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
    flag_data = models.JSONField()
