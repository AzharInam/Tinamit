import os
import datetime
from tinamit.Ejemplos.en.Ejemplo_SAHYSMOD import Plotting
from tinamit.Geog.Geog import Lugar, Geografía # need to import from tinamit

hoy = datetime.date.today().strftime("%d%m%Y")

#Rutas de acceso de archivo
base_dir = 'C:\\Users\\Azhar Inam\\PycharmProjects\\Tinamit\\tinamit\\Ejemplos\\en\\Ejemplo_SAHYSMOD\\Shape_files'
File_dir = 'C:\\Users\\Azhar Inam\\PycharmProjects\\Tinamit_old computer\\tinamit\\Ejemplos\\en\\Ejemplo_SAHYSMOD\\Vensim'
Map_dir = os.path.join('C:\\Users\\Azhar Inam\\Documents\\Tinamit_maps', 'Scenario_map_{}'.format(hoy))
try:
    if not os.path.exists(Map_dir):
        os.makedirs(Map_dir)
except OSError:
    print('Error: Creating directory. ' + Map_dir)


#El filtrado de los datos de interés variables
Haveli_Circle = Plotting.leer_datos(nombre='Haveli', archivo=File_dir)
simulación_datos = Haveli_Circle.leer_csv_data(File_dir, 'Soil salinity Tinamit CropA', 'Watertable depth Tinamit')

#Sitio de la geografía
Rechna_Doab = Geografía(nombre='Rechna Doab')

#Forma de archivos
Rechna_Doab.agregar_frm_regiones(os.path.join(base_dir, 'Internal_Polygon.shp'), col_id='Polygon_ID')
Rechna_Doab.agregar_forma(os.path.join(base_dir, 'External_Polygon.shp'), color='#edf4da')
Rechna_Doab.agregar_forma(os.path.join(base_dir, 'RIVR.shp'), tipo='agua', color='#41b2f4')
Rechna_Doab.agregar_forma(os.path.join(base_dir, 'CNL_Arc.shp'), tipo='agua', llenar=False, color='#4153f4')
# Rechna_Doab.agregar_forma(os.path.join(base_dir, 'Forst_polygon.shp'), tipo='bosque')
Rechna_Doab.agregar_forma(os.path.join(base_dir, 'buildup_Polygon.shp'), tipo='ciudad')
#Rechna_Doab.agregar_forma(os.path.join(base_dir, 'road.shp'), tipo='calle')

#variable de interés para la asignación de
vars_interés = {Haveli_Circle.vars_interés[0]: {'col': ['#00CC66', '##FFCC66', '#FF431D'],'escala_núm': [Haveli_Circle.min_max_dic[Haveli_Circle.vars_interés[0]][0], Haveli_Circle.min_max_dic[Haveli_Circle.vars_interés[0]][1]]},
                Haveli_Circle.vars_interés[1]: {'col':['#FF6666', '#FFCC66', '#00CC66'],'escala_núm': [Haveli_Circle.min_max_dic[Haveli_Circle.vars_interés[1]][0], Haveli_Circle.min_max_dic[Haveli_Circle.vars_interés[1]][1]]}}

#número de pasos
n_paso = simulación_datos[Haveli_Circle.vars_interés[0]][Haveli_Circle.n_csv[0]].shape[1]

#trazado
for v, d in vars_interés.items():
    for y in Haveli_Circle.n_csv:
        for i in range(n_paso):
            valores = simulación_datos[v][y][:, i]
            if i % 2 == 0:
                X = int(1990 + i / 2)
                SS = 'Season 1'
            else:
                SS = 'Season 2'

            Rechna_Doab.dibujar(archivo=os.path.join(Map_dir, '{}_{}_{}.png'.format(v, y[:3]+y[8], X)),
                                valores=valores,
                                título='{}_{}_{}_{}'.format(v, y[:3]+y[8], X, SS),
                                unidades='', colores=d['col'], escala_num=d['escala_núm']
                                )
