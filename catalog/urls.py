from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('share/', views.share, name='share'),
    path('qr/', views.qr, name='qr'),
    path('features/', views.FeaturesView.as_view(), name='features'),
    path('pricing/', views.PricingView.as_view(), name='pricing'),
    path('documentation/', views.documentation, name='documentation'),
    path('faq/', views.FAQView.as_view(), name='faq'),
    path('download/', views.download, name='download'),
    path('docs/', views.docs, name='docs'),
    path('product-intro/', views.product_intro, name='product_intro'),
    path('product-overview/', views.product_overview, name='product_overview'),
    path('purpose-usage/', views.purpose_usage, name='purpose_usage'),
    path('key-features/', views.key_features, name='key_features'),
    path('requirements/', views.requirements, name='requirements'),
    path('initial-setup/', views.initial_setup, name='initial_setup'),
    path('advanced-settings/', views.advanced_settings, name='advanced_settings'),
    path('reporting-management/', views.reporting_management, name='reporting_management'),
    path('support-training/', views.support_training, name='support_training'),
    path('demo-request/', views.demo_request, name='demo_request'),
] 