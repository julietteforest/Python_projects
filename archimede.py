
"""
Archimedes' principle

Wikipedia quote
"Archimedes' principle states that the upward buoyant force that is exerted on a body immersed in a fluid,
whether fully or partially submerged, is equal to the weight of the fluid that the body's displaces and acts in the upward
direction at the center of mass of the displaced fluid. Archimedes' principle is a law of physics fundamental to fluid mechanics.
It was formulated by Archimedes of Syracuse."

10/2019
Author:
        Juliette Forest
"""

class float_or_not(): #name of our class
    def __init__(self, volume, masse):# give default values
        self.volume = volume # initialisation value (default)
        self.masse = masse # initialisation value (default)
        self.gravity = float(input("How is the gravity ?")) # enter the gravity of the place where the object is located
        self.masse_fluide = float(input("How is the fluid mass")) #enter the mass of th fluide where the objetc is

    # utility 1: calcule Archimedes' principle on the object
    def Archimedes_principle(self):
        AP = self.volume * self.masse_fluide * self.gravity
        print("Eureka! Archimedes' principle on the object is {}".format(AP))
        return AP

    # utilite 2: # calcule gravity on the objet
    def gravity_on_object(self):
        force = self.masse * self.gravity
        print("Eureka! The force of the gravity on this volume is {} Newton".format(force))
        return force


def comparing(AP,force): # comparing force of Archimedes' principle with the force of gravity to knwo if the object is floating or not
    if AP > force: # comparaison des résultats pour savoir si l'objet flotte ou non
        print("Object is floating.")
    else:
        print("It's drawning !! helps !")
