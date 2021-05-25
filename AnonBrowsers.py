import os
import time

def ddgr_duckduckgo():
    os.system("apt-get install ddgr")
    os.system("clear")
    return main()

def tor_browser():
    os.system("wget https://www.torproject.org/dist/torbrowser/8.5.3/tor-browser-linux64-8.5.3_en-US.tar.xz")
    os.system("clear")
    return main()

def jondo():
    os.system("wget https://jondobrowser.jondos.de/releases/current/jondobrowser-linux64_en-US.tar.xz")
    os.system("apt-get install default-jre java-wrappers firefox")
    os.system("dpkg -i jondo_all.deb")
    os.system("dpkg -i jondofox-en_all.deb")
    os.system("clear")
    return main()

def tor():
    print("El navegador debe configurarse manualmente ingresando el puerto 9050.")
    os.system("apt-get install tor && service tor start")
    os.system("clear")
    return main()

def iridium_browser():
    os.system("wget -qO - https://downloads.iridiumbrowser.de/ubuntu/iridium-release-sign-01.pub|sudo apt-key add -")
    os.system("cat <<EOF | sudo tee /etc/apt/sources.list.d/iridium-browser.list","deb [arch=amd64] https://downloads.iridiumbrowser.de/deb/ stable main","EOF")
    os.system("sudo apt update")
    os.system("sudo apt install iridium-browser")
    return main()

def brave_browser():
    os.system("apt install apt-transport-https curl")
    os.system("curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
    os.system("echo 'deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main'|sudo tee /etc/apt/sources.list.d/brave-browser-release.list")
    os.system("apt update")
    os.system("apt install brave-browser")
    return main()

def salir():
    print('\033[5;31m' "<<<<<<<<<<Saliendo de la Herrameinta>>>>>>>>>>")
    time.sleep(5)
    exit()


banner = """


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<By:DarkPhoenix87>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    #                         ######                                                   
   # #   #    #  ####  #    # #     # #####   ####  #    #  ####  ###### #####   ####  
  #   #  ##   # #    # ##   # #     # #    # #    # #    # #      #      #    # #      
 #     # # #  # #    # # #  # ######  #    # #    # #    #  ####  #####  #    #  ####  
 ####### #  # # #    # #  # # #     # #####  #    # # ## #      # #      #####       # 
 #     # #   ## #    # #   ## #     # #   #  #    # ##  ## #    # #      #   #  #    # 
 #     # #    #  ####  #    # ######  #    #  ####  #    #  ####  ###### #    #  ####  
                                                                                                                                    

Canal Youtube: https://www.youtube.com/channel/UConS1Dk6zZAOFuaSwTtLbqA

Github: https://github.com/DarkPhoenix2020 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<By:DarkPhoenix87>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


"""

def main():
        print('\033[0;33m' + banner + '\033[0;33m')
	menu = '''
    (1) DDRG(DUCKDUCKGO)
    (2) TOR-BROWSER
    (3) JONDO x64
    (4) TOR
    (5) BRAVE-BROWSE
    (0) SALIR
	'''
        print('\033[1;36m' + menu + '\033[1;36m')

        opcion = raw_input("Introduzca el Numero, que corresponda a la Opcion deseada : ")

        if opcion == "1":
            ddgr_duckduckgo()
        elif opcion == "2":
            tor_browser()
        elif opcion == "3":
            jondo()
        elif opcion == "4":
            tor()
        elif opcion == "5":
            brave_browser()
        elif opcion == "0":
            salir()
        else:
            print("Opcion Incorrecta")
            exit()

main()
