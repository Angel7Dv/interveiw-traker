from django.template.defaultfilters import slugify

def get_original_slug(originail_slug, Model):
    queryset = Model.objects.all().filter(slug__iexact=originail_slug).count() 
    count = 1
    slug = originail_slug
    while(queryset): 
        slug = slugify(f'{originail_slug} {str(count)}')
        count += 1
        queryset = Model.objects.all().filter(slug__iexact=slug).count() 
    return slug