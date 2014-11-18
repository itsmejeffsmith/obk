import csv

fn = "whatevs.csv"
newFile = open(fn, 'rw') 

def printcsv(fname):
	print fn
	with open(fn, 'w') as csvfile:
		docReader = csv.reader(newFile)
		print docReader
		for row in docReader:
			#print "here", row
			print ', '.join(row)


print fn
print newFile
printcsv(newFile)