from stat import FILE_ATTRIBUTE_READONLY
import pandas as pd
import json

dfe = pd.read_csv('static/data/consumos.csv',encoding='utf-8-sig',sep=";")
dfr = pd.read_csv('static/data/consumos_fr.csv',encoding='utf-8-sig',sep=";")

def edificios(i):
    if i == "fr":
        print("fr")
        df = dfr
    else:
        df = dfe
    edificios = []
    print(edificios)
    for i in range(len(df)):
        if df.loc[i][1] not in edificios:
            edificios.append(df.loc[i][1])
    newdf = pd.DataFrame()
    newdf['edificios'] = edificios
    return json.dumps(newdf.to_dict('records'))

def sel(edificio,i):
    if i == "fr":
        df = dfr
        filtro = df['EMPLACEMENT'] == edificio
    else:
        df = dfe
        filtro = df['UBICACIÓN'] == edificio
    filtrado = df[filtro]
    filtrado = filtrado.reset_index()
    data = filtrado.to_dict('records')
    get = json.dumps(data)
    return get

def selectmp(edificio,year,param,i):
    if i == "fr":
        df = dfr
        filtro = df['EMPLACEMENT'] == edificio
        filtrado = df[filtro]
        filtrado = filtrado.reset_index()
        newdf = pd.DataFrame()
        for i in range(len(filtrado)):
            print(filtrado.loc[i]['DATE DE LECTURE']);
            print(year)
            if str(filtrado.loc[i]['DATE DE LECTURE']).find(year) > 0:
                print("in year")
                dict = filtrado.loc[i].to_dict()
                newdf = newdf.append(dict,ignore_index=True)
        lastdf = newdf.filter(items=['DATE DE LECTURE',param])
    else:
        df = dfe
        filtro = df['UBICACIÓN'] == edificio
        filtrado = df[filtro]
        filtrado = filtrado.reset_index()
        newdf = pd.DataFrame()
        for i in range(len(filtrado)):
            print(filtrado.loc[i]['FECHA DE LECTURA']);
            print(year)
            if str(filtrado.loc[i]['FECHA DE LECTURA']).find(year) > 0:
                print("in year")
                dict = filtrado.loc[i].to_dict()
                newdf = newdf.append(dict,ignore_index=True)
        lastdf = newdf.filter(items=['FECHA DE LECTURA',param])
    return json.dumps(lastdf.to_dict('records'))

def param(i):
    if i == "fr":
        df = dfr
        columns = df.columns.values
        columns = list(columns)
        lista = ["N⁰ DE FACTURE","EMPLACEMENT","N⁰ DE COMPTEUR","DATE DE LECTURE",
        "AL ACTIVA HP",
        "AL EXPORT HP",
        "AL ACTIVA P",
        "AL EXPORT P",
        "AL REACTIVA HP",
        "AL REACTIVA P",
        "%AHP",
        "%AP",
        "%TRAFO",
        "%PRIMA",
        "%PENA",
        "check"]
        for l in lista:
            columns.remove(l)
    else:
        df = dfe
        columns = df.columns.values
        columns = list(columns)
        lista = ["Nº FACTURA","UBICACIÓN","Nº CONTADOR","FECHA DE LECTURA",
        "AL ACTIVA HP",
        "AL EXPORT HP",
        "AL ACTIVA P",
        "AL EXPORT P",
        "AL REACTIVA HP",
        "AL REACTIVA P",
        "%AHP",
        "%AP",
        "%TRAFO",
        "%PRIMA",
        "%PENA",
        "check"]
        for l in lista:
            columns.remove(l)
    return json.dumps(columns)

def repconsumo(edif,fecha,i):
    if i == "fr":
        df = dfr
        filtro = df['EMPLACEMENT'] == edif
        filtrado = df[filtro]
        filtrado = filtrado.reset_index()
        filtro = filtrado['DATE DE LECTURE'] == fecha
        filtrado = filtrado[filtro]
        filtrado = filtrado.reset_index()
        lista = ["SOUS-TOTAL DE L'ÉNERGIE ACTIVE HP","SOUS-TOTAL DE L'ÉNERGIE ACTIVE HP","LOCATION TRANSFORMATEUR","SOUS-TOTAL PRIME FIXE","SOUS-TOTAL SURPLUS DE PUISSANCE",'PÉNALITÉS FACTEUR DE PUISSANCE']
        lastdf = filtrado.filter(items=["SOUS-TOTAL DE L'ÉNERGIE ACTIVE HP","SOUS-TOTAL DE L'ÉNERGIE ACTIVE HP","LOCATION TRANSFORMATEUR","SOUS-TOTAL PRIME FIXE","SOUS-TOTAL SURPLUS DE PUISSANCE","PÉNALITÉS FACTEUR DE PUISSANCE"])
    else:
        df = dfe
        filtro = df['UBICACIÓN'] == edif
        filtrado = df[filtro]
        filtrado = filtrado.reset_index()
        filtro = filtrado['FECHA DE LECTURA'] == fecha
        filtrado = filtrado[filtro]
        filtrado = filtrado.reset_index()
        lista = ['SUBTOTAL ACTIVA HP','SUBTOTAL ACTIVA P','ALQUILER TRANSFORMADOR','SUBTOTAL PRIMA FIJA','SUBTOTAL EXCESO DE POTENCIA','PENALIZACION FP']
        lastdf = filtrado.filter(items=['SUBTOTAL ACTIVA HP','SUBTOTAL ACTIVA P','ALQUILER TRANSFORMADOR','SUBTOTAL PRIMA FIJA','SUBTOTAL EXCESO DE POTENCIA','PENALIZACION FP'])
    return json.dumps(lastdf.to_dict('records'))

def kpimed(edif,i):
    if i == "es":
        df = dfe
        filtro = df['UBICACIÓN'] == edif
        filtrado = df[filtro]
        filtrado = filtrado.reset_index()
        kpi = ['IMPORTE','CONSUMO ACTIVA HP','CONSUMO ACTIVA P','FACTOR DE POTENCIA','NUMERO DE HORAS UTILIZACION']
        lastdf = filtrado.filter(items=kpi)
        dict = {}
        dict[kpi[0]] = round(lastdf['IMPORTE'].mean(),2)
        dict[kpi[1]] = round(lastdf['CONSUMO ACTIVA HP'].mean(),2)
        dict [kpi[2]] = round(lastdf['CONSUMO ACTIVA P'].mean(),2)
        dict [kpi[3]] = round(lastdf['FACTOR DE POTENCIA'].mean(),2)
        dict [kpi[4]] = round(lastdf['NUMERO DE HORAS UTILIZACION'].mean(),2)
    else:
        df = dfr
        filtro = df['EMPLACEMENT'] == edif
        filtrado = df[filtro]
        filtrado = filtrado.reset_index()
        kpi = ['MONTANT',"CONSOMMATION DE L'ÉNERGIE ACTIVE HP","CONSOMMATION DE L'ÉNERGIE ACTIVE P",'FACTEUR DE PUISSANCE',"NOMBRE D'HEURES D'UTILISATION"]
        lastdf = filtrado.filter(items=kpi)
        dict = {}
        dict[kpi[0]] = round(lastdf['MONTANT'].mean(),2)
        dict[kpi[1]] = round(lastdf["CONSOMMATION DE L'ÉNERGIE ACTIVE HP"].mean(),2)
        dict [kpi[2]] = round(lastdf["CONSOMMATION DE L'ÉNERGIE ACTIVE P"].mean(),2)
        dict [kpi[3]] = round(lastdf['FACTEUR DE PUISSANCE'].mean(),2)
        dict [kpi[4]] = round(lastdf["NOMBRE D'HEURES D'UTILISATION"].mean(),2)
    return json.dumps(dict)

def kpi(edif,fecha,i):
    if i == "es":
        df = dfe
        filtro = df['UBICACIÓN'] == edif
        filtrado = df[filtro]
        filtrado = filtrado.reset_index()
        print("filtrado1",filtrado)
        filtro = filtrado['FECHA DE LECTURA'] == fecha
        filtrado = filtrado[filtro]
        filtrado = filtrado.reset_index()
        print("filtrado2",filtrado)
        kpi = ['IMPORTE','CONSUMO ACTIVA HP','CONSUMO ACTIVA P','FACTOR DE POTENCIA','NUMERO DE HORAS UTILIZACION']
        lastdf = filtrado.filter(items=kpi)
        print("lastdf",lastdf)
    else:
        df = dfr
        filtro = df['EMPLACEMENT'] == edif
        filtrado = df[filtro]
        filtrado = filtrado.reset_index()
        print(filtrado)
        filtro = filtrado['DATE DE LECTURE'] == fecha
        filtrado = filtrado[filtro]
        filtrado = filtrado.reset_index()
        print(filtrado)
        kpi =  ['MONTANT',"CONSOMMATION DE L'ÉNERGIE ACTIVE HP","CONSOMMATION DE L'ÉNERGIE ACTIVE P",'FACTEUR DE PUISSANCE',"NOMBRE D'HEURES D'UTILISATION"]
        lastdf = filtrado.filter(items=kpi)
        lastdf=lastdf.reset_index()
        print("lastdf",lastdf)
    return json.dumps(lastdf.to_dict('records'))

def maxpam(pam,i):
    if i == "fr":
        df = dfr
    else:
        df = dfe
    max = df.sort_values(by=[pam],ascending=False)
    max = max.reset_index()
    return str(max.loc[0][pam])

esto = kpi("AKWA PALACE NOUVEL IMMEUBLE","31-1-2019","fr")
print("kpi",esto)