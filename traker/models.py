from django.db import models

# TYPES


class type_interview(models.TextChoices):
    TECHNICAL = "technical"
    CULTURAL = "cultural"


class vacant_state(models.TextChoices):
    SEND_CV = "send_cv"
    CANCELLED = "cancelled"
    NOT_APPROVED = "not_approved"
    NEXT_INTERVIEW = "next_interview"
    GHOSTING = "ghosting"


# MODELS


class Enterprise(models.Model):
    name = models.CharField(max_length=100)
    web = models.URLField(null=True, blank=True)
    glassdoor_link = models.URLField(null=True, blank=True)
    summary = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Vacant(models.Model):
    roll_Name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True,
                             blank=True, choices=vacant_state.choices)
    enterprise = models.ForeignKey(
        Enterprise, related_name="vacante", null=True, blank=True, on_delete=models.CASCADE)

    roll_description = models.TextField(blank=True)

    my_cv = models.FileField(null=True, blank=True)

    feed_back = models.TextField(blank=True)
    
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
