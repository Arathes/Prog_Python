

print("Hallo Welt und Felix")

limits = [-3.8, 5.9]
num_points = 20
height = 20

def calc_function (x):
    return 3 * x**3 - 2*x - 1

x_values = [limits[0] + (i * (limits[1] - limits[0]) / num_points) for i in range(num_points + 1)] # Nice to know um einfaches Array zu erstellen
y_values = [calc_function(x) for x in x_values]


min_y = min(y_values)
max_y = max(y_values)





def plot_values(x_values, y_values):

    plot_null = int(((0 - min_y) / (max_y - min_y)) * height)

    for y in reversed(range(height + 1)):
        line = ''
        for x in x_values:
            value = calc_function(x)
            # Höhe des Plots anpassen
            plot_position = int(((value - min_y) / (max_y - min_y)) * height) # Abstand y zu min. Funktionswert / Gesamtabstand Funktionswerte um einen Faktor zu erhalten * Höhe fürs plotten
            
            if plot_position == y:
                line += '*'
            elif plot_null == y:
                line += '-'
            else:
                line += ' '
        print(line)


print("Die Funktion:")
plot_values(x_values, y_values)


