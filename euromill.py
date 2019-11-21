import pandas as pd

# Use this function on premise if there is no data#
def actualizarlista():
    '''Función que toma todos los números, incluido el último, de los resultados
        de los sorteos y los mete en Resultados_base.csv'''
    print("Recuperando datos de Google spreadsheet")
    ref = "https://docs.google.com/spreadsheet/pub?key=0AhqMeY8ZOrNKdEFUQ3VaTHVpU29UZ3l4emFQaVZub3c&amp"
    tabla = pd.read_html(ref, header=0, parse_dates=True)
    t = pd.DataFrame(tabla[0])
    print(t.head(5))
    t.drop(t.index[0], inplace=True, axis=0)  # quitamos la fila 0, ya que no hay datos
    t.drop(['Unnamed: 0'], inplace=True, axis=1)  # quitamos la columna 1, no necesario
    t.drop(['Unnamed: 7'], inplace=True, axis=1)  # quitamos la columna 7, no necesaria
    enca = ['FECHA', 'N1', 'N2', 'N3', 'N4', 'N5', 'Star1', 'Star2']
    t.columns = enca  # redefinimos las columnas
    # falta pasarlos a enteros
    print(t.head())
    t.drop(t.index[0], inplace=True, axis=0)
    t.to_csv('Resultados_base.csv')
    print("\nGuardado en Resultados_base.csv\n")


class EuroMill:

    def __init__(self):
        self.data_frame = self.get_data()

    def version(self):
        print('version 09/11/2019')

    def get_data(self):
        '''Función para cargar los datos en un Dataframe'''
        datos = pd.read_csv("Resultados_base.csv", parse_dates=True)
        df = pd.DataFrame(datos)
        df.set_index('FECHA', inplace=True, drop=True)
        df.drop(['Unnamed: 0'], inplace=True, axis=1)
        return df

    def BackUp_datos(self):
        '''Función para guardar los datos en un backup de respaldo'''
        print("Actualizando datos...")
        self.get_data()
        print("Cargando datos...")
        dataframe = self.get_data()
        dataframe.to_csv("ResultadosBackup.csv")
        print("\nGuardado en ResultadosBackup.csv\n")

    def analise_data(self):
        ''' Función para saber el peso de cada número en cada columna'''
        n1 = self.data_frame.N1.values
        n2 = self.data_frame.N2.values
        n3 = self.data_frame.N3.values
        n4 = self.data_frame.N4.values
        n5 = self.data_frame.N5.values
        st1 = self.data_frame.Star1.values
        st2 = self.data_frame.Star2.values
        print(st2, type(st2), len(st2))
        numero = st2
        l = len(numero)
        if max(numero) <= 12:
            n = [i for i in range(1, 13)]
        else:
            n = [i for i in range(1, 51)]
        popu = []
        weights = []
        for i in n:
            count = 0
            for j in numero:
                if i == j:
                    count += 1
            w = 100 * (count / float(l))
            # print(i,'encontrado',count,'times','weight',w)
            popu.append(i)
            weights.append(round(w))

        print(popu, weights)


def test():
    eur1 = EuroMill()
    df = eur1.get_data()
    print(eur1.analise_data())


test()