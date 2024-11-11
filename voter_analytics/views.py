from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.db.models import Count
from . models import Voter
# Create your views here.
import plotly
import plotly.graph_objs as go

class VoterListView(ListView):
    '''a view to display the voter lists'''
    template_name = "voter_analytics/voter.html"
    model = Voter
    context_object_name = "voters"
    paginate_by = 100

    def get_queryset(self):
        qs = super().get_queryset().order_by('last_name')
        #filter results
        # print(Voter.objects.values_list('party_affiliation', flat=True).distinct())
        # check the get request
        # if self.request.GET:
        #     print(self.request.GET)
        if 'party_affiliation' in self.request.GET:
            print("found")
            party_affilliation = self.request.GET['party_affiliation'].strip()
            if party_affilliation:
                print(party_affilliation)
                qs = qs.filter(party_affiliation=party_affilliation)
                print(len(qs))
            
        # see if you can use all ifs or if you need elifs
        if 'birthdate_min' in self.request.GET:
            birthdate = self.request.GET['birthdate_min']
            if birthdate:
                qs = qs.filter(birthdate__gt=birthdate)

        if 'birthdate_max' in self.request.GET:
            birthdate = self.request.GET['birthdate_max']
            if birthdate:
                qs = qs.filter(birthdate__lt=birthdate)

        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score:
                qs = qs.filter(voter_score=voter_score)

        if 'v20state' in self.request.GET:
            voted_in = self.request.GET['v20state']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v20state="TRUE")

        if 'v21town' in self.request.GET:
            voted_in = self.request.GET['v21town']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v21town="TRUE")

        if 'v21primary' in self.request.GET:
            voted_in = self.request.GET['v21primary']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v21primary="TRUE")
        
        if 'v22general' in self.request.GET:
            voted_in = self.request.GET['v22general']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v22general="TRUE")

        if 'v23town' in self.request.GET:
            voted_in = self.request.GET['v23town']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v23town="TRUE")
    
        return qs
    
class VoterDetailView(DetailView):
    '''a view to display details of the individual voter'''
    template_name = 'voter_analytics/voter_detail.html'
    model = Voter
    context_object_name = 'v'

    def get_context_data(self, **kwargs):
        '''Provide the context values for context'''
        #start with the super class
        context = super().get_context_data(**kwargs)
        v = context['v']

        return context

        # return super().get_context_data(**kwargs)

class GraphView(ListView):
    '''view to display the information for the voter base, will eventually need to figure out how to do the filter'''
    template_name = 'voter_analytics/graph.html'
    model = Voter
    # context_object_name ='v'

    # coppied the filter func
    def get_queryset(self):
        qs = super().get_queryset().order_by('last_name')
        #filter results
        # print(Voter.objects.values_list('party_affiliation', flat=True).distinct())
        # check the get request
        # if self.request.GET:
        #     print(self.request.GET)
        if 'party_affiliation' in self.request.GET:
            print("found")
            party_affilliation = self.request.GET['party_affiliation'].strip()
            if party_affilliation:
                print(party_affilliation)
                qs = qs.filter(party_affiliation=party_affilliation)
                print(len(qs))
            
        # see if you can use all ifs or if you need elifs
        if 'birthdate_min' in self.request.GET:
            birthdate = self.request.GET['birthdate_min']
            if birthdate:
                qs = qs.filter(birthdate__gt=birthdate)

        if 'birthdate_max' in self.request.GET:
            birthdate = self.request.GET['birthdate_max']
            if birthdate:
                qs = qs.filter(birthdate__lt=birthdate)

        if 'voter_score' in self.request.GET:
            voter_score = self.request.GET['voter_score']
            if voter_score:
                qs = qs.filter(voter_score=voter_score)

        if 'v20state' in self.request.GET:
            voted_in = self.request.GET['v20state']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v20state="TRUE")

        if 'v21town' in self.request.GET:
            voted_in = self.request.GET['v21town']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v21town="TRUE")

        if 'v21primary' in self.request.GET:
            voted_in = self.request.GET['v21primary']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v21primary="TRUE")
        
        if 'v22general' in self.request.GET:
            voted_in = self.request.GET['v22general']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v22general="TRUE")

        if 'v23town' in self.request.GET:
            voted_in = self.request.GET['v23town']
            if voted_in:
                print(voted_in) #not sure what this prints
                qs = qs.filter(v23town="TRUE")
    
        return qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # v = context['v']
        filtered_qs = self.get_queryset()

        birthdate = filtered_qs.values_list('birthdate', flat=True)
        # get all the birth years
        birth_years = [date.year for date in birthdate if date]
        hist_fig = go.Histogram(x=birth_years, nbinsx=50)
      
        title_text = f"Voter Distribution by Year of Birth"
        graph_div_hist = plotly.offline.plot({
            "data":[hist_fig],
            "layout_title_text": title_text,
            # "layout": go.Layout(
            #     title =  "Voter distribution by Year of Birth",
            #     xaxis_title = "Year of Birth",
            #     yaxis_title = "Count"

            # )
        }, auto_open=False, output_type="div")

        # get counts and categories
        party_counts = filtered_qs.values('party_affiliation').annotate(count=Count('party_affiliation'))

        # populate the labels and values before setting up the pie chart
        labels = [entry['party_affiliation'] for entry in party_counts if entry['party_affiliation']]
        values = [entry['count'] for entry in party_counts if entry['party_affiliation']]
        
        pie_fig = go.Pie(labels=labels, values=values)
        title_text = "Distribution of Voters by Party Affiliation"

        graph_div_pie = plotly.offline.plot({
            "data":[pie_fig],
            "layout_title_text": title_text,
        },
        auto_open=False,
        output_type="div")

        # get the categories for the election count
        election_counts = {
            'v20state': filtered_qs.filter(v20state="TRUE").count(),
            'v21town': filtered_qs.filter(v21town="TRUE").count(),
            'v21primary':filtered_qs.filter(v21primary="TRUE").count(),
            'v22general':filtered_qs.filter(v22general="TRUE").count(),
            'v23town':filtered_qs.filter(v23town="TRUE").count(),
        }
        # print(filtered_qs.filter(v20state=True).count())

        # get names and values for histagram
        labels = list(election_counts.keys())
        values = list(election_counts.values())

        bar_fig = go.Bar(x=labels, y=values)
        title_text = "Vote Count by Election"
        graph_div_bar = plotly.offline.plot({
            "data":[bar_fig],
            "layout_title_text":title_text,
        },
        auto_open=False,
        output_type="div")
        
        context['graph_div_hist'] = graph_div_hist
        context['graph_div_pie'] = graph_div_pie
        context['graph_div_bar'] = graph_div_bar
        return context




