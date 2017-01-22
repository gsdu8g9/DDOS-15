import urllib2
for i in range (0,100000):
	req = urllib2.Request('http://0.0.0.0:5000/getEmployees/baduser')
	response = urllib2.urlopen(req)
	the_page = response.read()
	print the_page


