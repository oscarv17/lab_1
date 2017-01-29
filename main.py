# Laboratorio 1 Ciencias de Datos
# ============
# Oscar Valecillos 22343034

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('C:\Users\Oscar\Desktop\student\student-por.csv',sep=';')


# ### -Propiedades de los datos

data.describe()


# ###  -Histograma del tiempo libre de los estudiantes


data['freetime'].plot(kind="hist",title="Tiempo Libre")


# ### -Diagrama de dispersion entre el numero de clases fallidas y las notas finales


notas=data['G3']
fallas=data['failures']
plt.scatter(fallas,notas)
plt.ylabel('Notas finales')
plt.xlabel('Clases fallidas')


# #### Hipotesis
# Como podemos ver, el diagrama tiene un comportamiento decreciente, con esto podemos presentar la siguiente hipotesis: mienstras mayor sea el numero de clases fallidas, las notas finales seran menores e iran disminuyendo, con base en esto podemos decir que existe una correlacion negativa entre las variables

# ### -Explore, usando lo aprendido en el laboratorio, los datos provistos


data['G1'].max() #valor maximo del primer periodo


data['G2'].median() #valor medio del segundo periodo


data['G3'].min() #valor minimo del tercer periodo


data['studytime'].value_counts() #retorna el numero de repeticiones de cada elemento


(data['G3']==3).any() #verificamos si existe algun estudiante con una nota igual a 3 en el periodo 3


data['absences'].plot(kind="hist",title="Ausencias") #histograma de ausencias


# ### -Plantee al menos 3 preguntas sobre que puedan ser respondidas con los datos provistos y postule el codigo (o algoritmo) necesario para responderla

# a. numero de estudiantes femeninos que su tiempo de estudio sea de 5 a 10 horas

f=data[data['sex']=='F']
tiempEstudio=f[f['studytime']==3]
tiempEstudio['sex'].count()


# b. edad promedio de alumnos con ayuda educativa

sup=data[data['schoolsup']=='yes']
sup['age'].mean()


# c. promedio de notas del primer periodo de los estudiantes que no tienen una relacion romantica

single=data[data['romantic']=='no']
single['G1'].mean()

