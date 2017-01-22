
from timeit import default_timer
import urllib2



emp_no=299999

userid='gooduser'
 



#import cookielib
#cj = cookielib.CookieJar()
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#for i in range (0,4000):
#	start=default_timer()
#	r = opener.open("http://0.0.0.0:5000/getEmployees/gooduser")
#	the_page=r.read()
#	duration = default_timer() - start
#	print duration
#	print the_page

for i in range(0,2):
	start=default_timer()
	req = urllib2.Request('http://0.0.0.0:5000/getEmployees/'+str(userid)+'/'+str(emp_no))
	response = urllib2.urlopen(req)
	the_page = response.read()
	duration=default_timer()- start
	print the_page
	print duration











