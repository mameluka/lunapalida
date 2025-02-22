
import winsound
import time
from colorama import init, Fore, Back, Style
init()

inv = {"ORO": False,
       "PALA": False,
       "SOGA": False, }

suelo = {"cavado": False,
         "enterrado": False,
         "tapado": False, }

oro = True and Fore.GREEN+">Hay ORO en la esquina."
pala = True and Fore.GREEN+">Hay una PALA en el borde."
soga = True and Fore.GREEN+">Hay una SOGA al lado."

loop = 4
while True:
    while loop == 4:
        if loop == 4:
            time.sleep(1)
            print(Fore.GREEN+">Te encuentras en una habitación oscura. La luz de la luna brilla por la ventana."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(oro), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(pala), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(soga), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Hay una PUERTA hacia el ESTE."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.YELLOW+">¿Comandos?"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.CYAN+"1) Coger ORO"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.CYAN+"2) Coger SOGA"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.CYAN+"3) Coger PALA"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.CYAN+"4) Ir al ESTE"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            second = input(">>>").strip().lower()
        if second.lower() == "1":
            print(Fore.GREEN+">Coges el ORO."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            oro = "" and False
            inv["ORO"] = True
        elif second.lower() == "2":
            print(Fore.GREEN+">Coges la SOGA."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            soga = "" and False
            inv["SOGA"] = True
        elif second.lower() == "3":
            print(Fore.GREEN+">Coges la PALA."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            pala = "" and False
            inv["PALA"] = True
        elif second.lower() == "4" and inv["ORO"] == True and inv["PALA"] == True and inv["SOGA"] == True:
            loop = 8
        elif second.lower() == "4":
            print(Fore.GREEN+">Te dirijes hacia la puerta"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(
                Fore.GREEN+">Al abrir la puerta notas como la luz de la luna palida acaricia tu rostro"), winsound.PlaySound('C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1.7)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Sientes cansancio"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Comienzas a pensar que fue una mala idea salir asi sin mas con" +
                  Fore.RED+" la luna "+Fore.GREEN+"de testigo de tu rostro..."), winsound.PlaySound('C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.YELLOW+"..."), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.RED+">>>FIN DEL JUEGO<<<"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            input(">>>")
            exit()
        else:
            print("")

    while loop == 8:
        if loop == 8:
            time.sleep(1)
            print(Fore.GREEN+">Cosecha tu recompensa."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Luna palida te sonrie"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Estas en el bosque. Hay caminos al OESTE, NORTE y ESTE"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.YELLOW+">¿Comandos?"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.CYAN+"1) Ir al NORTE"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.CYAN+"2) Ir al ESTE"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.CYAN+"3) Ir al OESTE"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.LIGHTCYAN_EX+"a) Usar ORO"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.LIGHTCYAN_EX+"b) Usar PALA"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.5)
            print(Fore.LIGHTCYAN_EX+"c) Usar SOGA"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            third = input(">>>").strip().lower()
        if third.lower() == "a":
            print(Fore.GREEN+">aqui no..."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
        elif third == "b":
            print(Fore.GREEN+">ahora no..."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
        elif third.lower() == "c":
            print(Fore.GREEN+">ya has usado esto..."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
        elif third.lower() == "1":
            time.sleep(1)
            print(Fore.GREEN+">Te dirijes hacia el NORTE."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">La luna se ve hermosa."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">La luz de la luna palida ilumina lo oscuro del bosque."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Escuchas ruidos de ramas quebrandose mientras caminas..."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(
                Fore.GREEN+">Al parecer el brillo de la luna tambien ha alcanzado a la manada de lobos."), winsound.PlaySound('C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Los lobos se saborean mientras te ven correr de la manada"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">La"+Fore.RED+" luna palida "+Fore.GREEN +
                  "te ha condenado a ser comida fresca para una manada de pulgosos en el bosque..."), winsound.PlaySound('C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.RED+">>>FIN DEL JUEGO<<<"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            input(">>>")
            exit()
        elif third.lower() == "2":
            print(Fore.GREEN+">Te dirijes hacia el ESTE."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            loop = 12
        elif third.lower() == "3":
            print(Fore.GREEN+">Te dirijes hacia el OESTE."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">La luna se ve hermosa."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">La luz de la luna palida ilumina lo oscuro del bosque."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">La luz de la luna palida ilumina tambien tu rostro."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Te quedas estatico apreciando la belleza de la luna."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Al parecer la belleza de"+Fore.RED +
                  " la luna palida "+Fore.GREEN+"te ha cautivado."), winsound.PlaySound('C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.GREEN+">Terminas desmayandote."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(1)
            print(Fore.RED+">>>FIN DEL JUEGO<<<"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
        else:
            print("")
    while loop == 12:
        if loop == 12:
            time.sleep(0.3)
            print(Fore.GREEN+">Luna palida sonrie ampliamente"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.LIGHTYELLOW_EX+"No hay caminos"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.GREEN+">Luna palida sonrie ampliamente"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.LIGHTYELLOW_EX+"El suelo es blando"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.GREEN+">Luna palida sonrie ampliamente"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.LIGHTYELLOW_EX+"Aqui"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.YELLOW+"¿Comandos?"), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.CYAN+"1) Cavar HOYO"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.CYAN+"2) Tirar ORO"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            time.sleep(0.3)
            print(Fore.CYAN+"3) Llenar HOYO"), winsound.PlaySound(
                'C:/Windows/Media/Windows Pop-up Blocked.wav', winsound.SND_FILENAME)
            if suelo["cavado"] == True and suelo["enterrado"] == True and suelo["tapado"] == True:
                loop = 16
            four = input(">>>").strip().lower()
        if four.lower() == "1":
            print(Fore.GREEN+">Cavas el HOYO."), winsound.PlaySound(
                'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            suelo["cavado"] = True
        elif four.lower() == "2":
            if suelo["cavado"] == False:
                print(Fore.GREEN+">No sin cavar antes"), winsound.PlaySound(
                    'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            elif suelo["cavado"] == True:
                print(Fore.GREEN+">Tiras el ORO"), winsound.PlaySound(
                    'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
                suelo["enterrado"] = True
        elif four.lower() == "3":
            if suelo["cavado"] == False and suelo["enterrado"] == False:
                print(Fore.GREEN+">No..."), winsound.PlaySound(
                    'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
            elif suelo["cavado"] == True and suelo["enterrado"] == True:
                print(Fore.GREEN+">Llenas el HOYO."), winsound.PlaySound(
                    'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
                suelo["tapado"] = True
        while loop == 16:
            if loop == 16:
                time.sleep(0.7)
                print(Fore.GREEN+"-- -33.48083314156804 --"), winsound.PlaySound(
                    'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
                time.sleep(0.7)
                print(Fore.GREEN+"-- -70.74024792386159 --"), winsound.PlaySound(
                    'C:/Windows/Media/chord.wav', winsound.SND_FILENAME)
                input(">>>")
                exit()
