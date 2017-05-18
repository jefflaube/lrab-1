#          oooo                                .            
#          `888                              .o8            
# .ooooo.   888 .oo.    .ooooo.   .oooo.   .o888oo  .oooo.o
#d88' `"Y8  888P"Y88b  d88' `88b `P  )88b    888   d88(  "8
#888        888   888  888ooo888  .oP"888    888   `"Y88b.  
#888   .o8  888   888  888    .o d8(  888    888 . o.  )88b
#`Y8bod8P' o888o o888o `Y8bod8P' `Y888""8o   "888" 8""888P'
#
#
 
import subprocess,os,urllib2,sys,random,time
 
   
print("\x1b[0;32m**********************************\x1b[0m")    
print("\x1b[0;32m*  usage: python cheats.py       *\x1b[0m")
print("\x1b[0;32m* sets up pretty much everything *\x1b[0m")
print("\x1b[0;32m**********************************\x1b[0m")
 
def system(cmd):
    subprocess.call(cmd, shell=True)
   
 
pussy_server = raw_input("update/upgrade ? Y/n: ")
if pussy_server.lower() == "y":
    print("updating Server")
    system("yum update -y")
    system("yum upgrade -y")
    system("yum install gcc -y")
    system("yum install httpd -y")
    system("yum install tftp -y")
    system("yum install ftp -y")
    system("yum install nano -y")
    system("yum install wget -y")
    system("yum install perl -y")
    system("yum install xinetd tftp tftp-server -y")
    system("yum install screen -y")
    system("yum install nc -y")
    system("yum install cpan -y")
    system("yum install httpd -y")
    system("yum install nginx -y")
    system("yum install vsftpd -y")
    system("yum install busybox -y")
    system("yum install unzip -y")
   
   
    system("yum install gcc python-paramiko -y")
    system("yum install nano -y")
   
    system("service iptables stop")
    system("chkconfig iptables off")
    system("iptables -F")
   
    system("service vsftpd start")
   
    system("service xinetd start")
 
    system("service httpd start")
 
    system('echo -e "ulimit -n 99999" >> ~/.bashrc')
    system("echo -e \"ulimit -n 99999\" > ulimit.sh")
    system("sh ulimit.sh")
    system("rm -rf ulimit.sh")
   
    fdsize = open("/usr/include/bits/typesizes.h","r").readlines()
   
    fdsizew = open("/usr/include/bits/typesizes.h","w").write("")
    for line in fdsize:
        line = line.replace("1024","99999")
        fdsizew = open("/usr/include/bits/typesizes.h","a").write(line)
 
    system("yum install perl cpan -y")
    system("""echo -e \"cpan force install IO::Socket
cpan force install IO::Select 
cpan force install Parallel::ForkManager
cpan force install Net::SSH2
yum install screen -y
yum install gcc* -y --skip-broken
yum install cpan -y
yum install gcc php-devel php-pear libssh2 libssh2-devel -y --skip-broken
pecl install -f ssh2
touch /etc/php.d/ssh2.ini
echo extension=ssh2.so > /etc/php.d/ssh2.ini
/etc/init.d/httpd restart
php -m | grep ssh2
cpan -fi Net::SSH2
cpan -fi Parallel::ForkManager
yum groupinstall 'Development Tools' -y --skip-broken\" >> i.sh""")
    system("sh i.sh")
    system("rm -rf i.sh")
    system("chmod 777 *")
    system("clear")
print("\x1b[0;32mDo You Wish To Set All Your Unlimited FAG\x1b[0m")
assface = raw_input("Getting Ready Bitch Y to fuck the bitch hoe  Y/n: ")
if assface.lower() == "y":
    system ("ulimit -Hn 999999; ulimit -Sn 99999;echo -e 'ulimit -s 999999; ulimit -n 999999; ulimit -u 999999\n' > ~/.bashrc;ulimit -s 999999; ulimit -n 999999; ulimit -u 999999;sysctl -w fs.file-max=999999 >/dev/null;nano /etc/security/limits.conf")

