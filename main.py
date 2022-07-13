import pandas as pd
import numpy as np
import os
import scipy.stats as scipy
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Import Dataframe
fname = os.path.join(".\Base de datos Historica - Hoja 1.csv")
datos = pd.read_csv(fname)
#Eliminación de columnas no necesarias para construcción del modelo de predicción.
datos2 = datos.drop(['Cantidad de Horas por Turno','Req5: Numero de Iteraciones','Req6: Numero de Movimientos','Req7: Cantidad de Lista Tabu/Individiuos','Costo/Fitness','Tiempo en segundos','Acertividad en Costo'],axis=1)

#Renombrar columnas para mejor uso
datos2.rename(columns={'Req1: Horas diarias maximas por empleado' : 'Req1', 
                       'Req2: Tiempo de descanso minimo por empleado minutos' : 'Req2',
                       'Req3: Tiempo de descanso maximo por empleado minutos' : 'Req3',
                       'Req4: Dias libres al mes' : 'Req4',
                       'Turnos Mensuales' : 'Turnos'}, inplace = True)

# Datos de Entrada desde la interfaz de Usuario
def new_data_Empleados(data):
    final = np.reshape(data, (1,5))
    return(final)
def new_data_Turnos(data):
    final = np.reshape(data, (1,5))
    return(final)

# Creacion de los Inputs y Outputs para el Modelo con evaluacion de Empleados
def LogisticRegressionEmpleados(data):
    X = datos2[['Empleados','Req1','Req2','Req3','Req4']]
    y = datos2[['Algoritmo']].iloc[:,-1:].values.ravel()
    # Definir el Modelo
    model = LogisticRegression(solver='lbfgs')
    # Entrenar Modelo
    model.fit(X, y)
    # Crear la prediccion
    yhat = model.predict(X)
    # Evaluar la prediccion
    acc = accuracy_score(y, yhat)
    print("")
    print("")
    print("Exactitud del Modelo",acc)
    print("")
    print("")
    #Evaluar la prediccion con datos de entrada
    new_input = new_data_Empleados(data)
    print("Valores ingresados",new_input)
    print("")
    print("")
    new_output = model.predict(new_input)
    print("Modelo Heuristico Predicho",new_output)
    print("")
    print("")
    return new_output

# Creacion de los Inputs y Outputs para el Modelo con evaluacion de Turnos
def LogisticRegressionTurnos(data):
    X = datos2[['Turnos','Req1','Req2','Req3','Req4']]
    y = datos2[['Algoritmo']].iloc[:,-1:].values.ravel()
    # Definir el Modelo
    model = LogisticRegression(solver='lbfgs')
    # Entrenar Modelo
    model.fit(X, y)
    # Crear la prediccion
    yhat = model.predict(X)
    # Evaluar la prediccion
    acc = accuracy_score(y, yhat)
    print("")
    print("")
    print("Exactitud del Modelo",acc)
    print("")
    print("")
    #Evaluar la prediccion con datos de entrada
    new_input = new_data_Turnos(data)
    print("Valores ingresados",new_input)
    print("")
    print("")
    new_output = model.predict(new_input)
    print("Modelo Heuristico Predicho",new_output)
    print("")
    print("")
    return new_output