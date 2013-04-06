'''
/* Listing 46-3 */

/* svmsg_receive.c

   Usage: svmsg_receive [-nex] [-t msg-type] msqid [max-bytes]

   Experiment with the msgrcv() system call to receive messages from a
   System V message queue.

   See also svmsg_send.c.
*/
'''

# $ python svmsg_receive.py 10 -n 0x21

import getopt
import sys
import sysv_ipc

def usage():
    print '''\
    Usage: %s [options] msqid [max-bytes]
    Permitted options are:
        -e       Use MSG_NOERROR flag
        -t type  Select message of given type
        -n       Use IPC_NOWAIT flag
        -x       Use MSG_EXCEPT flag
    ''' % __file__

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hent:x", ["help", ])
    except getopt.GetoptError, err:
        print str(err)
        usage()

    flags = 0
    type = 0
    block = True

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-e", ):
            flags |= sysv_ipc.MSG_NOERROR
        elif o in ("-n", ):
            block = False
        elif o in ("-t", ):
            type = int(a, 0)
        elif o in ("-x", ):
            flags = sysv_ipc.MSG_EXCEPT
        else:
            assert False, "unhandled option"

    key = int(sys.argv[-1], 0)
    mq = sysv_ipc.MessageQueue(key)
    try:
        mtext, mtype = mq.receive(type=type, block=block)
        print "Received: type=%d; body=%s" % (mtype, mtext)
    except sysv_ipc.BusyError, err:
        print err

if __name__ == '__main__':
    main()
