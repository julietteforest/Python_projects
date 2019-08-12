
"""
Programme qui chronomètre en millisecondes.
08/2019
Author:
        Juliette Forest
"""

print __doc__

import time
def chronometre():
    start = input("Pour lancer le chronomètre, pressez la touche Entrée")
    time_before = time.time()
    stop = input("Pour arrêter le chronomètre, appuyez sur la touche Entrée")
    time_after = time.time()
    time_spent = (time_after - time_before)*1000
    print("Le temps écoulé est de {} millisecondes.".format(time_spent))
    return time_spent
