import sys

print >> sys.stderr, 'Fatal error: invalid input !'  # >> 表示定向输出
print >> sys.stderr, 'Fatal error: invalid input !'

logfile = open('/mylog.txt', 'a')
print >> logfile, 'Fatal error: invalid input !'
logfile.close()