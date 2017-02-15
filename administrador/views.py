from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publisher, Author, Book
from django.shortcuts import get_object_or_404

# Create your views here.


class PublisherList(ListView):
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'


class PublisherFilter(ListView):
    model = Publisher
    template_name = 'publisher_list.html'
    context_object_name = 'publisher_list'

    def get_queryset(self):
        print self.args[0]
        self.editorial = get_object_or_404(Publisher, name=self.args[0])
        return self.editorial

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherFilter, self).get_context_data(**kwargs)
        # Add in the publisher
        context['editorial'] = self.editorial
        return context

class PublisherDetail(DetailView):

    model = Publisher
    template_name = 'publisher_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context

