import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

r0 = 3
n = 100
x0 = 0.62

def calc(r):
    x = np.empty(n + 1)
    x[0] = x0

    for k in range(n):
        x[k + 1] = r * x[k] * (1 - x[k])

    return x


fig, (ax, bx) = plt.subplots(2, 1)
fig.subplots_adjust(bottom=0.25)

fig.canvas.manager.set_window_title("Logistic map")

#logistic map at a given r value
line, = ax.plot(calc(r0))

ax.set_xlim(0, n)
ax.set_ylim(0, 1)
ax.grid()
ax.set_xlabel("Set elements")
ax.set_ylabel("Population")
ax.set_title("Logistic map")

slider_ax = fig.add_axes([0.2, 0.08, 0.65, 0.04])

slider = Slider(
    ax=slider_ax,
    label="r",
    valmin=0,
    valmax=5,
    valinit=r0,
    valstep=0.01
)

def update(val):
    line.set_ydata(calc(slider.val))
    fig.canvas.draw_idle()

slider.on_changed(update)


# Bifurkációs diagram számítása
r_values = np.linspace(0, 5, 6001)
x = np.full_like(r_values, x0)

r_points = []
x_points = []

for k in range(100):
    x = r_values * x * (1 - x)

    if k >= 25:
        r_points.append(r_values)
        x_points.append(x.copy())

# Összes pont egyetlen kirajzolással
bx.scatter(
    np.concatenate(r_points),
    np.concatenate(x_points),
    s=0.2,
    linewidths=0
)

bx.set_xlim(0, 5)
bx.set_ylim(0, 1)
bx.grid()
bx.set_xlabel("r")
bx.set_ylabel("Population")
bx.set_title("Bifurcation diagram")

plt.show()
