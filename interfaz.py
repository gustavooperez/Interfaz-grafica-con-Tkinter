import tkinter as tk
import RPi.GPIO as GPIO
import time
#---Configuracion de la Raspberry
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#---Pines a utilizar
motor = 12  #PWM del motor
A = 20      #Control de giro
B = 21      #Control de giro
servo = 6   #PWM del servomotor
led_rojo = 22   #PWM LED RGB rojo
led_verde = 27  #PWM LED RGB verde
led_azul = 17   #PWM LED RGB azul
trig = 23   #trigger ultrasonico
echo = 24   #echo ultrasonico
#---Establecer entradas, salidas y PWM
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(servo,GPIO.OUT)
servo = GPIO.PWM(6, 50)
servo.start(0)
GPIO.setup(motor,GPIO.OUT)
GPIO.setup(A,GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
motor = GPIO.PWM(12, 50)
motor.start(0)
GPIO.setup(led_rojo,GPIO.OUT)
GPIO.setup(led_verde,GPIO.OUT)
GPIO.setup(led_azul,GPIO.OUT)
led_rojo = GPIO.PWM(22, 50)
led_rojo.start(100)
led_verde = GPIO.PWM(27, 50)
led_verde.start(100)
led_azul = GPIO.PWM(17, 50)
led_azul.start(100)

#---Funciones
def ultrasonico():
    GPIO.output(trig, False)
    time.sleep(0.1)
    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig,False)
    inicio = time.time()
    while GPIO.input(echo) == 0:
        inicio=time.time()
    while GPIO.input(echo) == 1:
        final = time.time()
    tiempo = final - inicio
    distancia = tiempo*34000
    distancia = distancia/2
    l2.configure(text=str(distancia))
    fr.after(100, ultrasonico)
def servomotor(s):
    angulo = var3.get()
    p_grados = float (angulo) * (5/9)
    t_pulso = ((p_grados) * 0.002) / 100
    duty = (((t_pulso) / 0.02) * 100) + 1
    servo.ChangeDutyCycle(duty)
def control(c):
    duty = pwm.get()
    motor.ChangeDutyCycle(duty)
def avanza():
    pass
    GPIO.output(A,True)
    GPIO.output(B,False)
def reversa():
    pass
    GPIO.output(A,False)
    GPIO.output(B,True)
def rojo(r):
    duty = var.get()
    duty = abs((duty-255)*(20/51))
    led_rojo.ChangeDutyCycle(duty)
def verde(v):
    duty = var1.get()
    duty = abs((duty-255)*(20/51))
    led_verde.ChangeDutyCycle(duty)
def azul(a):
    duty = var2.get()
    duty = abs((duty-255)*(20/51))
    led_azul.ChangeDutyCycle(duty)
def limpiar():
    pass
    GPIO.cleanup()

#---Interfaz grafica
w = tk.Tk()
w.title('Interfaz Grafica')
w.geometry('450x500')
w.config(bg='azure2')
fr = tk.Toplevel(w)
fr.geometry('200x250')
fr.title('Ultrasonico')
l1=tk.Label(fr, text='Distancia', bg='black', fg='white')
l1.grid(row=0, column=0)
l2=tk.Label(fr, text='0', bg ='black', fg='white')
l2.grid(row=0, column=1)
b1=tk.Button(fr, text='Inicio', command = ultrasonico)
b1.grid(row=1, column=0)


l3=tk.Label(w, text='GRADOS', bg='gold2',borderwidth=10, width=8)
l3.grid(row=0, column=0, padx=10)
var3=tk.IntVar()
s4=tk.Scale(w, from_=0, to=180, orient=tk.HORIZONTAL, bg='gold2', length=210, variable=var3, command=servomotor)
s4.grid(row=0,column=1, columnspan=3, pady=3)

var = tk.IntVar()
var1 = tk.IntVar()
var2 = tk.IntVar()
l4=tk.Label(w, text='LED ROJO', bg='red3', font=('Arial', 10))
l4.grid(row=1,column=1, padx=5)
s1=tk.Scale(w, from_=0, to=255, bg='red3',width=30, length=200, variable = var, command=rojo)
s1.grid(row=2,column=1)
l5=tk.Label(w, text='LED VERDE', bg='green', font=('Arial', 10))
l5.grid(row=1,column=2, padx=5)
s2=tk.Scale(w, from_=0, to=255, bg='green',width=30, length=200, vari = var1, command=verde)
s2.grid(row=2,column=2)
l6=tk.Label(w, text='LED AZUL', bg='blue', font=('Arial', 10))
l6.grid(row=1,column=3, padx=5)
s3=tk.Scale(w, from_=0, to=255, bg='blue',width=30, length=200, varia = var2, command = azul)
s3.grid(row=2,column=3)
b2=tk.Button(w, text='Limpiar',command=limpiar)
b2.place(x=370, y=100)
b3=tk.Button(w, text='Salir',command= w.destroy)
b3.place(x=370, y=150)

l7 = tk.Label(w, text='MOTOR DC', bg = 'cyan',borderwidth=10, width=8)
l7.grid(row = 3,column=0, padx=10)
var4 = tk.IntVar()
pwm = tk.IntVar()
s1 = tk.Scale(w,from_=0,to = 100, orient=tk.HORIZONTAL,bg='cyan', length=210, variab = pwm, command=control)
s1.grid(row=3,column=1, columnspan=3)
r1 = tk.Radiobutton(w, text = 'Avanza', variable = var4, value = 1, command = avanza)
r1.grid(row =5, column=1,pady=5)
r2 = tk.Radiobutton(w, text = 'Reversa', variable = var4, value = 2, command = reversa)
r2.grid(row =5, column=3)


w.mainloop()







