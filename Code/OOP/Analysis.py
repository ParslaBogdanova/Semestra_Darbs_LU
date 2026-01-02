import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from scipy.stats import norm
import math


class Analysis():
    def __init__(self):
        self.distances = []
        self.times = []

    def record_clicks(self, circle_x, circle_y, mouse_x, mouse_y, reaction_time):
        dx = mouse_x - circle_x
        dy = mouse_y - circle_y
        distance = math.sqrt(dx**2 + dy**2)

        self.distances.append(distance)
        self.times.append(reaction_time)

    def gauss_line(self, data):
        mu = np.mean(data)
        sigma = np.std(data)
        x = np.linspace(min(data), max(data), 100)
        y = norm.pdf(x, mu, sigma) * len(data) * (max(data)-min(data))/25
        return x, y

    def show_results(self):
        with PdfPages("Analysis.pdf") as pdf:

            x_d, y_d = self.gauss_line(self.distances)
            x_t, y_t = self.gauss_line(self.times)

            plt.figure(figsize=(12, 8))

            plt.subplot(1, 2, 1)
            plt.title("Attālums no apļa centra")
            plt.xlabel("Attālums(px)")
            plt.ylabel("Skaits")
            plt.hist(self.distances, density=False, bins=25, alpha=0.6,
                     edgecolor="black", color="#c0a0db")
            plt.plot(x_d, y_d, 'r', linewidth=2)

            plt.subplot(1, 2, 2)
            plt.title("Reakcijas laiks")
            plt.xlabel("Reakcijas laiks(ms)")
            plt.ylabel("Skaits")
            plt.hist(self.times, bins=25, density=False,
                     alpha=0.6, edgecolor="black", color="#a0d1db")
            plt.plot(x_t, y_t, 'r', linewidth=2)

            plt.tight_layout()
            pdf.savefig()
            plt.show()
