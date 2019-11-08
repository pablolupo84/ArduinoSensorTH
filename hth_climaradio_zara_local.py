import time
import serial

device_serie=serial.Serial('COM4')
lectura=device_serie.readline()

#lectura="hhhh tttt ffff\n"
#lectura="22.44 66.77 44.66\n"
lectura.rstrip('\n')

datos_lista=lectura.split();

hum=datos_lista[0]
temp_c=datos_lista[1]
temp_f=datos_lista[2]

f=open("c:\\ClimaRadio\\Zara\\Tiempo-plantilla.html")
salida=open("c:\\ClimaRadio\\Zara\\Tiempo.html", "w")
for line in f:
	salida.write(line.replace("%t",temp_c).replace("%h",hum).replace("%f",temp_f))
f.close()
salida.close()
print ("Se actualizo el archivo Zara de ClimaRadio")
#time.sleep(600)
