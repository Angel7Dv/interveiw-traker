from django.db import models

# TYPES


class type_interview(models.TextChoices):
    technical = "technical"
    cultural = "cultural"


class vacant_state(models.TextChoices):
    cancelled = "cancelled"
    not_approved = "not_approved"
    next_interview = "next_interview"
    ghosting = "ghosting"

# MODELS


class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    web = models.URLField(null=True, blank=True)
    glassdoor_link = models.URLField(null=True, blank=True)
    summary = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)


class Vacant(models.Model):
    state = models.CharField(max_length=100, null=True,
                             blank=True, choices=vacant_state.choices)
    enterprise = models.ForeignKey(
        Enterprise, related_name="vacante", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll = models.TextField(blank=True)
    my_cv = models.FileField(null=True, blank=True)
    feed_back = models.TextField(blank=True)
    roll = models.TextField(blank=True)

    strategy = models.TextField(blank=True)


class Interview(models.Model):
    vacant = models.ForeignKey(
        Vacant, related_name="interview", on_delete=models.CASCADE)
    day = models.DateTimeField()
    type = models.CharField(max_length=100, null=True,
                            blank=True, choices=type_interview.choices)
    preparation = models.TextField(blank=True)

    feed_back = models.TextField(blank=True)


class NetWorking(models.Model):
    name = models.CharField(max_length=100)
    enterprise = models.ForeignKey(
        Enterprise, related_name="networking", null=True, blank=True, on_delete=models.CASCADE)

    is_interviewer = models.BooleanField(default=False)
    interviewer = models.ForeignKey(
        Interview, related_name="interviewer", null=True, blank=True, on_delete=models.CASCADE)

    enterprise_opinion = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    feed_back = models.TextField(blank=True)
    position = models.TextField(blank=True)


class SocialNetworks(models.Model):
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
