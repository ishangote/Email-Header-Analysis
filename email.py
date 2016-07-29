#/bin/python
#To print key-value pairs of email header.

rlist=[]
with open('email.txt','r+') as fo:	
	for line in fo:		
		if line.startswith('Date:'):
			print line
		if line.startswith('From:'):
			print line
		if line.startswith('To:'):
			print line
		if line.startswith('Message-ID:'):
			print line
		if line.startswith('Subject:'):
			print line
		if line.startswith('MIME-Version:'):
			print line
fo.close()
with open('email.txt','r+') as fo:	
	for line in fo:
		if line.startswith('Received:'):
			rlist.append(line)
		if line.startswith(" "):
			rlist.append(line)
	print "".join(rlist)
fo.close()


