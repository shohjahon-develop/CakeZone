from django.urls import path
from .views import (index, contact, about, menu, service, testimonial, team, onesdetailview, mastersdetailview,
                    saysdetailview, custsdetailview, chefsdetailview, vedsdetailview)

urlpatterns = [
path('', index, name='index'),
    path('menu/',menu , name='menu'),
    path('contact/', contact, name='contact'),
    path('service/',service,name='service'),
    path('about/', about, name='about'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('ones/<int:id>', onesdetailview, name='onesDetail'),
    path('masters/<int:id>', mastersdetailview, name='mastersDetail'),
    path('says/<int:id>',saysdetailview, name='saysDetail'),
    path('custs/<slug:custs>', custsdetailview, name='custsDetail'),
    path('chefs/<slug:chefs>', chefsdetailview, name='chefsDetail'),
    path('veds/<slug:chefs>', vedsdetailview, name='vedsDetail')
]