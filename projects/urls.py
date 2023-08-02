from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('detail/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path("projects/", views.ProjectListView.as_view(), name='projects'),
    path('create/', views.create, name='project-create'),
    path('update/<int:id>', views.update, name='project-update')
]