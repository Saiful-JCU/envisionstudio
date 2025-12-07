from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField
from shortuuid.django_fields import ShortUUIDField

# Create your models here.

# class Hero(models.Model):
    

class Message(models.Model):
    name = models.CharField(max_length = 200)
    subject = models.CharField(max_length = 500, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()

class ServiceCategory(models.Model):
    img = models.FileField(upload_to="serviceCategory/", null=True, blank=True)
    servicecategory_name = models.CharField(max_length = 100, unique = True )

    def __str__(self):
        return self.servicecategory_name

class JobData(models.Model):
    email = models.EmailField()
    service = models.CharField(max_length = 200)
    fileformat = models.CharField(max_length = 200)
    background = models.CharField(max_length = 200)
    message = models.CharField(max_length = 400)
    file = models.FileField(upload_to="uploads/job/")
    checked = models.BooleanField(default=False)


class Pricing(models.Model):
    title = models.CharField(max_length = 50)
    simple_category = models.CharField(max_length = 50)
    medium_category = models.CharField(max_length = 50, null=True, blank=True)
    complex_category = models.CharField(max_length = 50)
    super_complex = models.CharField(max_length = 50)
     

class BeforAfterImg(models.Model):
    before_img = models.FileField(upload_to = "before_after_img/")
    before_img_alt_text = models.CharField(null=True, blank=True, max_length=650)
    after_img = models.FileField(upload_to = "before_after_img/")
    after_img_alt_text = models.CharField(null=True, blank=True, max_length=450)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, blank=True, null = True)


class ServiceDetail(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    service_img = models.FileField(null=True, blank=True, upload_to="service_img/")
    ServiceCategory = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, blank=True, null = True)

    img_alt_text = models.CharField(null=True, blank=True,max_length=450)
    description = models.CharField(max_length=250)
    about_service = models.CharField(max_length=800, null=True, blank=True)
    service_features1 = models.CharField(null=True, blank=True,max_length=450)
    service_features2 = models.CharField(null=True, blank=True,max_length=455)
    service_features3 = models.CharField(null=True, blank=True,max_length=455)
    service_features4 = models.CharField(null=True, blank=True,max_length=450)
    service_features5 = models.CharField(null=True, blank=True,max_length=450)

    
    working_process_h2 = models.CharField(max_length=250)
    step_1_p = models.CharField(max_length=250)
    step_2_p = models.CharField(max_length=250)

    pricing_h2 = models.CharField(max_length=250)
    
    # Basic plan
    basic_plan = models.CharField(max_length=50)
    bli_1 = models.CharField(null=True, blank=True, max_length=100)
    bli_2 = models.CharField(null=True, blank=True, max_length=100)
    
    # Standard plan
    standard_plan = models.CharField(max_length=50)
    sli_1 = models.CharField(null=True, blank=True, max_length=100)
    sli_2 = models.CharField(null=True, blank=True, max_length=100)
    
    # Premium plan
    premium_plan = models.CharField(max_length=50)
    pli_1 = models.CharField(null=True, blank=True, max_length=100)
    pli_2 = models.CharField(null=True, blank=True, max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while ServiceDetail.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogDetailsView(models.Model):
    title = models.CharField(null = True, blank=True, max_length=300)
    slug = models.SlugField(unique=True, blank=True, null=True,  max_length=300)
    banner = models.FileField(null=True, blank=True, upload_to="blog_banner/")
    alt_text = models.CharField(null = True, blank=True, max_length=300)
    author = models.CharField(null = True, blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    description = RichTextField()

    # generate slug automatically if not manually
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + '-' + shortuuid.ShortUUID().random(length=8)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

class Staff(models.Model):
    image = models.FileField(upload_to="Staff/")
    image_alt_text = models.CharField(max_length=250)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=250)

    fb_link = models.URLField(max_length=500, null=True, blank=True, unique=True)
    twitter_link = models.URLField(max_length=500, null=True, blank=True, unique=True)
    linkedin_link = models.URLField(max_length=500, null=True, blank=True, unique=True)
    instagram_link = models.URLField(max_length=500, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name


class AdditionalImage(models.Model):
    intro_image = models.FileField(upload_to = "intro_image/")    
    intro_overlay_image = models.FileField(upload_to = "intro_image/")    








