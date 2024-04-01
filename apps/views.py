import logging
from django.shortcuts import redirect, render,get_object_or_404 
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CrmContact,CrmCompany,CrmLead,JobApplication,EcommerceOrder,EcommerceCustomer,TicketList,Project,Company,Person,Address

from .forms import CrmContactAddForm,Company_create_Form,Project_Create_Form,CrmContactAddForm,Company_create_Form,Project_Create_Form,BidForm,EcommerceCustomerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
# Create your views here.
class AppsView(LoginRequiredMixin,TemplateView):
    pass
  
# Calendar
apps_calendar_view = AppsView.as_view(template_name="apps/apps-calendar.html")
# Chat
apps_chat_view = AppsView.as_view(template_name="apps/apps-chat.html")
# Mail Box
apps_mailbox_view = AppsView.as_view(template_name="apps/email/apps-mailbox.html")
apps_basicaction_view = AppsView.as_view(template_name="apps/email/apps-email-basic.html")
apps_invoiceaction_view = AppsView.as_view(template_name="apps/email/apps-email-ecommerce.html")

# Ecommerce
apps_ecommerce_products_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-products.html")
apps_ecommerce_product_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-product-details.html")
apps_ecommerce_add_product_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-add-product.html")
# apps_ecommerce_orders_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-orders.html")
apps_ecommerce_order_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-order-details.html")
# apps_ecommerce_customers_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-customers.html")
apps_ecommerce_cart_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-cart.html")
apps_ecommerce_checkout_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-checkout.html")
apps_ecommerce_sellers_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-sellers.html")
apps_ecommerce_seller_details_view = AppsView.as_view(template_name="apps/ecommerce/apps-ecommerce-seller-details.html")

# Projects
apps_projects_list_view = AppsView.as_view(template_name="apps/projects/apps-projects-list.html")
apps_projects_overview_view = AppsView.as_view(template_name="apps/projects/apps-projects-overview.html")
apps_projects_create_view = AppsView.as_view(template_name="apps/projects/apps-projects-create.html")

# Companies

apps_Companies_list_view = AppsView.as_view(template_name="apps/companies/apps-projects-list.html")
apps_Companies_Create_view =AppsView.as_view(template_name="apps/companies/apps-companies-create.html")

# Tasks
apps_tasks_kanban_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-kanban.html")
apps_tasks_list_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-list-view.html")
apps_tasks_details_view = AppsView.as_view(template_name="apps/tasks/apps-tasks-details.html")

# CRM
apps_crm_contacts_view = AppsView.as_view(template_name="apps/crm/apps-crm-contacts.html")
apps_crm_companies_view = AppsView.as_view(template_name="apps/crm/apps-crm-companies.html")
apps_crm_deals_view = AppsView.as_view(template_name="apps/crm/apps-crm-deals.html")
apps_crm_leads_view = AppsView.as_view(template_name="apps/crm/apps-crm-leads.html")

# Crypto
apps_crypto_transactions_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-transactions.html")
apps_crypto_buy_sell_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-buy-sell.html")
apps_crypto_orders_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-orders.html")
apps_crypto_wallet_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-wallet.html")
apps_crypto_ico_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-ico.html")
apps_crypto_kyc_view = AppsView.as_view(template_name="apps/crypto/apps-crypto-kyc.html")

# Invoices
apps_invoices_list_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-list.html")
apps_invoices_details_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-details.html")
apps_invoices_create_view = AppsView.as_view(template_name="apps/invoices/apps-invoices-create.html")

# Support Tickets
# apps_tickets_list_view = AppsView.as_view(template_name="apps/support-tickets/apps-tickets-list.html")
apps_tickets_details_view = AppsView.as_view(template_name="apps/support-tickets/apps-tickets-details.html")

#NFT pages
apps_nft_marketplace_view = AppsView.as_view(template_name="apps/nft/apps-nft-marketplace.html")
apps_nft_explore_view = AppsView.as_view(template_name="apps/nft/apps-nft-explore.html")
apps_nft_liveauction_view = AppsView.as_view(template_name="apps/nft/apps-nft-auction.html")
apps_nft_itemdetails_view= AppsView.as_view(template_name="apps/nft/apps-nft-item-details.html")
apps_nft_collections_view= AppsView.as_view(template_name="apps/nft/apps-nft-collections.html")
apps_nft_creators_view = AppsView.as_view(template_name="apps/nft/apps-nft-creators.html")
apps_nft_ranking_view = AppsView.as_view(template_name="apps/nft/apps-nft-ranking.html")
apps_nft_wallet_view = AppsView.as_view(template_name="apps/nft/apps-nft-wallet.html")
apps_nft_create_view = AppsView.as_view(template_name="apps/nft/apps-nft-create.html")

#Job Pages
# apps_job_application_view = AppsView.as_view(template_name="apps/jobs/apps-job-application.html")
apps_job_candidate_grid_view = AppsView.as_view(template_name="apps/jobs/apps-job-candidate-grid.html")
apps_job_candidate_lists_view = AppsView.as_view(template_name="apps/jobs/apps-job-candidate-lists.html")
apps_job_companies_lists_view = AppsView.as_view(template_name="apps/jobs/apps-job-companies-lists.html")
apps_job_categories_view = AppsView.as_view(template_name="apps/jobs/apps-job-categories.html")
apps_job_details_view = AppsView.as_view(template_name="apps/jobs/apps-job-details.html")
apps_job_grid_lists_view = AppsView.as_view(template_name="apps/jobs/apps-job-grid-lists.html")
apps_job_lists_view = AppsView.as_view(template_name="apps/jobs/apps-job-lists.html")
apps_job_new_view = AppsView.as_view(template_name="apps/jobs/apps-job-new.html")
apps_job_statistics_view = AppsView.as_view(template_name="apps/jobs/apps-job-statistics.html")

# Calendar
apps_file_manager_view = AppsView.as_view(template_name="apps/apps-file-manager.html")

# Calendar
apps_todo_view = AppsView.as_view(template_name="apps/apps-todo.html")

apps_api_key_view = AppsView.as_view(template_name="apps/apps-api-key.html")






def apps_crm_contacts_view(request,pk):

    
    contacts = CrmContact.objects.all().order_by('-id')
    if contacts:
        contact = CrmContact.objects.get(pk=pk)
    return render(request,"apps/crm/apps-crm-contacts.html",{'contacts':contacts,'contact':contact})
def apps_crm_persons_view(request):
    persons = Person.objects.all().order_by('-person_id')

    return render(request,"apps/crm/apps-crm-persons.html",{'persons':persons})


@login_required
def apps_crm_add_contacts_view(request):
    contacts = CrmContact.objects.all().order_by("-id")
    
    if request.method == 'POST':
        form = CrmContactAddForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.created_by = request.user  # Assuming you have a 'created_by' field in your CrmContact model
            form.save()
            messages.success(request,"Contact inserted successfully!")
            return redirect("apps:crm.contacts")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.contacts")
    return render(request,"apps/crm/apps-crm-contacts.html",{'contacts':contacts})

def apps_crm_update_contacts_view(request,pk):
    contact = CrmContact.objects.get(pk=pk)
    if request.method == "POST":
        form = CrmContactUpdateForm(request.POST or None,request.FILES or None,instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request,"Contact updated successfully!")
            return redirect("apps:crm.contacts")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.contacts")
    return render(request,'apps/crm/apps-crm-contacts.html',{'contact':contact})

def apps_crm_delete_contacts_view(request,pk):
    contacts = CrmContact.objects.get(pk=pk)
    contacts.delete()
    messages.success(request,"Contact deleted successfully!")
    return redirect("apps:crm.contacts")

# Crm Companies views

def apps_crm_companies_view(request, pk):
    # Retrieve all companies ordered by company_id in descending order
    companies = Company.objects.all().order_by('-company_id')
    
    # Check if there are any companies
    if companies:
        # If there are companies, retrieve the specific company with the given primary key (pk)
        company = Company.objects.get(pk=pk)
    else:
        company = None  # If no companies exist, set company to None
    
    # Render the HTML template "apps/crm/apps-crm-companies.html" with the companies and selected company
    return render(request, "apps/crm/apps-crm-companies.html", {'companies': companies, 'company': company})



@login_required
def apps_crm_add_companies_view(request):
    companies = Company.objects.all().order_by('-company_id')

    if request.method == "POST":
        form = Company_create_Form(request.POST)

        if form.is_valid():
            company = form.save(commit=False)
            
            # Associate the company with the logged-in user
            company.user_created = request.user  # Assuming you have a 'created_by' field in your Company model
            
            # Now save the company to the database
            company.save()

            messages.success(request, "Company inserted successfully!")
            return redirect("apps:crm.companies")
        else:
            # Print form errors to the console
            print("Form errors:", form.errors)
            messages.error(request, "Something went wrong!")
            return redirect("apps:crm.companies")
    else:
        form = Company_create_Form()

    return render(request, "apps/crm/apps-crm-companies.html", {'companies': companies, 'form': form})


    return render(request, "apps/crm/apps-crm-companies.html", {'companies': companies})
def apps_Companies_overview_view(request, pk):
     company = get_object_or_404(Company, company_id=pk)
     return render(request, 'apps/crm/apps-crm-companies-overview.html', {'company': company})

def apps_crm_delete_companies_view(request, pk):
    try:
        Company = get_object_or_404(Company, project_id=pk)

        # Print the name of the user to the console
        user_name = request.user.username
        print(f"User {user_name} is deleting the project.")

        Company.user_deleted = request.user
        Company.delete()
        messages.success(request, "Company deleted successfully!")
        return redirect("apps:crm.companies")

    except Company.DoesNotExist:
        messages.error(request, "Company not found.")
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        messages.error(request, error_message)
        logger.exception(error_message)  # Log the exception details

    return render(request, "apps/crm/apps-crm-companies.html")


# Project

def apps_projects_list_view(request):
    projects = Project.objects.all().order_by('-project_id')
    return render(request, "apps/projects/apps-projects-list.html", {'projects': projects})
@login_required
def apps_projects_create_view(request):
    projects = Project.objects.all().order_by('-project_id')

    if request.method == 'POST': 
        print(request.FILES)  # Add this line
        form = Project_Create_Form(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            
            project.user_created = request.user
            # Save the project
            project.save()

            messages.success(request, "Project and Bid inserted successfully!")
            return redirect("apps:projects.list")
        else:
            # Print form errors to the console
            print("Form errors:", form.errors)
            messages.error(request, "Something went wrong!")

            return redirect('apps:projects.list')  # Replace 'success_url' with the URL where you want to redirect after successful form submission
    else:
        form = Project_Create_Form()

    return render(request, "apps/projects/apps-projects-create.html", {'projects': projects, 'form': form})



def apps_projects_overview_view(request, pk):
     project = get_object_or_404(Project, project_id=pk)
     return render(request, 'apps/projects/apps-projects-overview.html', {'project': project})


def apps_projects_delete_view(request, pk):
    try:
        project = get_object_or_404(Project, project_id=pk)
        project.delete()
        messages.success(request, "Project deleted successfully!")
        return redirect("apps:projects.list")

    except Project.DoesNotExist:
        messages.error(request, "Project not found.")
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        messages.error(request, error_message)
    return render(request, 'apps/projects/apps-projects-list.html')



def apps_crm_update_companies_view(request,pk):
    companies = Company.objects.get(pk=pk) 
    if request.method == "POST":
        form = Company_create_Form(request.POST or None,request.FILES or None,instance=companies)
        if form.is_valid():
            form.save()
            messages.success(request,"Company updated successfully!")
            return redirect("apps:crm.companies")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.companies")
    return render(request,"apps/crm/apps-crm-companies.html")
def apps_crm_delete_companies_view(request,pk):
    companies = Company.objects.get(pk=pk)
    companies.delete()
    messages.success(request,"Contact deleted successfully!")
    return redirect("apps:crm.companies")

# Crm Leads views

def apps_crm_leads_view(request):
    leads = CrmLead.objects.all().order_by('-id')
    if request.method == 'POST':
        form = CrmLeadsAddForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Lead inserted successfully!")
            return redirect("apps:crm.leads")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.leads")
    return render(request,"apps/crm/apps-crm-leads.html",{'leads':leads})

def apps_crm_update_leads_view(request,pk):
    lead = CrmLead.objects.get(pk=pk)
    if request.method == "POST":
        form = CrmLeadsUpdateForm(request.POST or None,request.FILES or None,instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request,"Lead Updated successfully!")
            return redirect("apps:crm.leads")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:crm.leads")
    return render(request,"apps/crm/apps-crm-leads.html")

def apps_crm_delete_leads_view(request,pk):
    leads = CrmLead.objects.get(pk=pk)
    leads.delete()
    messages.success(request,"Contact deleted successfully!")
    return redirect("apps:crm.leads")

def apps_job_application_view(request):
    apps = JobApplication.objects.all().order_by('-id')
    if request.method == "POST":
        form = JobApplicationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Application inserted Successfully!")
            return redirect("apps:job.application")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:job.application")
    return render(request,'apps/jobs/apps-job-application.html',{'apps':apps})

def apps_job_update_application_view(request,pk):
    apps = JobApplication.objects.get(pk=pk)
    if request.method == "POST":
        form = JobApplicationForm(request.POST or None, request.FILES or None, instance=apps)
        if form.is_valid():
            form.save()
            messages.success(request,"Application updated Successfully!")
            return redirect("apps:job.application")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:job.application")
    return render(request,'apps/jobs/apps-job-application.html')

def apps_job_delete_application_view(request,pk):
    apps = JobApplication.objects.get(pk=pk)
    apps.delete()
    messages.success(request,"Application deleted Successfully!")
    return redirect("apps:job.application")

def apps_ecommerce_orders_view(request):
    orders = EcommerceOrder.objects.all().order_by('-id')
    if request.method == "POST":
        form = EcommerceOrderForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Order inserted Successfully!")
            return redirect("apps:ecommerce.orders")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:ecommerce.orders")
    return render(request,'apps/ecommerce/apps-ecommerce-orders.html',{'orders':orders})

def apps_ecommerce_update_orders_view(request,pk):
    orders = EcommerceOrder.objects.get(pk=pk)
    if request.method == 'POST':
        form = EcommerceOrderForm(request.POST or None, request.FILES or None,instance=orders)
        if form.is_valid():
            form.save()
            messages.success(request,"Order updated Successfully!")
            return redirect("apps:ecommerce.orders")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:ecommerce.orders")
    return render(request,'apps/ecommerce/apps-ecommerce-orders.html')

def apps_ecommerce_delete_orders_view(request,pk):
    orders = EcommerceOrder.objects.get(pk=pk)
    orders.delete()
    messages.success(request,"Order deleted Successfully!")
    return redirect("apps:ecommerce.orders")







@login_required
def apps_ecommerce_customers_view(request):
    # customers = EcommerceCustomer.objects.all().order_by('-id')
    customers = EcommerceCustomer.objects.filter(user=request.user).order_by('-id')
    if request.method == "POST":
        form = EcommerceCustomerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            customer = form.save(commit=False)  # Create a customer instance but don't save it yet
            customer.user = request.user  # Associate the customer with the logged-in user
            customer.save()  # Save the customer with the user association
            messages.success(request,"Customer inserted Successfully!")
            return redirect("apps:ecommerce.customers")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:ecommerce.customers")
    return render(request,'apps/ecommerce/apps-ecommerce-customers.html',{'customers':customers})

def apps_ecommerce_update_customers_view(request,pk):
    customers = EcommerceCustomer.objects.get(pk=pk)
    if request.method == 'POST':
        form = EcommerceCustomerForm(request.POST or None, request.FILES or None,instance=customers)
        if form.is_valid():
            form.save()
            messages.success(request,"Customer updated Successfully!")
            return redirect("apps:ecommerce.customers")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:ecommerce.customers")
    return render(request,'apps/ecommerce/apps-ecommerce-customers.html')

def apps_ecommerce_delete_customers_view(request,pk):
    customers = EcommerceCustomer.objects.get(pk=pk)
    customers.delete()
    messages.success(request,"Customer deleted Successfully!")
    return redirect("apps:ecommerce.customers")

def apps_tickets_list_view(request):
    tickets = TicketList.objects.all().order_by('-id')
    if request.method == "POST":
        form = TicketListForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Tickets inserted Successfully!")
            return redirect("apps:tickets.list")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:tickets.list")
    return render(request,'apps/support-tickets/apps-tickets-list.html',{'tickets':tickets})

def apps_tickets_update_list_view(request,pk):
    tickets = TicketList.objects.get(pk=pk)
    if request.method == "POST":
        form = TicketListForm(request.POST or None,request.FILES or None,instance=tickets)
        if form.is_valid():
            form.save()
            messages.success(request,"Tickets inserted Successfully!")
            return redirect("apps:tickets.list")
        else:
            messages.error(request,"Something went wrong!")
            return redirect("apps:tickets.list")
    return render(request,'apps/support-tickets/apps-tickets-list.html')

def apps_tickets_delete_list_view(request,pk):
    tickets = TicketList.objects.get(pk=pk)
    tickets.delete()
    messages.success(request,"Tickets deleted Successfully!")
    return redirect("apps:tickets.list")
