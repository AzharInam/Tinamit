import os
import re
import csv
import numpy as np

class leer_datos(object):

    def __init__(símismo, nombre, archivo):
        símismo.n_csv = []
        símismo.nombre = nombre
        símismo.archivo = archivo
        símismo.min_max_dic = {}
        símismo.vars_interés = []

    def leer_egr_mds(símismo, archivo=None, var=None):
        if archivo is None:
            archivo = símismo.archivo

        datos = []

        with open(archivo) as d:
            lector = csv.reader(d)
            filas = [f for f in lector if re.match('{}(\[.*\])?$'.format(var), f[0])]

        for f in filas:
            datos.append(f[1:])

        return np.array(datos, dtype=float)

    def leer_csv_data(símismo, archivo=None, *args):

        if archivo is None:
            archivo = símismo.archivo

        var_interest =símismo.vars_interés = [*args]
        runs = {}


        símismo.n_csv = [x for x in os.listdir(archivo) if x.endswith('csv')]
        for v in var_interest:
            ind_runs = {}
            list_min = []
            list_max = []
            for i in símismo.n_csv:
                datos = leer_datos.leer_egr_mds(símismo, archivo=os.path.join(archivo, '{}'.format(i)), var=v)
                list_max.append(np.nanmax(datos))
                list_min.append(np.nanmin(datos))
                ind_runs[i] = datos
            runs[v] = ind_runs
            símismo.min_max_dic.update({v: (np.nanmax(list_max), np.nanmin(list_min))})
        return runs

