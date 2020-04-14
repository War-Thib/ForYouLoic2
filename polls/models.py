from django.db import models


class Pharmacie(models.Model):
    pharmacie_name = models.CharField(max_length=30, primary_key=True)
    pharmacie_adress = models.CharField(max_length=30, blank=True, null=True)
    COMMUNE_CHOICE = [('ixelles', 'Ixelles'),
                      ('eterbeek', 'Eterbeek'),
                      ('uccle', 'Uccle'),
                      ('bruxelles', 'Bruxelles'),
                      ('anderlecht', 'anderlecht'),
                      ('ganshoren', 'Ganshoren'),
                      ('jette', 'Jette'),
                      ('berchem-Sainte-Agathe', 'Berchem-Sainte-Agathe'),
                      ('saint-Gilles', 'Saint-Gilles'),
                      ('molenbeek-Saint-Jean', 'Molenbeek-Saint-Jean'),
                      ('saint-Josse-ten-Noode', 'Saint-Josse-ten-Noode'),
                      ( 'woluwe-Saint-Lambert' ,  'Woluwe-Saint-Lambert '),
                      ('woluwe-Saint-Pierre', 'Woluwe-Saint-Pierre'),
                      ( 'watermael-Boitsfort',  'Watermael-Boitsfort'),
                      ('audergem', 'Audergem'),
                      ('evere', 'Evere'),
                      ('schaerbeek', 'Schaerbeek'),
                      ('koekelberg', 'Koekelberg')
                      ]
    pharmacie_ville = models.CharField(max_length=30, blank=True, null=True, default='Bruxelles')
    pharmacie_commune = models.CharField(max_length= 30, choices= COMMUNE_CHOICE, blank= True, null = True)
    pharmacie_email = models.EmailField(max_length= 254, blank=True, null= True)





