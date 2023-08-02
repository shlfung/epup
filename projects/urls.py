from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path('projects/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path('detail/<int:pk>', views.ProjectDetailView.as_view(), name='project-detail'),
    path("projects/", views.ProjectListView.as_view(), name='projects'),

    #path('projects/create/', views.ProjectCreateView.as_view(), name='project-create'),
    path('create/', views.create, name='project-create'),
    #path('projects/update/<int:pk>', views.ProjectUpdateView.as_view(), name='project-update')
    #path('projects/update/<int:id>', views.update, name='project-update')
    path('update/<int:id>', views.update, name='project-update')
]