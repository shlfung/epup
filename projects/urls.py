from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path("projects/", views.ProjectListView.as_view(), name='projects'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='project-create')

]