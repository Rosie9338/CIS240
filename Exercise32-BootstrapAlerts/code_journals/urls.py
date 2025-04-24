"""Defines URL patterns for code_journals."""

from django.urls import path

from . import views
app_name = 'code_journals'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # ---snip---
    # Show all topics.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # --snip--
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
	# Page for displaying a bar chart
	path('bar_chart/', views.bar_chart, name='bar_chart'),
    #Page for editing an existing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    #Delete Topic
    path('delete_topic/<int:topic_id>/', views.delete, name='delete'),
    ]
