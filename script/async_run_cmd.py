#!/usr/bin/env python
"""
    @file async run cmd
    @author shikuan@baidu.com
    @date 2015.09.15
"""

import os
import sys
import argparse
import subprocess

LOOP = False
LOOP_COUNT = 10

def run_shell(command,
              useshell=True,
              universal_newlines=True,
              async=False):
    """
    execute cmd as shell
    """
    ret = {
        'rtc':      -1,
        'stdout':   None,
        'stderr':   None,
    }   
    try:
        p = subprocess.Popen(command,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          shell=useshell,
                          universal_newlines=universal_newlines)
        if async:
            return p
        output, errout = p.communicate()
        ret = {
            'rtc':  p.returncode,
            'stdout':   output,
            'stderr':   errout,
        }
        return ret
    except:
        return ret


def async_run_cmd(cmd_list, mode):
    """ run deploy.py async """
    if not cmd_list:
        print "[ERROR] cmd_list is empty"
        return -1
 
    cmd_count = len(cmd_list)
    popen_list = []

    # async run cmd
    for cmd in cmd_list:
        if not cmd:
            print "[Exception] cmd is empty"
            continue
        p = run_shell(cmd, async=True)
        popen_list.append(p)
        print "[INFO] cmd[%s] : pid[%s]" % (cmd, p.pid)

    # get run result
    run_status = True
    for p_obj in popen_list:
        if not run_status and mode != 0:
            print "[INFO] kill other proc: %s" % p_obj.pid
            p_obj.kill()
            continue

        output, errout = p_obj.communicate() 
        retcode = p_obj.returncode
        if retcode != 0:
            print "[ERROR] some error in running cmd, pid[%s]!" % p_obj.pid
            print errout
            run_status = False
            continue
        print "[INFO] proc[%s] result:\n %s" % (p_obj.pid, output)
    return run_status                

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='async run cmd')
    parser.add_argument('-m', '--mode', default=0, type=int, help='mode 1 for all cmd run required true, mode 0 for else')
    parser.add_argument('-l', '--loop', default=0, help='counts of loop to run async')
    parser.add_argument('cmd_list', metavar='cmd_list', nargs='+',
                        help='serial cmds to run')
    args = parser.parse_args()
    print args
    status = async_run_cmd(args.cmd_list, args.mode) 

    if args.loop:
        for i in range(1, int(args.loop)):
            status = async_run_cmd(args.cmd_list, args.mode) 

    if not status:
        sys.exit(1)
