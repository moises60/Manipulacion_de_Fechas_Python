import tkinter as tk
from tkinter import messagebox, ttk
from fecha import Fecha

def mostrar_fecha():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        año = int(entry_año.get())
        fecha = Fecha(dia, mes, año)
        lbl_resultado.config(text=f"Fecha: {fecha}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def incrementar_fecha():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        año = int(entry_año.get())
        fecha = Fecha(dia, mes, año)
        fecha.incrementar_dia()
        lbl_resultado.config(text=f"Fecha incrementada: {fecha}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def decrementar_fecha():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        año = int(entry_año.get())
        fecha = Fecha(dia, mes, año)
        fecha.decrementar_dia()
        lbl_resultado.config(text=f"Fecha decrementada: {fecha}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def comparar_fechas():
    try:
        dia1 = int(entry_dia.get())
        mes1 = int(entry_mes.get())
        año1 = int(entry_año.get())
        fecha1 = Fecha(dia1, mes1, año1)
        
        dia2 = int(entry_dia2.get())
        mes2 = int(entry_mes2.get())
        año2 = int(entry_año2.get())
        fecha2 = Fecha(dia2, mes2, año2)
        
        if Fecha.son_iguales(fecha1, fecha2):
            resultado = "Las fechas son iguales."
        elif Fecha.es_posterior(fecha1, fecha2):
            resultado = "La primera fecha es posterior a la segunda."
        else:
            resultado = "La primera fecha es anterior a la segunda."
        
        lbl_resultado.config(text=resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def calcular_diferencia():
    try:
        dia1 = int(entry_dia.get())
        mes1 = int(entry_mes.get())
        año1 = int(entry_año.get())
        fecha1 = Fecha(dia1, mes1, año1)
        
        dia2 = int(entry_dia2.get())
        mes2 = int(entry_mes2.get())
        año2 = int(entry_año2.get())
        fecha2 = Fecha(dia2, mes2, año2)
        
        diferencia_dias = Fecha.diferencia(fecha1, fecha2)
        lbl_resultado.config(text=f"Diferencia en días: {diferencia_dias} días")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

def generar_fecha_aleatoria():
    fecha = Fecha.fecha_aleatoria()
    lbl_resultado.config(text=f"Fecha aleatoria: {fecha}")

root = tk.Tk()
root.title("Manipulación de Fechas")
root.geometry("500x450")

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#ccc")
style.configure("TLabel", padding=6)

frame_principal = ttk.Frame(root, padding="10")
frame_principal.pack(fill="both", expand=True)

frame_fecha1 = ttk.Labelframe(frame_principal, text="Fecha 1", padding="10")
frame_fecha1.pack(fill="x", padx=10, pady=10)

tk.Label(frame_fecha1, text="Día:").grid(row=0, column=0, padx=5, pady=5)
entry_dia = tk.Entry(frame_fecha1)
entry_dia.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_fecha1, text="Mes:").grid(row=1, column=0, padx=5, pady=5)
entry_mes = tk.Entry(frame_fecha1)
entry_mes.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_fecha1, text="Año:").grid(row=2, column=0, padx=5, pady=5)
entry_año = tk.Entry(frame_fecha1)
entry_año.grid(row=2, column=1, padx=5, pady=5)

frame_fecha2 = ttk.Labelframe(frame_principal, text="Fecha 2", padding="10")
frame_fecha2.pack(fill="x", padx=10, pady=10)

tk.Label(frame_fecha2, text="Día:").grid(row=0, column=0, padx=5, pady=5)
entry_dia2 = tk.Entry(frame_fecha2)
entry_dia2.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_fecha2, text="Mes:").grid(row=1, column=0, padx=5, pady=5)
entry_mes2 = tk.Entry(frame_fecha2)
entry_mes2.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_fecha2, text="Año:").grid(row=2, column=0, padx=5, pady=5)
entry_año2 = tk.Entry(frame_fecha2)
entry_año2.grid(row=2, column=1, padx=5, pady=5)

frame_acciones = ttk.Frame(frame_principal, padding="10")
frame_acciones.pack(fill="x", padx=10, pady=10)

btn_mostrar = ttk.Button(frame_acciones, text="Mostrar Fecha 1", command=mostrar_fecha)
btn_mostrar.grid(row=0, column=0, padx=5, pady=5)

btn_incrementar = ttk.Button(frame_acciones, text="Incrementar Día", command=incrementar_fecha)
btn_incrementar.grid(row=0, column=1, padx=5, pady=5)

btn_decrementar = ttk.Button(frame_acciones, text="Decrementar Día", command=decrementar_fecha)
btn_decrementar.grid(row=0, column=2, padx=5, pady=5)

btn_comparar = ttk.Button(frame_acciones, text="Comparar Fechas", command=comparar_fechas)
btn_comparar.grid(row=1, column=0, padx=5, pady=5)

btn_diferencia = ttk.Button(frame_acciones, text="Calcular Diferencia", command=calcular_diferencia)
btn_diferencia.grid(row=1, column=1, padx=5, pady=5)

btn_aleatoria = ttk.Button(frame_acciones, text="Fecha Aleatoria", command=generar_fecha_aleatoria)
btn_aleatoria.grid(row=1, column=2, padx=5, pady=5)

lbl_resultado = ttk.Label(frame_principal, text="", background="#eee", relief="solid", anchor="center")
lbl_resultado.pack(fill="x", padx=10, pady=10)

root.mainloop()
