from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Feature, PricingPlan, FAQ

# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')

def gallery(request):
    return render(request, 'catalog/gallery.html')

def share(request):
    return render(request, 'catalog/share.html')

def qr(request):
    return render(request, 'catalog/qr.html')

def download(request):
    return render(request, 'catalog/download.html')

def docs(request):
    return render(request, 'catalog/docs.html')

def product_intro(request):
    return render(request, 'catalog/product_intro.html')

# ویوهای جدید برای 8 بخش
def product_overview(request):
    return render(request, 'catalog/product_overview.html')

def purpose_usage(request):
    return render(request, 'catalog/purpose_usage.html')

def key_features(request):
    return render(request, 'catalog/key_features.html')

def requirements(request):
    return render(request, 'catalog/requirements.html')

def initial_setup(request):
    return render(request, 'catalog/initial_setup.html')

def advanced_settings(request):
    return render(request, 'catalog/advanced_settings.html')

def reporting_management(request):
    return render(request, 'catalog/reporting_management.html')

def support_training(request):
    return render(request, 'catalog/support_training.html')

class FeaturesView(TemplateView):
    template_name = 'catalog/features.html'

class PricingView(TemplateView):
    template_name = 'catalog/pricing.html'

class DocumentationView(TemplateView):
    template_name = 'catalog/documentation.html'

class FAQView(TemplateView):
    template_name = 'catalog/faq.html'
