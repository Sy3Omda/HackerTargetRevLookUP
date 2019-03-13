from urllib import urlopen as o
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', help='list of IPs')
args = parser.parse_args()
lists = open(args.list).read().split('\n')
for ip in lists:
    print 'Looking', ip
    grab = 'null'
    try:
        grab = o('https://api.hackertarget.com/reverseiplookup/?q=' + ip).read()
    except:
        continue
    if 'error check' in grab:
        print 'Check ip format in input file'
        continue
    if 'No records' in grab:
        print 'No reverse IP record available'
        continue
    grab = grab.split('\n')
    for domain in grab:
        open('reverse_result.txt', 'a+').write(domain + '\n')
