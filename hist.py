def fetchRecords():
	import psycopg2
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", port="5432")
	cur = conn.cursor()
	cur.execute('''SELECT * FROM tweetwordcount ORDER BY count DESC;''')
	records = cur.fetchall()
	conn.commit()
	conn.close()

	return records


def main():
	from optparse import OptionParser
	parser = OptionParser()
	parser.add_option("-v", "--verbose", action = "store_true")

	(options, args) = parser.parse_args()
	recs = fetchRecords()
	
	if len(args) > 0:
		minhist = int(args[0].split(',')[0])
		maxhist = int(args[0].split(',')[1])
		
		for i in recs:
			
			if (i[2]>=minhist) and (i[2]<=maxhist):
				print i[1] + ': ' + str(r[2])
	else:
		print "Error!!! Fix yo Hist FUNC"

	


if __name__ == '__main__':
	main()