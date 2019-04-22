from custom_functions import temperature

Guajira={"Enero":33, "Febrero":33, "Marzo":35, "Abril":36, "Mayo":37, "Junio":38, "Julio":37, "Agosto":39, "Septiembre":42,"Octubre":37, "Noviembre":36, "Diciembre":34}
Narino={"Enero":25, "Febrero":25, "Marzo":25, "Abril":25, "Mayo":25, "Junio":25, "Julio":25, "Agosto":28, "Septiembre":29,"Octubre":25, "Noviembre":24, "Diciembre":24}
Santander={"Enero":27, "Febrero":27, "Marzo":27, "Abril":27, "Mayo":27, "Junio":27, "Julio":27, "Agosto":27, "Septiembre":27,"Octubre":27, "Noviembre":26, "Diciembre":31}

x= temperature.prom(Guajira.values())
y= temperature.prom(Narino.values())
z= temperature.prom(Santander.values())
print("El promedio de temperatura de la Guajira es: ", x)
print("El promedio de temperatura de Nariño es: ", y)
print("El promedio de temperatura de Santander es:", z)

print("-----------------")

nacional=[temperature.prom(Guajira.values()) + temperature.prom(Narino.values()) + temperature.prom(Santander.values())]
nacional_final=(temperature.prom(nacional))/3
print("El promedio de la temperatura a nivel nacional es: ", nacional_final)

print("-----------------")
print("La temperatura mayor regitrada en La Guajira fue en el mes de: " ,max(Guajira,key=Guajira.get),max(Guajira.values()),"°C")
print("La temperatura mayor regitrada en Nariño fue en el mes de: " ,max(Narino,key=Narino.get),max(Narino.values()),"°C")
print("La temperatura mayor regitrada en Santader fue en el mes de: " ,max(Santander,key=Santander.get),max(Santander.values()),"°C")

print("-----------------")
suma = 0
for i in range (1,4):
    if i==1:
        a=float(input("Ingrese la temperatura mayor de Guajira: "))
        suma= suma+a
    if i==2:
        a = float(input("Ingrese la temperatura mayor de Nariño: "))
        suma = suma + a
    if i==3:
        a = float(input("Ingrese la temperatura mayor de Santander: "))
        suma = suma + a
final=suma/3
print("El promedio de la tmepratura de los tres mese mas calientes es: ",final)


print("----------------")

promedios=[x,y,z]
print("El promedio mas caliente es: ", max(x,y,z))

print("----------------")

MaxGuajira= max(Guajira.values())
MaxNarino= max(Narino.values())
MaxSantander= max(Santander.values())

if MaxGuajira > MaxNarino and MaxGuajira > MaxSantander:
    print("La mayor temperatura se encuentra en La Guajira ", max(Guajira,key=Guajira.get),max(Guajira.values()),"°C")

if MaxNarino > MaxGuajira and MaxNarino > MaxSantander:
    print("La mayor temperatura se encuentra en Nariño ",max(Narino,key=Narino.get),max(Narino.values()),"°C" )

if MaxSantander > MaxGuajira and MaxSantander > MaxNarino:
    print("La myor temperatura se encuentra en Santander ", max(Santander,key=Santander.get),max(Santander.values()),"°C")

print("----------------")


print("Desviacion estandar", temperature.desviacion_estandar(Guajira.values()))
print("Desviacion estandar", temperature.desviacion_estandar(Narino.values()))
print("Desviacion estandar", temperature.desviacion_estandar(Santander.values()))



