import pygame, time
from pygame.locals import*
import random

pygame.init()

screen= pygame.display.set_mode (( 1000 , 600 ))
pygame.display.set_caption ( 'Tour Hanoi' )




def  hanoi ( n ,  start, temp, target ): #recursion qui résout la tour hanoi
    global  etape
    if  n == 0 :
        etape.append([ 1 , start , target ])
        return etape
    else:
        hanoi(n - 1, start, target, temp)
        etape.append([ n , start , target ]) ## ajoute a la liste etape une liste contenat les positionnement de chaque disque 
        hanoi(n - 1, temp, start, target)




def  dessiner( pos ): # dessine l'état des piquets et la postion des disques enreigstré sur la liste pos 
    global color
    
    pygame.draw.rect(screen, Color( 'light green' ), ( 0 , 0 , 1000 , 600 ))## met le fond de la fenetre en vert clair
    for i  in range ( 3 ):
        pygame.draw.rect ( screen , ( 255 , 255 , 255 ), ( i * 300 + 200 , 100 , 20 , 500 )) ## dessine les 3 piquets en blanc
    # dessine les disques 
    for  i  in range( len (pos)):
        a= - 1 ## la variable a va permettre d'ajuster la postion du coordonnés y 
        for  j  in range( i + 1 ):
            if  pos[ i ] ==  pos[ j ]:
        
                a+= 1 
        myDisk=pygame.Rect( pos[ i ] * 300 + ( 150 + i * 25 ) - 90 , 570 - a * 30 , 300 - i * 50 , 30 )
        ## Rect(x,y,width,height)
        pygame.draw.rect( screen , Color(color[i]), myDisk)
        ## rect(ecran,couleur,rectangle)
    pygame.display.update()
    

def  move( i ):   # fct qui change l'état des piquets selon les positionnement des disques stocké dans la liste de sous liste etape  
    global  etape
    global position
    ##  0 pour les disques positioné sur le piquet A
    ##  1 pour les disques sur le piquet B
    ##  2 pour les disques sur le piquet C
    
    if etape[ i ][ 2 ] ==  'A' :
        position[ len ( position ) - etape[ i ][ 0 ]] =  0
    if  etape[ i ][ 2 ] ==  'B' :
        position[ len ( position ) - etape[ i ][ 0 ]] =  1
    if etape[ i ][ 2 ] ==  'C' :
        position[ len ( position ) - etape[ i ][ 0 ]] =  2
    ##print(position)
    time.sleep(0.1) ## cela va permettre de voir les déplacements des disques
    
    

n =7 # vous pouvez définir le nbre de disque.
## ATTENTION ! le nbre maximal de disque est 7 au delà de 7 le programme ne marche pas bien.

etape = []    # liste qui va contenir les étapes n de résolution qui seront ajouter par l'appel de la fct hanoi
position = []     #liste qui va contenir la position intiale des disques
## initialise la taille de liste position selon le nbre de disque
for i  in range(n):
    position.append( 0 )
## choix de couleur des rectangle correspondant aux disques
color=[]
choix_couleur=['red','black','yellow','blue','purple']
for i in range( n ):
    color.append ( random.choice( choix_couleur))
## appel de la fct honoi qui renvoie la liste etape
hanoi ( n , 'A' , 'B' , 'C' )
##print(etape)

## Main

i  =  0 ## compteur d'arrêt
run  =  True
while run:
    time.sleep(0.05)
    for event in pygame.event.get ():
        if event.type  ==  pygame.QUIT :
            run  =  False 
    dessiner( position )
    move( i )
    i += 1
    if  i  >  len (etape ) - 1 : ## si le compteur i est superieur au nbre de deplacements arrêter la boucle
        run  =  False

   

time.sleep(0.10)
pygame.quit()
