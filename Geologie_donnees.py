
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import math as mathematiques

################ Fonction qui calcule l'échelle ##############################
def calculerEchelle(longueur_papier, longueur_terrain):
    longueur_papier = int(longueur_papier)
    longueur_terrain = int(longueur_terrain)
    denominateur = float((longueur_terrain * 1000000) / (longueur_papier * 10))
    deno_text = str(denominateur)
    text_splite = deno_text.split(".")
    partie_flottante = int(text_splite[1][:1])
    if partie_flottante < 5:
        denominateur = mathematiques.floor(denominateur)
    else:
        denominateur = mathematiques.ceil(denominateur)
    return denominateur

################ Fonction de conversion des données X #############################
def convertirX(nombre):
    return nombre*1000

################ Fonction de conversion des données Y #############################
def convertirY(nombre, echelle_trouve):
    return nombre*1000*echelle_trouve

################ Fonction qui calcule l'équidistance #############################
def calculerEquidistance(alt1, alt2):
    return mathematiques.fabs(alt1 - alt2)


def tracerCourbeGeologique(Xdata, Ydata):
    ma_figure = plt.figure("GeoGraph - Courbe géologique", figsize=(14, 7))  # Implemente une interface basique autonome
    ma_courbe = ma_figure.add_subplot(111)
    ma_courbe.plot(Ydata, Xdata)
    plt.show()


def tracerProfilTopographique(X, Y, Z):
    fig = figure("GeoGraph - Profil topographique", figsize=(14, 7))
    ax = fig.add_subplot(111, projection='3d')
    # X = donneesX #np.arange(-4, 4, 0.25)
    # Y = donneesY #np.arange(-4, 4, 0.25)
    # X, Y = np.meshgrid(X, Y)
    # R = np.sqrt(X ** 2 + Y ** 2)
    # Z = np.sin(R)
    # ax.plot_surface(X, Y, Z)
    # ax.contourf(X, Y, Z)
    # ax.set_zlim(-2, 2)
    # savefig('../figures/plot3d_ex.png',dpi=48)
    ax.plot_wireframe(Z, X, Y)
    plt.show()

sai = [8000, 9000, 7000]
sa = []
#convertir(sai, sa)
#print(sai)
#print("======================================================")
#print(echelle)
#print("======================================================")
#print(sa)
#tracerCourbeGeologique()
#tracerProfilTopographique()
