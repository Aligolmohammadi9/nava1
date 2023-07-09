from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Coach(models.Model):
    full_name = models.CharField(max_length=64)
    
    
    def __str__(self):
        return f"{self.full_name}"
    

class Class(models.Model):
    name = models.CharField(max_length=64)
    level = models.CharField(max_length=64)
    teacher = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='teacher')
    capacity = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=1)
    
    def __str__(self):
        return f"{self.name} | سطح کلاس: {self.level} | مربی: {str(self.teacher.full_name)}"

    @property
    def current_capacity(self):
        registered_users = UserModel.objects.filter(course=self)
        return registered_users.count()


marital_choices = (("1","ترجیح میدهم اعلام نکنم" ), ("2", "مجرد"), ("3","متاهل"))  
pragnancy_choices = (("1", "باردار نیستم"), ("2", "باردارم"))  
orientation_choices = (("1", "سایت"), ("2", "اینستاگرام"), ("3", "تلگرام"), ("4", "واتساپ"), 
                       ("5", "مربیان"), ("6", "مسئولین موسسه"), ("7", "دوره پاکسازی درون"), ("8", "دوستان و آشنایان"))  
    
class UserModel(models.Model):
    full_name = models.CharField(max_length=64)
    email=models.EmailField(max_length=128)
    national_code = models.CharField(max_length=10)
    age = models.CharField(max_length=2)
    marital_status = models.CharField(max_length=10, choices=marital_choices, blank=True,null=True)
    whatsapp_number = models.CharField(max_length=11)
    cellphone_number = models.CharField(max_length=11,blank=True,null=True)
    phone_number = models.CharField(max_length=11,blank=True,null=True)
    emergency_phone_number = models.CharField(max_length=11)
    pragnancy = models.CharField(max_length=20 ,choices= pragnancy_choices)
    taking_medication = models.BooleanField(blank=True,null=True)
    list_of_medication = models.CharField(max_length=250,blank=True,null=True)
    disease_background = models.CharField(max_length=256, blank=True, null=True)
    disease_discribtion = models.CharField(max_length=256,blank=True, null=True )
    orientation = models.CharField(max_length=20, choices= orientation_choices)
    course = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name=("Course"))
    course_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name=("Course Price"))
    deposit_amount = models.DecimalField(max_digits=8, decimal_places=0)
    issue_tracking = models.DecimalField(max_digits=6, decimal_places=0)
    last_four_digits = models.DecimalField(max_digits=4, decimal_places=0)
    deposit_date = models.DateField()
    any_discribtion = models.CharField(max_length=250, blank=True, null=True)
    
    def clean(self):
        super().clean()
        if self.course.current_capacity >= self.course.capacity:
            raise ValidationError(f"{self.course} is already full.")

