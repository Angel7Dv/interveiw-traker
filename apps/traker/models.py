from django.db import models
from django.template.defaultfilters import slugify
from users.models import User

# TYPES


class type_interview(models.TextChoices):
    TECHNICAL = "technical"
    CULTURAL = "cultural"


class vacant_status(models.TextChoices):
    SEND_CV = "send_cv"
    GHOSTING = "ghosting"
    NEXT_INTERVIEW = "next_interview"
    NOT_APPROVED = "not_approved"


class networking_status(models.TextChoices):
    GHOSTING = "ghosting"
    INFORMATION = "information"
    WELL_COMUNICATION = "well_comunication"


# MODELS
class Enterprise(models.Model):
    user_register = models.ForeignKey(
        User, null=True, blank=True, related_name="enterprises", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)

    web = models.URLField(null=True, blank=True)
    glassdoor_link = models.URLField(null=True, blank=True)
    summary = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    mission = models.TextField(blank=True)

    slug = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        slug = slugify(f'{self.name}')
        queryset = Enterprise.objects.all().filter(slug__iexact=slug).count()
        self.slug = slugify(f'{self.name}{queryset}')
        super(Enterprise, self).save(*args, **kwargs)


class Vacant(models.Model):
    user_register = models.ForeignKey(
        User, null=True, blank=True, related_name="vacants", on_delete=models.CASCADE)
    roll_Name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, null=True,
                             blank=True, choices=vacant_status.choices)
    enterprise = models.ForeignKey(
        Enterprise, related_name="vacante", null=True, blank=True, on_delete=models.CASCADE)
    roll_description = models.TextField(blank=True)
    my_cv = models.FileField(null=True, blank=True)
    feed_back = models.TextField(blank=True)
    strategy = models.TextField(blank=True)
    slug = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.roll_Name

    def save(self, *args, **kwargs):
        original_slug = slugify(self.roll_Name) # creacion automatica apartir del titulo

        # LOGICA PARA LAS URLS UNICAS        
        queryset = Vacant.objects.all().filter(slug__iexact=original_slug).count() 
            # "Busca si hay otro slug que conincida con el mismo original_slug"
        count = 1
        slug = original_slug
        # (queryset) si encuentra otro con este mismo slug
        while(queryset): 
            slug = original_slug + '-' + str(count)
            count += 1
            # vuelve a hacer la verificacion
            queryset = Vacant.objects.all().filter(slug__iexact=slug).count() 
        self.slug = slug
        
        super(Vacant, self).save(*args, **kwargs)


class Interview(models.Model):
    user_register = models.ForeignKey(
        User, null=True, blank=True, related_name="interviews", on_delete=models.CASCADE)
    vacant = models.ForeignKey(
        Vacant, related_name="interview", on_delete=models.CASCADE)
    day = models.DateTimeField()
    type = models.CharField(max_length=100, null=True,
                            blank=True, choices=type_interview.choices)
    preparation = models.TextField(blank=True)

    feed_back = models.TextField(blank=True)

    slug = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f'interview {self.vacant.enterprise} {self.day}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'interview{self.vacant.enterprise}{self.day}')
        super(Interview, self).save(*args, **kwargs)


class NetWorking(models.Model):
    user_register = models.ForeignKey(
        User, null=True, blank=True, related_name="networking", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    enterprise = models.ForeignKey(
        Enterprise, related_name="networking", null=True, blank=True, on_delete=models.CASCADE)


    is_interviewer = models.BooleanField(default=False)
    interviewer = models.ForeignKey(
        Interview, related_name="interviewer", null=True, blank=True, on_delete=models.CASCADE)

    state = models.CharField(max_length=100, null=True,
                             blank=True, choices=networking_status.choices)
    enterprise_opinion = models.TextField(blank=True)
    interests = models.TextField(blank=True)
    feed_back = models.TextField(blank=True)
    position = models.TextField(blank=True)

    slug = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return f'{self.enterprise} {self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.enterprise} {self.name}')
        super(NetWorking, self).save(*args, **kwargs)


class SocialNetworks(models.Model):
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    tlf = models.IntegerField(null=True, blank=True)
    mail = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'SocialNetworks {self.enterprise} {self.enterprise}'
