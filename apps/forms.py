from django import forms
from .models import ProjectPlans,ProjectSpecifications ,Project_Takeoff_Documents,Authority,SubAuthority,CrmContact,CrmCompany,CrmLead,JobApplication,EcommerceOrder,EcommerceCustomer,TicketList,Company,Person,Address,Company_Details,Project,Bid,Solicitation,MWSEBsAndSDVOBs
from django.contrib.auth import get_user_model

class CrmContactAddForm(forms.ModelForm):
    
    class Meta:
        model = CrmContact
        fields = ['profile_pic','name','company_name','designation','email_id','phone','lead_score','tags']
        
class CrmContactUpdateForm(forms.ModelForm):  
    class Meta:
        model = CrmContact
        fields = ['profile_pic','name','company_name','designation','email_id','phone','lead_score','tags']
        
class CrmCompanyAddForm(forms.ModelForm):
    class Meta:
        model = CrmCompany
        fields = ['logo','name','owner_name','industry_type','rating','location','employee','website','contact_email','since']
        
class CrmCompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = CrmCompany
        fields = ['logo','name','owner_name','industry_type','rating','location','employee','website','contact_email','since']
        
class CrmLeadsAddForm(forms.ModelForm):
    class Meta:
        model = CrmLead
        fields = ['profile_pic','name','company_name','lead_score','phone','location','tags','create_date']

class CrmLeadsUpdateForm(forms.ModelForm):
    class Meta:
        model = CrmLead
        fields = ['profile_pic','name','company_name','lead_score','phone','location','tags','create_date']
        
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['profile_pic','company_name','designation','apply_date','contact','status','type']
        
class EcommerceOrderForm(forms.ModelForm):
    class Meta:
        model = EcommerceOrder
        fields = ['name','product','order_date','amount','payment_method','status']
        
class EcommerceCustomerForm(forms.ModelForm):
    class Meta:
        model = EcommerceCustomer
        fields = ['name','email_id','phone','joining_date','status']
        
class TicketListForm(forms.ModelForm):
    class Meta:
        model = TicketList
        fields = ['title','client_name','assign_to','create_date','due_date','status','priority']
  

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'

def validate_percentage(value):
    if value < 1 or value > 100:
        raise forms.ValidationError('Percentage must be between 1 and 100.')


class Project_Create_Form(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
      
    # Bid model fields
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
    bid_amount = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    # bid_history = forms.ModelChoiceField(queryset=BidHistory.objects.all(), required=False)
    bidding_method = forms.ChoiceField(choices=BIDDING_METHOD_CHOICES, required=False)
    bid_phase = forms.ChoiceField(choices=BID_PHASE_CHOICES, required=False)
    project_completion_time = forms.IntegerField(required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    solicitation_date = forms.DateField(required=False)
    liquidated_damages = forms.DecimalField(max_digits=10, decimal_places=2, required=False)
    pre_bid_meeting_date = forms.DateField(required=False)
    pre_bid_meeting_notes = forms.CharField(widget=forms.Textarea, required=False)
    bid_bond = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    performance_bond = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    payment_bond_percentage = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    bid_date = forms.DateField(required=False)
    bid_location = forms.CharField(max_length=100, required=False)

    mwsebs = forms.DecimalField(max_digits=5, decimal_places=2, required=False, validators=[validate_percentage])
    sdvobs = forms.DecimalField(max_digits=5, decimal_places=2, required=False, validators=[validate_percentage])
    MBE = forms.DecimalField(max_digits=5, decimal_places=2, required=False, validators=[validate_percentage])
    EEO = forms.DecimalField(max_digits=5, decimal_places=2, required=False, validators=[validate_percentage])
    

    # Project Address model fields
    location = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=50, required=False)
    state = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=50, required=False)

    Project_plans = forms.FileField(required=False)
    Project_specs = forms.FileField(required=False)
    Project_take_offs = forms.FileField(required=False)

    AUTHORITIES = [
        ('SCA', 'SCA'),
        # Add more options as needed
      ]
    SUB_AUTHORITIES = [
        ('MENTOR', 'MENTOR'),
        ('CIP', 'CIP'),
        ('GRADUATE_MENTOR', 'Graduate MENTOR'),
        ('Capacity_Projects', 'Capacity Projects'),
        ('other', 'Other'),
        # Add more options as needed
      ]

    Authority = forms.ChoiceField(choices=AUTHORITIES, required=False)
    SubAuthority = forms.ChoiceField(choices=SUB_AUTHORITIES, required=False)
    # Add the form-control class to the widget attributes
    def __init__(self, *args, **kwargs):
        super(Project_Create_Form, self).__init__(*args, **kwargs)
        self.fields['project_files'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True, user=None):
        project = super().save(commit=False)
        if user:
            project.user_created = user
            project.save()
        if commit:
            # Create Address instance associated with the saved Project
            Address.objects.create(
                project=project,
                location=self.cleaned_data['location'],
                country=self.cleaned_data['country'],
                state=self.cleaned_data['state'],
                city=self.cleaned_data['city'],
            )
            
            # Create Bid instance associated with the saved Project
            Bid.objects.create(
                project=project,
                bid_amount=self.cleaned_data['bid_amount'],
                bidding_method=self.cleaned_data['bidding_method'],
                bid_phase=self.cleaned_data['bid_phase'],
                project_completion_time=self.cleaned_data['project_completion_time'],
                notes=self.cleaned_data['notes'],
                solicitation_date=self.cleaned_data['solicitation_date'],
                liquidated_damages=self.cleaned_data['liquidated_damages'],
                pre_bid_meeting_date=self.cleaned_data['pre_bid_meeting_date'],
                pre_bid_meeting_notes=self.cleaned_data['pre_bid_meeting_notes'],
                bid_bond=self.cleaned_data['bid_bond'],
                performance_bond=self.cleaned_data['performance_bond'],
                payment_bond_percentage=self.cleaned_data['payment_bond_percentage'],
                bid_date=self.cleaned_data['bid_date'],
                bid_location=self.cleaned_data['bid_location']
            )

            # Create MWSEBsAndSDVOBs instance associated with the saved Project
            MWSEBsAndSDVOBs.objects.create(
                project=project,
                mwsebs=self.cleaned_data['mwsebs'],
                sdvobs=self.cleaned_data['sdvobs'],
                MBE=self.cleaned_data['MBE'],
                EEO=self.cleaned_data['EEO'],
            )

            # Create ProjectPlans instance associated with the saved Project
            ProjectPlans.objects.create(
                project=project,
                Project_plans=self.cleaned_data['Project_plans'],
            )
            
            # Create ProjectSpecifications instance associated with the saved Project
            ProjectSpecifications.objects.create(
                project=project,
                Project_specs=self.cleaned_data['Project_specs'],
            )

            # Create Project_Takeoff_Documents instance associated with the saved Project
            Project_Takeoff_Documents.objects.create(
                project=project,
                Project_take_offs=self.cleaned_data['Project_take_offs'],
            )

        return project

class Company_create_Form(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    # Define Address fields using model form fields0
    location = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=50, required=False)
    state = forms.CharField(max_length=50, required=False)
    city = forms.CharField(max_length=50, required=False)
    zip_code = forms.CharField(max_length=10, required=False)
    year_founded = forms.DateField(required=False)
    csi_division = forms.CharField(max_length=50, required=False)
    financial_information = forms.CharField(max_length=200, required=False)
    notes_and_comments = forms.CharField(max_length=200, required=False)
    type_of_construction = forms.CharField(max_length=50, required=False)
    size = forms.CharField(max_length=50, required=False)
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField(max_length=254, required=False)
    phone_no = forms.CharField(max_length=15, required=False)


     # Define Company Address fields using model form fields
    company_location = forms.CharField(max_length=100, required=False)
    company_country = forms.CharField(max_length=50, required=False)
    company_state = forms.CharField(max_length=50, required=False)
    company_city = forms.CharField(max_length=50, required=False)
    company_zip_code = forms.CharField(max_length=10, required=False)
    # Define Person Address fields using model form fields
    person_location = forms.CharField(max_length=100, required=False)
    person_country = forms.CharField(max_length=50, required=False)
    person_state = forms.CharField(max_length=50, required=False)
    person_city = forms.CharField(max_length=50, required=False)
    person_zip_code = forms.CharField(max_length=10, required=False)


    def save(self, commit=True):
        company = super().save(commit=False)

        if commit:
            # Create an Address instance for the company
            company_address, _ = Address.objects.get_or_create(
                location=self.cleaned_data['company_location'],
                country=self.cleaned_data['company_country'],
                state=self.cleaned_data['company_state'],
                zip_code=self.cleaned_data['company_zip_code'],
            )
            company_address.save()

            # Create an Address instance for the person
            person_address, _ = Address.objects.get_or_create(
                location=self.cleaned_data['person_location'],
                country=self.cleaned_data['person_country'],
                state=self.cleaned_data['person_state'],
                zip_code=self.cleaned_data['person_zip_code'],
            )
            person_address.save()

            # Create or get Company_Details instance
            company_details, _ = Company_Details.objects.get_or_create(
                year_founded=self.cleaned_data['year_founded'],
                csi_division=self.cleaned_data['csi_division'],
                financial_information=self.cleaned_data['financial_information'],
                notes_and_comments=self.cleaned_data['notes_and_comments'],
                type_of_construction=self.cleaned_data['type_of_construction'],
                size=self.cleaned_data['size'],
            )

            # Create Person instance
            person_details = Person.objects.create(
                name=self.cleaned_data['name'],
                email=self.cleaned_data['email'],
                phone_no=self.cleaned_data['phone_no'],
                address=person_address  # Assigning person's address
            )

            # Save the person_Details instance
            person_details.save()

            # Associate the created instances with the company
            company.company_address = company_address
            company.company_details = company_details
            company.contact_person = person_details
            company.save()

        return company

    
    

class CrmPersonAddForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'name',
            'email',
            'phone_no',
            'role',
        ]

class CrmAddressAddForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'location',
            'country',
            'state',
            'zip_code'
        ]