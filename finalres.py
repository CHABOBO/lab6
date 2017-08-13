def fetchRecords():
	import psycopg2
	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", port="5432")
	cur = conn.cursor()
	cur.execute('''SELECT * FROM tweetwordcount ORDER BY word ASC;''')
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
		findword = args[0]
		for r in recs:
			if r[1]==findword:
				print "Total number of occurances of '"+ findword + "': " + str(r[2])
				return
		print "Total number of occurances of '"+ findword + "': " + str(0)
	else:
		print [(r[1],r[2]) for r in recs]

	


if __name__ == '__main__':
	main()

