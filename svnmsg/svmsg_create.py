'''
/* Listing 46-1 */

/* svmsg_create.c

   Experiment with the use of msgget() to create a System V message queue.
*/
'''
import getopt
import sys
import sysv_ipc

def usage():
    print '''\
    Usage: %s [-cx] {-f pathname | -k key | -p} [octal-perms]
        -c           Use IPC_CREAT flag
        -x           Use IPC_EXCL flag
        -f pathname  Generate key using ftok()
        -k key       Use 'key' as key
        -p           Use IPC_PRIVATE key
    ''' % __file__

def main():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hcf:k:px", ["help", ])
    except getopt.GetoptError, err:
        print str(err)
        usage()

    flags = 0
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-c", ):
            flags |= sysv_ipc.IPC_CREAT
        elif o in ("-f", ):
            key = sysv_ipc.ftok(a, 1)
        elif o in ("-k", ):
            key = int(a, 0)
        elif o in ("-p", ):
            key = sysv_ipc.IPC_PRIVATE
        elif o in ("-x", ):
            flags |= sysv_ipc.IPC_EXCL
        else:
            assert False, "unhandled option"

    mq = sysv_ipc.MessageQueue(key, flags=flags, mode=0666)
    print "msqid :", mq.id

if __name__ == '__main__':
    main()
