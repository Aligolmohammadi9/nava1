from django import forms
from .models import UserModel, Class




class UserForm(forms.ModelForm):
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # populate the course prices for the select widget
        self.fields['course'].widget.choices = [(c.id, f"اسم کلاس: {c.name} | سطح کلاس: {c.level} | مربی: {str(c.teacher.full_name)} | مبلغ: ({c.price}ریال)") for c in Class.objects.all()]


    

    
    class Meta:
        model = UserModel
        js = ('js/index.js',)
        
        
        
        fields =(
                "full_name","email","national_code","age","marital_status","whatsapp_number",
                 "cellphone_number","phone_number","emergency_phone_number","pragnancy","taking_medication","list_of_medication","disease_background",
                 "disease_discribtion","orientation","course","course_price", "deposit_amount", "issue_tracking", "last_four_digits", "deposit_date", "any_discribtion"
        )
        
        labels ={
                "full_name":"نام کامل", "email":"پست الکتریکی", "national_code":"کد ملی", "age":"سن", "marital_status":"وضعیت تاهل",
                "whatsapp_number":"شماره واتس اپ", "cellphone_number":"شماره همراه", "phone_number":"شماره ثایت",
                "emergency_phone_number":"شماره تماس اضطراری", "pragnancy":"وضعیت بارداری",
                "taking_medication":"دارو مصرف میکنم", "list_of_medication":"لیست داروها", "disease_background":"بیماری های زمینه ای",
                "disease_discribtion":"توضیح بیماری", "orientation":"نحوه آشنایی", "course":"کلاس", "course_price":"مبلغ کلاس", "deposit_amount":"مبلغ واریزی"
                , "issue_tracking":"شماره پیگیری", "last_four_digits":"چهار رقم آخر کارت", "deposit_date":"تاریخ واریزی", "any_discribtion":"هرگونه توضیحات"
        }
        error_messages = {
            
        }
        
        
        
        widgets={
            "full_name": forms.TextInput( attrs= {'class': 'form-control'}),
            "email": forms.EmailInput(attrs= {'class': 'form-control', 'label':'پست الکترونیکی', 'placeholder':'example@gmail.com'}),
            "national_code": forms.TextInput(attrs= {'class': 'form-control', 'label':'کد ملی','min':'1000000000','max': '9999999999'}),
            "age": forms.NumberInput(attrs= {'class': 'form-control', 'label':'سن','min':'12','max': '100'}),
            "marital_status": forms.Select(attrs= {'class': 'form-control select', 'label':'وضعیت تاهل'}),
            "whatsapp_number": forms.TextInput(attrs= {'class': 'form-control', 'label':'شماره واتساپ', 'placeholder':'09*********','min':'1000000000','max': '99999999999'}),
            "cellphone_number": forms.TextInput(attrs= {'class': 'form-control', 'label':'شماره همراه', 'placeholder':'09*********','min':'1000000000','max': '99999999999'}),
            "phone_number": forms.TextInput(attrs= {'class': 'form-control', 'label':'شماره ثابت', 'placeholder':'021********','min':'1000000000','max': '9999999999'}),
            "emergency_phone_number": forms.TextInput(attrs= {'class': 'form-control', 'label':'شماره تماس اضطراری', 'placeholder':'09*********','min':'1000000000','max': '99999999999'}),
            "pragnancy": forms.Select(attrs= {'class': 'form-control select', 'label':'وضعیت بارداری'}),
            "taking_medication": forms.CheckboxInput(attrs= {'class': 'select', 'label':'دارو مصرف میکنم'}),
            "list_of_medication": forms.TextInput(attrs= {'class': 'form-control', 'label':'لیست داروها', 'disabled':True, 'requierd':False}),
            "disease_background": forms.TextInput(attrs= {'class': 'form-control', 'label':'بیماری های زمینه ای', 'requierd':False}),
            "disease_discribtion": forms.TextInput(attrs= {'class': 'form-control', 'label':'توضیح بیماری', 'requierd':False}),
            "orientation": forms.Select(attrs= {'class': 'form-control select', 'requierd':False}),
            "course": forms.Select(attrs={"class": "form-control select"}),
            "course_price": forms.HiddenInput(attrs={"class": "form-control", "readonly": True}),
            "deposit_amount": forms.NumberInput(attrs={"class":"form-control" }),
            "issue_tracking": forms.NumberInput(attrs={"class":"form-control" }),
            "last_four_digits": forms.NumberInput(attrs={"class":"form-control" }),
            "deposit_date": forms.DateInput(attrs={"class":"form-control", "type":"date" }),
            "any_discribtion": forms.TextInput( attrs= {'class': 'form-control'}),
        }
        
        


        











