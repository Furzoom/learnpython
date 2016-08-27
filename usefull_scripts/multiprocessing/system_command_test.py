import os

def check_daemon():
    daemon_query = 'ps -ef | grep daemon_push.py | grep -v catlog | grep -v grep | grep -v ksh | grep -v awk | grep -c daemon_push.py'
    daemon_list = os.popen(daemon_query).readlines()
    if len(daemon_list) != 1:
        pids_query = 'ps -ef | grep daemon_push.py | grep -v catlog | grep -v grep | grep -v ksh | grep -v awk | awk \'{print $2}\''
        pids = os.open(pids_query).readlines()
        for pid in pids:
            os.system('kill -9 {0}'.format(pid))
            time.sleep(0.5)
        os.system('nohup /usr/bin/env python daemon_push.py &')
#        log.error('restart daemon_push.py')

if "__main__" == __name__:
    check_daemon()
