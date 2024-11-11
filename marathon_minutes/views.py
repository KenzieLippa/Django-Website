from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Result

import plotly
import plotly.graph_objects as go


class ResultsListView(ListView):
    '''View to display marathon results'''
    template_name = 'marathon_minutes/results.html'
    model = Result
    context_object_name = 'results'
    paginate_by = 50
    def get_queryset(self):
        
        # start with entire queryset
        qs = super().get_queryset().order_by('place_overall')
        # filter results by these field(s):
        if 'city' in self.request.GET:
            city = self.request.GET['city']
            if city:
                qs = qs.filter(city=city)
                
        return qs

class ResultDetailView(DetailView):
    template_name = 'marathon_minutes/result_detail.html'
    model = Result
    context_object_name = 'r'
    def get_context_data(self, **kwargs) :
        '''
        Provide context variables for use in template
        '''
        # start with superclass context
        context = super().get_context_data(**kwargs)
        r = context['r']
        # create graph of first half/second half as pie chart:
        x = ['first half', 'second half']
        first_half_seconds = (r.time_half1.hour * 60 + r.time_half1.minute) * 60 + r.time_half1.second
        second_half_seconds = (r.time_half2.hour * 60 + r.time_half2.minute) * 60 + r.time_half2.second
        y = [first_half_seconds , second_half_seconds]
        
        # generate the Pie chart
        fig = go.Pie(labels=x, values=y) 
        title_text = f"Half Marathon Splits"
        # obtain the graph as an HTML div"
        graph_div_splits = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title_text,
                                         }, 
                                         auto_open=False, 
                                         output_type="div")
        # send div as template context variable
        context['graph_div_splits'] = graph_div_splits

        # create graph of runners who passed/passed by
        x= [f'Runners Passed by {r.first_name}', f'Runners who Passed {r.first_name}']
        y = [r.get_runners_passed(), r.get_runners_passed_by()]
        
        fig = go.Bar(x=x, y=y)
        title_text = f"Runners Passed/Passed By"
        graph_div_passed = plotly.offline.plot({"data": [fig], 
                                         "layout_title_text": title_text,
                                         }, auto_open=False, output_type="div",
                                         
                                         ) 
        context['graph_div_passed'] = graph_div_passed
        return context