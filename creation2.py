#!/Usr/bin/env python
#-- coding:utf-8 --

## Imports & Param's :

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from os import listdir
from os.path import isfile, join

# Path of ffmpeg executable for animation
plt.rcParams['animation.ffmpeg_path'] = r'C:/FFmpeg/bin/ffmpeg.exe'
#FFmpeg downloaded from : https://github.com/BtbN/FFmpeg-Builds/releases - Version : ffmpeg-N-100405-gbf4b9e933f-win64-gpl.zip


# Functions :


''' Returns the evolution of a board B after T generations '''
def get_history(B,T):
    history = np.zeros((T,B.shape[0], B.shape[1]),dtype=bool)
    for t in range(T):
        history[t,:,:] = B
        B = evolve(B)
    return history



''' Evolves a board of Game of Life for one turn '''
# Dead cells as a boundary condition
# Count neighbours
# Alive if 3 neighbours or 2 neighbours and already alive
def evolve(X):    
    Xi = X.astype(int)
    neigh = np.zeros(Xi.shape)
    neigh[1:-1,1:-1] = (Xi[:-2,:-2]  + Xi[:-2,1:-1] + Xi[:-2,2:] + 
                        Xi[1:-1,:-2] +                Xi[1:-1,2:]  + 
                        Xi[2:,:-2]   + Xi[2:,1:-1]  + Xi[2:,2:]) 
    
    return np.logical_or(neigh==3,np.logical_and(Xi==1,neigh==2))


''' Create the movie from a history of a game of life'''
# History is the boolean history (non inverted i.e. True = alive)
# Inversion is done in the colormap
# Filename should be *.mp4
def makeMovie(history, filename):
    
    FIGSIZE = (16,9)
    DPI = 240
    LW = 0.5    
    USE_IMSHOW = history.shape[1]>200
    
    # Create the plot and its starting point
    print("Create initial plot")
    my_cmap = plt.get_cmap('gray_r')
    fig = plt.figure(figsize=FIGSIZE,dpi=DPI)
    ax = fig.add_subplot(111)
    
    if USE_IMSHOW :            
        # First option : use imshow
        im  = ax.imshow(history[0,:,::-1].T, cmap='gray_r')
    else:
        # Second option : use pcolor
        pc = ax.pcolor(history[0,:,:].T, cmap='gray_r', edgecolors='cadetblue', linewidths=LW)
      
    #cnt is for annotating the step of the game
    #cnt = ax.text(0.01, 0.99, str(0),color='red', fontsize=30, verticalalignment='top', horizontalalignment='left', transform=ax.transAxes)
    plt.axis('off')
    fig.tight_layout()
        
    # The function as it is called at the n-th iteration
    # It directly modifies the data within the image
    def update_img(n):
        # Revert and scale from 0-1 to 0-255
        #print('Frame '+str(n))
        if USE_IMSHOW :
            im.set_data(history[n,:,::-1].T)            
        else:
            new_color = my_cmap(255*history[n,:,:].T.ravel()) 
            pc.update({'facecolors':new_color})        
        #cnt.set_text(str(n))
        return True
    
    # Create the animation and save it
    print("Make animation")
    ani = animation.FuncAnimation(fig, update_img, history.shape[0], interval=60) # 30ms per frame
    writer = animation.FFMpegWriter(fps=30, bitrate=5000)
    print("Save movie")
    ani.save(filename, writer = writer, dpi=DPI) 
    print("Saved")



def readRLE(filename):
    
    # Open file and cast it into a unique string    
    s = ''
    with open(filename,"r") as f :        
        for line in f :                 
            if line[0] =='#':
                continue
            if line[0] =='x':
                continue
            s = s + line[:-1]   # To remove EOL   
     
    # Create matrix
    SHAPE_MAX = (2500,2500)
    B = np.zeros(SHAPE_MAX, dtype=bool)

    curX, curY = 0, 0 #Les coordonnées x,y de la cellule b ou o B[curX, curY] = True si vivante "o", False sinon
    qs = '' #Le nombre de fois où la cellule b ou o doit se répéter
    #q sera simplement la conversion en int de qs (qui est un str)

    for c in s:

        # Next Line : Lorsqu'on arrive à la fin d'une ligne, on remet x à 0 et on fait avancer y d'un pas
        if c=='$':        
            q = 1 if qs=='' else int(qs)
            curY += q #On fait avancer les coordonnées Y, car on se trouve sur une nouvelle ligne
            curX = 0  #On remet les coord X à 0, car on se trouve sur une nouvelle ligne
            qs = ''

        # Digit (check ascii code for a digit from 0 to 9)
        if ord(c)>47 and ord(c)<58:  #Lorsqu'on est sur un entier (écrit en str) on l'ajoute à qs
            #Car la cellule doit se répéter int("c") fois /!\ : deux entiers écrit en str peuvent se suivre
            qs = qs + c        

        # Alive (o) or Dead (b) cell : Lorsqu'on est sur une cellule 'o' ou 'b'
        #On doit simplement inscrire dans la matrice B, 
        #aux coordonnées B[curX, curY] = True si vivante "o", False sinon
        #A chaque fois qu'on inscrit une information, la coordonnée x s'incrémente
        #Si une cellule se repète : par exemple 3o => on doit boucler trois fois, et inscrire trois fois l'information True d'où la boucle sur q
        #else:
        if c == 'b' or c=='o':        
            q = 1 if qs=='' else int(qs)
            for i in range(q):
                B[curX, curY] =  c=='o' #True si la cellule c est vivante, False sinon
                curX += 1
            qs = ''

    BshapeY=max(np.where(sum(B)>0)[0])+1    #Je prends le dernier indice y, où il y'a au moins une cellule vivante
    BshapeX=max(np.where(sum(B.T)>0)[0])+1  #Je prends le dernier indice x, où il y'a au moins une cellule vivante
    B = B[0:BshapeX,0:BshapeY] #Je vais utiliser ces indices, pour reshaper B | +1 car les opérateurs : ne prennent pas le dernier element

    facteurAgrandissement = 2
    posX = (BshapeX // 2) * facteurAgrandissement
    posY = (BshapeY // 2) * facteurAgrandissement
    computedShape = max(BshapeY,BshapeX) * facteurAgrandissement
    
    C = np.zeros((computedShape, computedShape))
    C[posX:(posX+BshapeX),posY:(posY+BshapeY)] = np.copy(B) #Enroule B dans une nouvelle matrice C, B est entouré de False pour êre dessiné aux positions pos données

    return C.astype(bool)


''' Plots a board of Game of Life + optionally saving the figure '''
def plotcells(X, filename=False):        
    LW = 0.5
    USE_IMSHOW = X.shape[0]>200
        
    fig = plt.figure(figsize=(16,9),dpi=144)
    if USE_IMSHOW :
        plt.imshow(X[:,::-1].T, cmap="gray_r") #imshow() : inverse automatiquement l'affichage, on lui donne donc l'inverse de X pour avoir le même affichage que pcolor()        
    else:        
        plt.pcolor(X.T, cmap="gray_r", edgecolors='cadetblue', linewidths=LW) # Light blue lines as cells boundaries    
    
    plt.axis('off')
    fig.tight_layout()
    plt.savefig(filename,dpi=144) if filename else plt.show()



''' Load a pattern from an RLE file, run evolution and make a movie '''
def do_it(patterns, T):
    for pattern in patterns :
        try :            
            B = readRLE("rle/"+pattern) # Read RLE file in the rle folder
        except :
            continue
        history = get_history(B,T)
        makeMovie(history,"output/"+pattern+".mp4")

## Main 

patterns = [f for f in listdir("rle/") if isfile(join("rle/", f))]
iterations = 300
do_it(patterns, iterations)