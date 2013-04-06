'''
/* Listing 46-2 */

/* svmsg_send.c

   Usage: svmsg_send [-n] msqid msg-type [msg-text]

   Experiment with the msgsnd() system call to send messages to a
   System V message queue.

   See also svmsg_receive.c.
*/
'''
import getopt
import sys
import sysv_ipc

# $ python svmsg_send.py -n 0xabc 10 'hello world!'
# msqid : 294912

def usage():
    print '''\
   Usage: %s [-n] msqid msg-type [msg-text]

   Experiment with the msgsnd() system call to send messages to a
   System V message queue.

   See also svmsg_receive.c.
   ''' % __file__

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hn", ["help", ])
    except getopt.GetoptError, err:
        print str(err)
        usage()

    block = True
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-n", ):
            block = False
        else:
            assert False, "unhandled option"

    key = int(sys.argv[-3], 0)
    type = int(sys.argv[-2], 0)
    message = sys.argv[-1]
    mq = sysv_ipc.MessageQueue(key)
    mq.send(message=message, type=type, block=block)

if __name__ == '__main__':
    main()

