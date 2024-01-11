from django.urls import path
from .import views

urlpatterns = [
    path('first', views.home, name='home'),
    path('second',views.second,name='second'),
    path('', views.home_page, name='home_page'),
    path('add_path', views.add, name='add'),
    path('add_person', views.add_person, name='add_person'),
    path('views_person', views.views_person, name='views_person'),
    path('update_person/<int:id1>',views.Update_person,name='Update_person'),
    path('dlt_person/<int:id2>',views.dlt_person,name='dlt_person'),
    path('search',views.search,name='search')
]