#Fonction qui transforme des coordonnées ITRF2008 vers ITRF2020
#Différence des coordonnées pour la même station sous le même ITRF à des dates différentes
#Calcul de la vitesse de déplacement
#Fonction qui transforme des coordonnées ITRF2020 vers ETRF2020 (système européen où les vitesses sont théoriquement annulées)
#Différences des coordonnées pour la même station sous le même ETRF à des dates différentes
#Calcul de la vitesse de déplacement qui doit être nulle

from pyproj import Transformer
import pandas as pd
import maths

transformer08to20 = Transformer.from_crs("EPSG:7912", "EPSG:9140", always_xy=True)
transformerITtoET = Transformer.from_crs("EPSG:9140", "EPSG:9988", always_xy=True)

def it08TOit20(lon,lat,h) :
    return transformer08to20.transform(lon, lat, h)

def diffDates(coords_1, coords_2) :
    '''
        coords_15 : List -> Coordonnées lon, lat, h en ITRF 2020 de la station en 2015
        coords_20 : List -> idem pour la station en 2020
    '''
    diff_lon = maths.abs(coords_1[0] - coords_2[0])
    diff_lat = maths.abs(coords_1[1] - coords_2[1])
    diff_h = maths.abs(coords_1[2] - coords_2[2])

    return diff_lon, diff_lat, diff_h

def calculVitesse(diff, temps_annees) :
    '''
        diff : List -> Différences de longitude, latitude et hauteur
        temps_annees : Int -> delta de temps étudié
    '''
    return diff/temps_annees    #ça c'est pas bon, vu que diff est une liste, mais je ne sais pas trop comment gérer le truc

def it20TOet20(lon, lat, h) :
    return transformerITtoET.transform(lon, lat, h)


if __name__=='__main__' :

    path = 'D:\Documents\Garance_Geodesie\etude_tectonique_geodesie\calcul_station.csv'
    coords = pd.read_csv(path, sep = ';', header=none)







