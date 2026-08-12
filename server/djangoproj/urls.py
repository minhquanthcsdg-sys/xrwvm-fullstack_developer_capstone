from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from djangoapp.views import login_user, get_dealer_reviews, get_all_dealers, get_dealer_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="Home.html")),
    path('about/', TemplateView.as_view(template_name="About.html")),
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
    path('api/login/', login_user, name='login'),
    path('api/dealer/<int:dealer_id>/reviews/', get_dealer_reviews, name='dealer_reviews'),
    path('api/dealers/', get_all_dealers, name='all_dealers'),
    path('api/dealer/<int:dealer_id>/', get_dealer_by_id, name='dealer_by_id'),
]
