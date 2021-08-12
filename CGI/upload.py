#!/usr/bin/python3

import cgi, os
import cgitb; cgitb.enable()
import subprocess as sp
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open('/var/www/html/carpix/' + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
else:
   message = 'No file was uploaded'
sp.getoutput("sudo chmod 777 /var/www/html/carpix/"+fn)
sp.getoutput("sudo cp /var/www/html/carpix/"+fn+" /var/www/html/task8.jpeg")
sp.getoutput("sudo chmod 775 /var/www/html/task8.jpeg")
sp.getoutput("sudo cp /var/www/html/task8.jpeg /var/www/cgi-bin/task8.jpeg")
sp.getoutput("sudo chmod 775 /var/www/cgi-bin/task8.jpeg")

print ("""\
content-type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,))




