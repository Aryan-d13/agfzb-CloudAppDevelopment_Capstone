from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import my_view

app_name = 'djangoapp'
urlpatterns = [
    path('my-template/', my_view, name='my_template'),
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    path('about/', views.about_view, name='about'),

    path('contact/', views.contact_view, name='contact'),

    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)