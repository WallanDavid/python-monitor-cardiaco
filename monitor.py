import tkinter as tk
from tkinter import messagebox
import random
import time
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

class MonitorAtividadeFisicaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor de Atividade Física")

        self.label = tk.Label(root, text="Bem-vindo ao Monitor de Atividade Física!")
        self.label.pack(pady=10)

        self.button_start = tk.Button(root, text="Iniciar Monitoramento", command=self.iniciar_monitoramento)
        self.button_start.pack(pady=10)

        self.button_stop = tk.Button(root, text="Parar Monitoramento", command=self.parar_monitoramento, state=tk.DISABLED)
        self.button_stop.pack(pady=10)

        self.button_export = tk.Button(root, text="Exportar Dados", command=self.exportar_dados, state=tk.DISABLED)
        self.button_export.pack(pady=10)

        self.progress_bar = ttk.Progressbar(root, length=200, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.fig, self.ax = plt.subplots(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

        self.monitoramento_ativo = False

    def iniciar_monitoramento(self):
        self.label.config(text="Monitoramento Iniciado!")
        self.button_start.config(state=tk.DISABLED)
        self.button_stop.config(state=tk.NORMAL)
        self.button_export.config(state=tk.DISABLED)

        self.monitoramento_ativo = True

        # Simulação de aquisição de dados
        self.simular_dados()

    def parar_monitoramento(self):
        self.label.config(text="Monitoramento Parado.")
        self.button_start.config(state=tk.NORMAL)
        self.button_stop.config(state=tk.DISABLED)
        self.button_export.config(state=tk.NORMAL)

        self.monitoramento_ativo = False

    def exportar_dados(self):
        # Exporta os dados simulados para um arquivo CSV
        dados = list(zip(self.frequencia_cardiaca, self.distancia_percorrida))
        with open('dados_monitoramento.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Frequência Cardíaca', 'Distância'])
            writer.writerows(dados)

        messagebox.showinfo("Exportar Dados", "Dados exportados para dados_monitoramento.csv")

    def simular_dados(self):
        self.frequencia_cardiaca = []
        self.distancia_percorrida = []

        for i in range(60):
            if not self.monitoramento_ativo:
                break

            frequencia_cardiaca = random.randint(60, 160)
            distancia_percorrida = random.uniform(0.1, 0.5)

            self.frequencia_cardiaca.append(frequencia_cardiaca)
            self.distancia_percorrida.append(distancia_percorrida)

            self.atualizar_interface(f"Frequência Cardíaca: {frequencia_cardiaca} BPM, Distância: {distancia_percorrida:.2f} km")
            self.atualizar_grafico(self.frequencia_cardiaca, self.distancia_percorrida)
            self.progress_bar["value"] = (i + 1) * (100 / 60)
            self.root.update()
            time.sleep(1)

        self.parar_monitoramento()

    def atualizar_interface(self, mensagem):
        self.label.config(text=mensagem)

    def atualizar_grafico(self, frequencia_cardiaca, distancia_percorrida):
        self.ax.clear()
        self.ax.plot(frequencia_cardiaca, label='Frequência Cardíaca', color='blue')
        self.ax.set_ylabel('BPM', color='blue')
        self.ax.set_xlabel('Tempo (s)')
        self.ax.legend(loc='upper left')

        ax2 = self.ax.twinx()
        ax2.plot(distancia_percorrida, label='Distância', color='green')
        ax2.set_ylabel('Distância (km)', color='green')
        ax2.legend(loc='upper right')

        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = MonitorAtividadeFisicaApp(root)
    root.mainloop()
