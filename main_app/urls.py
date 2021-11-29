from django.urls import path
from . import views

# localhost:8000/
urlpatterns = [
  # localhost:8000/
  path('', views.Home.as_view(), name='home'),
  # localhost:8000/about/
  path('about/', views.about, name="about"),
  # localhost:8000/finchs/
  path('finchs/', views.finchs_index, name='finchs_index'),
  # localhost:8000/finchs/:finch_id
  path('finchs/<int:finch_id>/', views.finchs_detail, name='finchs_detail'),
  # localhost:8000/finchs/create
  path('finchs/create/', views.FinchCreate.as_view(), name='finchs_create'),
  # localhost:8000/finchs/:pk/update
  path('finchs/<int:pk>/update', views.FinchUpdate.as_view(), name="finchs_update"),
  # localhost:8000/finchs/:pk/delete
  path('finchs/<int:pk>/delete', views.FinchDelete.as_view(), name="finchs_delete"),
  # localhost:8000/finchs/:finch_id/add_feeding/
  path('finchs/<int:finch_id>/add_feeding/', views.add_feeding, name="add_feeding"),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  # Associate a toy with a finch
  # localhost:8000/finchs/:finch_id/assoc_toy/:toy_id/
  path('finchs/<int:finch_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  # New url pattern below
path('accounts/signup/', views.signup, name='signup'),
]