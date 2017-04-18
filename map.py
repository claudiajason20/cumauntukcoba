import pandas as pd
import vincent as vi
import numpy as np

country_data_tmp = pd.DataFrame({'country_names' : np.array(['Anguilla','Antigua','Argentina','Aruba','Bahamas','Barbados','Belize','Bermuda','Bolivia','BritishVigin','Canada','Cayman','Chile','Colombia','CostaRica','Cuba','Curacao','Dominica','Dominican','Ecuador','Elsavador','Falkland','Greenland','Grenada','Guatemala','Guyana','Haiti','Honduras','Jamaica','Mexico','Montserrat','Nicaragua','Panama','Paraguay','Peru','PuoertoRico','SaintBarthelemy','SaintKitts','SaintLucia','SaintMartin','SaintPierre','SaintVincent','SintMaarten','Suriname','Trinidad','Turks','USA','USVirgin','Uruguay','Venezuela']),
                                 'country_alpha3' : np.array(['AIA','ATG','ARG','ABW','BHS','BRB','BLZ','BMU','BOL','VGB','CAN','CYM','CHL','COL','CRI','CUB','CUW','DMA','DOM','ECU','SLV','FLK','GRL','GRD','GTM','GUY','HTI','HND','JAM','MEX','MSR','NIC','PAN','PRY','PER','PRI','BLM','KNA','LCA','MAF','SPM','VCT','SXM','SUR','TTO','TCA','USA','VIR','URY','VEN'])})
country_data_tmp.head()

#map drawing bit Input[2] from your notebook
#Note the changes in variable names

world_topo = r'world-countries.topo.json'
geo_data = [{'name': 'countries',
      	     'url': world_topo,
             'feature': 'world-countries'}]

vis = vi.Map(data=country_data_tmp,
            	  geo_data=geo_data,
                scale=1100,
                data_key='country_alpha3',
                map_key={'countries': 'id'})

vis.display()
