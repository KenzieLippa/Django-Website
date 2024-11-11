from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from . models import Voter
# Create your views here.


class VoterListView(ListView):
    '''a view to display the voter lists'''
    template_name = "voter_analytics/voter.html"
    model = Voter
    context_object_name = "voters"
    paginate_by = 100

    def get_queryset(self):
        qs = super().get_queryset().order_by('last_name')
        #filter results
        print(Voter.objects.values_list('party_affiliation', flat=True).distinct())
        # check the get request
        if self.request.GET:
            print(self.request.GET)
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
