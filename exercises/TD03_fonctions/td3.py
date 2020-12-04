#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    temps = (((temps[0] * 24 + temps[1]) * 60 + temps[2]) * 60 + temps[3])
    pass 

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (temps[3] // 60 + temps[3] % 60jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
   temps[2] = temps[3] // 60 + temps[3] % 60
   temps[1] = temps[2] // 60 + temps[2] % 60
   temps[0] = temps[1] // 24 + temps[1] % 24
    pass 
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")