from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User  # If using Django's built-in User model
# To import Time 
from django.utils import timezone

from django.contrib.auth import get_user_model


# Create your models here.

TAG_CHOICES = (  
    ('Exiting','Exiting'),
    ('Lead','Lead'),
    ('Long-term','Long-term'),
    ('Partner','Partner'),
)

INDUSTRY_TYPE = (
    ('','Select industry type'),
    ('Computer Industry','Computer Industry'),
    ('Chemical Industries','Chemical Industries'),
    ('Health Services','Health Services'),
    ('Telecommunications Services','Telecommunications Services'),
    ('Textiles: Clothing, Footwear','Textiles: Clothing, Footwear')
)

STATUS_CHOICE = (
    ('Approved','Approved'),
    ('New','New'),
    ('Pending','Pending'),
    ('Rejected','Rejected')
)

TYPE_CHOICE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

STATUS = (
    ('Pending','Pending'),
    ('Inprogress','Inprogress'),
    ('Cancelled','Cancelled'),
    ('Pickups','Pickups'),
    ('Returns','Returns'),
    ('Delivered','Delivered')
)

PAYMENT_METHOD = (
    ('Mastercard','Mastercard'),
    ('Visa','Visa'),
    ('COD','COD'),
    ('Paypal','Paypal')
)
 
PRODUCT = (
    ('Puma Tshirt','Puma Tshirt'),
    ('Adidas Sneakers','Adidas Sneakers'),
    ('350 ml Glass Grocery Container','350 ml Glass Grocery Container'),
    ('American egale outfitters Shirt','American egale outfitters Shirt'),
    ('Galaxy Watch4','Galaxy Watch4'),
    ('Apple iPhone 12','Apple iPhone 12'),
    ('Funky Prints T-shirt','Funky Prints T-shirt'),
    ('USB Flash Drive Personalized with 3D Print','USB Flash Drive Personalized with 3D Print'),
    ('Oxford Button-Down Shirt','Oxford Button-Down Shirt'),
    ('Classic Short Sleeve Shirt','Classic Short Sleeve Shirt'),
    ('Half Sleeve T-Shirts (Blue)','Half Sleeve T-Shirts (Blue)'),
    ('Noise Evolve Smartwatch','Noise Evolve Smartwatch')
)

CUSTOMER_STATUS = (
    ('Active','Active'),
    ('Block','Block')
)

TICKET_STATUS = (
    ('Closed','Closed'),
    ('Inprogress','Inprogress'),
    ('New','New'),
    ('Open','Open')
)

PRIORITY = (
    ('High','High'),
    ('Low','Low'),
    ('Medium','Medium')
)

class CrmContact(models.Model):
    profile_pic = models.ImageField(upload_to="images/contact",blank=True,null=True)
    name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    email_id = models.EmailField(max_length=150,unique=True)
    phone = models.CharField(max_length=13)
    lead_score = models.IntegerField()
    tags = MultiSelectField(max_length=50,choices=TAG_CHOICES,max_choices=3)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/users/user-dummy-img.jpg"
    
    
class CrmCompany(models.Model): 
    logo = models.ImageField(upload_to='images/company',blank=True,null=True)
    name = models.CharField(max_length=150)
    owner_name = models.CharField(max_length=50)
    industry_type = models.CharField(max_length=50,choices=INDUSTRY_TYPE)
    rating = models.CharField(max_length=10)
    location = models.CharField(max_length=150)
    employee = models.CharField(max_length=10)
    website = models.CharField(max_length=150)
    contact_email = models.EmailField(max_length=150,unique=True)
    since = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Crm Companies"
        
    def get_photo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return "/static/images/users/multi-user.jpg"
    
class CrmLead(models.Model):
    profile_pic = models.ImageField(upload_to='images/leads',blank=True,null=True)
    name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    lead_score = models.IntegerField()
    phone = models.CharField(max_length=13)
    location = models.CharField(max_length=150)
    tags = MultiSelectField(max_length=50,choices=TAG_CHOICES,max_choices=3)
    create_date = models.DateField()
    
    def get_photo_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
            return "/static/images/users/user-dummy-img.jpg"
        
class JobApplication(models.Model):
    profile_pic = models.ImageField(upload_to='images/job/application',blank=True,null=True)
    company_name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    apply_date = models.DateField()
    contact = models.CharField(max_length=13)
    status = models.CharField(max_length=15,choices=STATUS_CHOICE)
    type = models.CharField(max_length=15,choices=TYPE_CHOICE)
    
class EcommerceOrder(models.Model):
    name = models.CharField(max_length=150)
    product = models.CharField(max_length=150,choices=PRODUCT)
    order_date = models.DateTimeField()
    amount = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=50,choices=PAYMENT_METHOD)
    status = models.CharField(max_length=30,choices=STATUS)
    
class EcommerceCustomer(models.Model): 
    name = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=50,unique=True)
    phone = models.CharField(max_length=13)
    joining_date = models.DateField()
    status = models.CharField(max_length=12,choices=CUSTOMER_STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class TicketList(models.Model):
    title = models.CharField(max_length=150)
    client_name = models.CharField(max_length=100)
    assign_to = models.CharField(max_length=150)
    create_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=10,choices=TICKET_STATUS)
    priority = models.CharField(max_length=10,choices=PRIORITY)



#  companies Table
 
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=300)
    company_address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
    company_details = models.ForeignKey('Company_Details', on_delete=models.SET_NULL, null=True, blank=True)
    contact_person = models.ForeignKey('Person', on_delete=models.SET_NULL, null=True, blank=True, related_name='company_contact_person')
    projects = models.ManyToManyField('Project', related_name='companies', blank=True)
    marketers = models.ManyToManyField(User, related_name='companies',blank=True)
    contractors = models.ManyToManyField(User, related_name='company_contractors',blank=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_companies')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_companies')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_companies')
    company_website = models.URLField(max_length=200, blank=True, null=True, default=None)
    #Types of contractors  like GC
    CONTRACTOR_TYPES = (
        ('Contractor', 'Contractor'),
        ('Sub_Contractor', 'Sub Contractor'),
        ('General Contractor', 'General Contractor'),
        ('completed', 'Completed'),
    )
    contractor_type = MultiSelectField(max_length=50, choices=CONTRACTOR_TYPES, max_choices=3)
    #What company was doing in a project like as a GC orSub contractor

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.company_name
class Person(models.Model):
    person_id = models.AutoField(primary_key=True) 
    # profile_pic = models.ImageField(upload_to='profile_pics/', blank=True) 
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
    phone_no = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name
class Address(models.Model):
    location = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    region = models.CharField(max_length=50, blank=True)
    timezone = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.location

class Company_Details(models.Model):
    # type_of_construction = models.CharField(max_length=100)
    CONSTRUCTION_TYPE_CHOICES = (
        ('RESIDENTIAL', 'Residential'),
        ('COMMERCIAL', 'Commercial'),
        ('INDUSTRIAL', 'Industrial'),
    )
    type_of_construction = MultiSelectField(max_length=200,choices=CONSTRUCTION_TYPE_CHOICES,max_choices=1)
    TAG_CHOICES = (  
    ('General_Requirements', 'General Requirements'),
    ('Existing_Conditions', 'Existing Conditions'),
    ('Concrete', 'Concrete'),
    ('Masonry', 'Masonry'),
    ('Metals', 'Metals'),
    ('Wood_Plastics_and_Composites', 'Wood, Plastics, and Composites'),
    ('Thermal_and_Moisture_Protection', 'Thermal and Moisture Protection'),
    ('Openings', 'Openings'),
    ('Finishes', 'Finishes'),
    ('Specialties', 'Specialties'),
    ('Equipment', 'Equipment'),
    ('Furnishings', 'Furnishings'),
    ('Special_Construction', 'Special Construction'),
    ('Conveying_Equipment', 'Conveying Equipment'),
    ('Plumbing_HVAC', 'Plumbing + HVAC'),
    ('Electrical_Lighting', 'Electrical + Lighting'),
    ('Reserved_For_Future_Expansion_1', 'RESERVED FOR FUTURE EXPANSION'),
    ('Reserved_For_Future_Expansion_2', 'RESERVED FOR FUTURE EXPANSION'),
    ('Reserved_For_Future_Expansion_3', 'RESERVED FOR FUTURE EXPANSION'),
    ('Mechanical_Support', 'Mechanical Support'),
    ('Fire_Suppression', 'Fire Suppression'),
    ('Plumbing', 'Plumbing'),
    ('HVAC', 'Heating Ventilating and Air Conditioning'),
    ('Reserved_For_Future_Expansion_4', 'RESERVED FOR FUTURE EXPANSION'),
    ('Integrated_Automation', 'Integrated Automation'),
    ('Electrical', 'Electrical'),
    ('Communications', 'Communications'),
    ('Electronic_Safety_and_Security', 'Electronic Safety and Security'),
    ('Reserved_For_Future_Expansion_5', 'RESERVED FOR FUTURE EXPANSION'),
    ('Reserved_For_Future_Expansion_6', 'RESERVED FOR FUTURE EXPANSION'),
    ('Earthwork', 'Earthwork'),
    ('Exterior_Improvements', 'Exterior Improvements'),
    ('Utilities', 'Utilities'),
    ('Transportation', 'Transportation'),
    ('Waterways_and_Marine_Construction', 'Waterways and Marine Construction'),
    ('Reserved_For_Future_Expansion_7', 'RESERVED FOR FUTURE EXPANSION'),
    ('Reserved_For_Future_Expansion_8', 'RESERVED FOR FUTURE EXPANSION'),
    ('Reserved_For_Future_Expansion_9', 'RESERVED FOR FUTURE EXPANSION'),
    ('Reserved_For_Future_Expansion_10', 'RESERVED FOR FUTURE EXPANSION'),
    ('Process_Interconnections', 'Process Interconnections'),
    ('Material_Processing_and_Handling_Equipment', 'Material Processing and Handling Equipment'),
    ('Process_Heating_Cooling_and_Drying_Equipment', 'Process Heating, Cooling, and Drying Equipment'),
    ('Process_Gas_and_Liquid_Handling_Purification_and_Storage_Equipment', 'Process Gas and Liquid Handling, Purification and Storage Equipment'),
    ('Pollution_Control_Equipment', 'Pollution Control Equipment'),
    ('Industry-Specific_Manufacturing_Equipment', 'Industry-Specific Manufacturing Equipment'),
    ('Water_and_Wastewater_Equipment', 'Water and Wastewater Equipment'),
    ('Reserved_For_Future_Expansion_11', 'RESERVED FOR FUTURE EXPANSION'),
    ('Electrical_Power_Generation', 'Electrical Power Generation'),
    ('Reserved_For_Future_Expansion_12', 'RESERVED FOR FUTURE EXPANSION'),
)

    csi_division = MultiSelectField(max_length=200,choices=TAG_CHOICES,max_choices=50)
    year_founded = models.IntegerField(null=True, blank=True)
    size = models.CharField(max_length=100)
    equipment_and_resources = models.TextField()
    insurance_information = models.TextField()
    financial_information = models.TextField()
    notes_and_comments = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return ', '.join(self.get_type_of_construction_display())
    


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    project_specification_files = models.ManyToManyField('ProjectSpecifications', blank=True, related_name='projects')
    project_address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    # will be using state column for Description
    state = models.CharField(max_length=50,blank=True)
    # will use city for project address 
    city = models.CharField(max_length=50,blank=True)
    STATUS_CHOICES = (
        ('Started', 'Started'),
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('Closed', 'Closed'),
    )
    status = MultiSelectField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    addendum_files = models.FileField(upload_to='project_addendum/', null=True, blank=True)
    project_files = models.FileField(upload_to='project_files/', null=True, blank=True)
    estimation_files = models.FileField(upload_to='project_estimation/', null=True, blank=True)
    Addendum_Date = models.DateTimeField(blank=True, null=True)
    Project_Posted_Date = models.DateTimeField(blank=True, null=True)
    Project_Bid_Date = models.DateTimeField(blank=True, null=True)
    Project_Work_Started_Date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_updated = models.ForeignKey(
        get_user_model(),
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='updated_Project'
    )
    user_deleted = models.ForeignKey(
        get_user_model(),
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='deleted_Project'
    )
    user_restored = models.ForeignKey(
        get_user_model(),
        models.DO_NOTHING,
        blank=True,
        null=True,
        related_name='restored_Project'
    )
    contractors = models.ManyToManyField(User, related_name='projects_as_contractor', blank=True)

    def delete(self, *args, **kwargs):
        try:
            # Attempt to get the 'deleted_user' or create it if it doesn't exist
            self.user_deleted = get_user_model().objects.get(username='deleted_user')
        except get_user_model().DoesNotExist:
            # If 'deleted_user' doesn't exist, create it
            self.user_deleted = get_user_model().objects.create(username='deleted_user')

        # Save the project with the 'user_deleted' set
        super().delete(*args, **kwargs)

    def restore(self, *args, **kwargs):
        self.user_restored = get_user_model().objects.get(username='restored_user')
        self.save()

    #To save 
    def __str__(self):
        return self.project_name


class Bid(models.Model):
    BIDDING_METHOD_CHOICES = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Selective', 'Selective'),
    )
    BID_PHASE_CHOICES = (    
        ('Pre-Bid', 'Pre-Bid'),
        ('Bidding', 'Bidding'),
        ('Post-Bid', 'Post-Bid'),
        ('Open-Solicitation', 'Open Solicitation'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)

    bid_history = models.ForeignKey('BidHistory', on_delete=models.CASCADE,blank=True,null=True)
    bidding_method = models.CharField(max_length=20, choices=BIDDING_METHOD_CHOICES,blank=True,null=True)
    bid_phase = models.CharField(max_length=20, choices=BID_PHASE_CHOICES,blank=True,null=True)
    project_completion_time = models.IntegerField(blank=True,null=True)  # Assuming this represents days

    def __str__(self):
        return f"Bid for {self.project.project_name}"
    # Bid History Table will be used for Making for projects and Company as well 
class BidHistory(models.Model):
    bid_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company,blank=True, on_delete=models.CASCADE,null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)
    bid_outcome = models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return f"Bid {self.bid_id}"


from django.core.validators import MinValueValidator, MaxValueValidator

class Solicitation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True)
    notes = models.TextField(blank=True,null=True)
    solicitation_date = models.DateField(blank=True,null=True)
    liquidated_damages = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    pre_bid_meeting_date = models.DateField(blank=True,null=True)
    pre_bid_meeting_notes = models.TextField(blank=True,null=True)
    bid_bond = models.DecimalField(max_digits=5, decimal_places=2, default=15, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)],null=True)
    performance_bond = models.DecimalField(max_digits=5, decimal_places=2, default=15, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)],null=True)
    payment_bond_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=100, blank=True, validators=[MinValueValidator(1), MaxValueValidator(100)],null=True)
    bid_date = models.DateField(blank=True,null=True)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    bid_location = models.CharField(max_length=100, blank=True,null=True)

    def __str__(self):
        return f"Solicitation for {self.project.project_name}"

    
class MWSEBsAndSDVOBs(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # will use for WBE
    mwsebs = models.DecimalField(max_digits=5, decimal_places=2, default=15,blank=True,null=True)
    sdvobs = models.DecimalField(max_digits=5, decimal_places=2, default=15,blank=True,null=True)
    MBE = models.DecimalField(max_digits=5, decimal_places=2, default=15,blank=True,null=True)
    EEO = models.DecimalField(max_digits=5, decimal_places=2, default=0,blank=True,null=True)
    def __str__(self):
        return f"MWSEBs and SDVOBs for {self.project.project_name}"









class Document(models.Model):
    DOCUMENT_TYPE_CHOICES = (
        ('Specification Sheet', 'Specification Sheet'),
        ('Quantity Takeoff', 'Quantity Takeoff'),
        ('Addendum', 'Addendum'),
        ('Other', 'Other'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50, choices=DOCUMENT_TYPE_CHOICES)
    document_name = models.CharField(max_length=100)
    document_path = models.FileField(upload_to='documents/')  # Store documents in the file system
    quantity_takeoffs_video = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.document_name

class ProjectAddendum(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Addendum_file = models.FileField(upload_to='project_addendum/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_ProjectAddendum')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_ProjectAddendum')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_ProjectAddendum')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_ProjectAddendum')
    created_at = models.DateTimeField(blank=True, null=True,auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def save(self, *args, **kwargs):
        # Update the 'created_at' field with the current timestamp
        if not self.created_at:
            self.created_at = timezone.now()

        super().save(*args, **kwargs)
    def __str__(self):
        return self.document_name
class ProjectPlans(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    Plans_file = models.FileField(upload_to='project_plans/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_ProjectPlans')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_ProjectPlans')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_ProjectPlans')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_ProjectPlans')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Plans for {self.project.project_name}"
class ProjectSpecifications(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    specifications_file = models.FileField(upload_to='project_specifications/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_ProjectSpecifications')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_ProjectSpecifications')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_ProjectSpecifications')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_ProjectSpecifications')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Specifications for {self.project.project_name}"
class Project_Bid_Documents(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    bid_file = models.FileField(upload_to='project_bid_documets/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_Bid_Documents')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_Bid_Documents')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_Bid_Documents')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_Bid_Documents')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Bid Documents for {self.project.project_name}"
class Project_Misclinius_Documents(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    misclinius_file = models.FileField(upload_to='project_Misclinius_documets/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_Misclinius_Document')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_Misclinius_Document')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_Misclinius_Document')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_Misclinius_Document')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Misclinius Documents for {self.project.project_name}"
class Project_Takeoff_Documents(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    takeoff_file = models.FileField(upload_to='project_Takeoff_documets/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_Takeoff_Documents')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_Takeoff_Documents')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_Takeoff_Documents')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_Takeoff_Documents')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Takeoff Documents for {self.project.project_name}"
class Project_swift_file_Documents(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    swift_file = models.FileField(upload_to='project_swift_file_documets/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_swift_file')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_swift_file')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_swift_file')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_swift_file')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Swift Files for {self.project.project_name}"
class Project_Drawings_Documents(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    drawings_file = models.FileField(upload_to='project_drawing_documets/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_Drawings')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_Drawings')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_Drawings')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_Drawings')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Drawings for {self.project.project_name}"
class ProjectEstimation_misc(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    estimation_misc_file = models.FileField(upload_to='project_estimation/')
    user_created = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='created_Estimation')
    user_updated = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='updated_Estimation')
    user_deleted = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='deleted_Estimation')
    user_restored = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True, related_name='restored_Estimation')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return f"Estimation for {self.project.project_name}"