"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import numpy as np

def ingest_data():

    #
    # Inserte su código aquí
    #
    
    
    df=pd.read_fwf('clusters_report.txt',
                    on_bad_lines='skip',
                    #colspecs="infer",
                    #names=column_names,
                     widths=[9, 15, 15,80])
    df.columns=('cluster', 'cantidad de palabras clave', 'porcentaje de palabras clave', 'principales palabras clave')

    df=df.drop([0, 1],axis=0).reset_index(drop=True)
    prueba=[]
    prueba.append(['cluster'])
    prueba.append(['cantidad de palabras clave'])
    prueba.append(['porcentaje de palabras clave'])
    prueba.append(['principales palabras clave'])
    aux=0
    df = pd.DataFrame(df)
    

    for i in range(len(df['cluster'])):

        if pd.isna(df['cluster'][i]):
            prueba[3][aux].extend([df['principales palabras clave'][i]])

        else:
            aux+=1
            prueba[0].extend([int(df['cluster'][i])])
            prueba[1].extend([int(df['cantidad de palabras clave'][i])])
            prueba[2].extend([float(df['porcentaje de palabras clave'][i].replace(' %','').replace(',','.'))])
            prueba[3].extend([[df['principales palabras clave'][i]]])
    
    df = pd.DataFrame(prueba)
    df=df.transpose() 
    df.columns=('cluster', 'cantidad de palabras clave', 'porcentaje de palabras clave', 'principales palabras clave')
    df=df.drop([0],axis=0).reset_index(drop=True)
    aux=0;

    for i in df['principales palabras clave']:
        df['principales palabras clave'][aux]=' '.join(i)
        aux+=1
    #print(df['principales palabras clave'][0])
    aux=0
    for i in df['principales palabras clave']:
        xx=i.replace('       ',' ')
        xx=i.replace('      ',' ')
        xx=i.replace('     ',' ')
        xx=xx.replace('    ',' ')
        xx=xx.replace('   ',' ')
        xx=xx.replace('  ',' ')
        xx=xx.replace('.','')
        df['principales palabras clave'][aux]= xx
        
        aux+=1
    df.columns=('cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave')
    return df
ingest_data()  
