from django.db import models

# Create your models here.
class Voter(models.Model):
    '''store and represent the various fields assosciated with voters
    start with our fields and then we define our other methods'''

    # voter data

    #name
    # need a toss field?
    voterID = models.TextField()
    last_name = models.TextField()
    first_name = models.TextField()

    #address
    street_num = models.IntegerField()
    street_name = models.TextField()
    apartment_num = models.TextField()
    zip_code = models.IntegerField()

    #dates
    birthdate = models.DateField()
    registration_date = models.DateField()

    #other
    party_affiliation = models.CharField(max_length=1)
    precinct_num = models.IntegerField()

    #vote frequents
    v20state = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()

    voter_score = models.IntegerField()

def load_data():
    '''read in all the stuff and put it in its field
    '''
    Voter.objects.all().delete()
    filename = 'C:/Users/rosey/Downloads/newton_voters.csv'
    f = open(filename)
    f.readline() #discards the headers

    for line in f:
        # line = f.readline().strip()
        fields = line.split(',')

        try:
            #create a new instance of result object with this record
            res = Voter(voterID = fields[0],
                        last_name = fields[1],
                        first_name = fields[2], 
                        street_num = fields[3],
                        street_name = fields[4],
                        apartment_num = fields[5],
                        zip_code = fields[6],
                        birthdate = fields[7],
                        registration_date = fields[8],
                        party_affiliation = fields[9].strip(),
                        precinct_num = fields[10],
                        v20state = fields[11],
                        v21town = fields[12],
                        v21primary = fields[13],
                        v22general = fields[14],
                        v23town = fields[15],
                        voter_score = fields[16],
                        )
            res.save() #commit to database
            print(f'Created result: {res}')
        except:
            print(f"skipped: {fields}")
    print(f'Done. Created {len(Voter.objects.all())} Voters')





