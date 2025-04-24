from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from . models import Topic, Entry
from .forms import TopicForm, EntryForm
import plotly.express as px
import pandas as pd
def index(request):
	"""The home page for Code Journal"""
	return render(request, 'code_journals/index.html')


def topics(request):
	"""Show all topics"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'code_journals/topics.html', context)


def topic(request, topic_id):
	"""Show a single topic and all its entries"""
	topic = Topic.objects.get(id=topic_id)
	entries = topic.entry_set.order_by('-date_added')
	context = {'topic': topic, 'entries': entries}
	return render(request, 'code_journals/topic.html', context)

def new_topic(request):
	"""Add a new topic."""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TopicForm()
	else:
		# Post data submitted; process data.
		form = TopicForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('code_journals:topics'))

	context = {'form': form}
	return render(request, 'code_journals/new_topic.html', context)


def new_entry(request, topic_id):
	"""Add a new entry for a particular topic."""
	topic = Topic.objects.get(id=topic_id)
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = EntryForm()
	else:
		# POST data submitted; process data.
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('code_journals:topic', args=[topic_id]))
	
	context = {'topic': topic, 'form': form}
	return render(request, 'code_journals/new_entry.html', context)


def bar_chart(request):
	topics = Topic.objects.all()
	topic_entry_counts = [(topic.text, topic.entry_set.count()) for topic in topics]
	df = pd.DataFrame(topic_entry_counts, columns=['Topic', 'Entry Count'])
	fig = px.bar(df, x='Topic', y='Entry Count', color='Topic', title='Number of Entries per Topic')
	fig.update_yaxes(tickformat='d', dtick=1)
	chart_html = fig.to_html()
	context = {'chart_html': chart_html}
	return render(request, 'code_journals/bar_chart.html', context)

def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = EntryForm(instance=entry)
	else:
		# POST data submitted; process data.
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('code_journals:topic', args=[topic.id]))

	# The context dictionary contains the entry being edited, its associated topic, and the form for editing.
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'code_journals/edit_entry.html', context)

def delete(request, topic_id):
	"""Show a single topic and all its entries"""
	delete = Topic.objects.get(id=topic_id)
	delete.delete()
	return HttpResponseRedirect(reverse('code_journals:topics'))
