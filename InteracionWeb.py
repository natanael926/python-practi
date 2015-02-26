import urllib2

try:

	f = urllib2.urlopen("http://platzi.com")

	print f.read()

	f.close()

except:
	print "Error"