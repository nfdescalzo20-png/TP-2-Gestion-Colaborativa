
import pandas as pd #Importa la biblioteca de pandas, para el analisis del DataSet.
import matplotlib.pyplot as plt #Importa la biblioteca de matplotlib, para la elaboracion del grafico.

df = pd.read_csv("datos/dataset.csv", parse_dates=['sales_date'])

total_ventas = df["sales_amount"].sum() #Calcula la suma los valores en la columna sales_amount
promedio_diario = df["sales_amount"].mean() #Calcula la Media de los valores en la columna sales_amount

pos_max = df["sales_amount"].idxmax() #Variable con posicion del mayor valor en la columna de sales_amount
monto_max = df.loc[pos_max, "sales_amount"] #Variable con mayores ventas de la columna sales_amount
dia_mayor_venta = df.loc[pos_max, "sales_date"].strftime("%d/%m/%Y") #Variable con la fecha (en la columna sales_date) en la misma posicion que que la mayor venta en sales_amount

pos_min = df["sales_amount"].idxmin() #Variable con posicion del menor valor en la columna de sales_amount
monto_min = df.loc[pos_min, "sales_amount"] #Variable con menores ventas de la columna sales_amount
dia_menor_venta = df.loc[pos_min, "sales_date"].strftime("%d/%m/%Y") #Variable con la fecha (en la columna sales_date) en la misma posicion que que la menor venta en sales_amount

mes = df["sales_date"].dt.to_period("M") #Convierte las fechas de la columna sales_date del formato AAAA-MM-DD al formato AAAA-MM
ventas_por_mes = df.groupby(mes)["sales_amount"].sum().reset_index() #Agrupa los datos del DataSet por mes y suma los valores de la columna de sales_amount

print("INDICADORES DE VENTAS") #Imprime por pantalla los indicadores
print(f"Ventas totales: ${total_ventas:,.0f}")
print(f"Promedio diario: ${promedio_diario:,.0f}")
print(f"Día mayor venta: {dia_mayor_venta} (${monto_max:,.0f})")
print(f"Día menor venta: {dia_menor_venta} (${monto_min:,.0f})")
print(f"Ventas por mes: {ventas_por_mes.to_string(index=False)}")

fig, ax = plt.subplots(figsize=(8, 5))
ventas_por_mes.plot(kind="bar", ax=ax) #Utiliza los datos de la variable ventas_por_mes para dibujar un grafico de barras
ax.set_title("Evolución de Ventas Mensuales - 2024") #Titulo del grafico
ax.set_xlabel("Mes") #Titulo de la barra horizontal (x)
ax.set_ylabel("Ventas ($)") #Titulo de la barra vertical (y)
ax.set_xticklabels(range(1, 13), rotation=0) #Define cada barra con un numero del 1 al 12, en referencia a los meses analizados
plt.tight_layout() #Ajusta automáticamente los márgenes para que ningún texto (como el nombre de los ejes) se corte o quede fuera de la imagen
plt.savefig("resultados/" + "grafico_ventas_mensuales.png", dpi=150) #Guarda el resultado en la carpeta resultados del repositorio
