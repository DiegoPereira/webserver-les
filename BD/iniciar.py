import subprocess
import time

time.sleep(60)
processo = subprocess.Popen("python bd_server.py", shell=True, stdout=subprocess.PIPE)
while True:
    if (processo.poll() == 0):
        break
    elif (processo.poll() == 1):
        print "Requisicao nao concluida"
        break
