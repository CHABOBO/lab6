#A count-bolt, that counts the number of words emitted by the tweet-parse bolt,
# and updates the total counts for each word in the Postgres table. 
#Modify the code in wordcount.py so that it updates the table. 
#You can find sample code on how to use the psycopg library to interact with Postgres in psycopg-sample.py.file.


import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt



class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]

        cur = conn.cursor()

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        #conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        uCount= self.counts[word]
        uWord= word
        cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (uCount, uWord))
        conn.commit()

        cur.execute("SELECT word, count from tweetwordcount")
        records = cur.fetchall()
        for rec in records:
          print("word = ", rec[0])
          print("count = ", rec[1], "\n")
        conn.commit()

        conn.close()

# Connect to the database
#conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

#Create the Database

#try:
    # CREATE DATABASE can't run inside a transaction
    #conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    #cur = conn.cursor()
    #cur.execute("CREATE DATABASE tcount")
    #cur.close()
    #conn.close()
#except:
   # print "Could not create tcount"

#Connecting to tcount

#conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

#Create a Table
#The first step is to create a cursor. 

#cur = conn.cursor()
#cur.execute('''CREATE TABLE tweetwordcount
#       (word TEXT PRIMARY KEY     NOT NULL,
#       count INT     NOT NULL);''')
#conn.commit()


#Running sample SQL statements
#Inserting/Selecting/Updating

#Rather than executing a whole query at once, it is better to set up a cursor that encapsulates the query, 
#and then read the query result a few rows at a time. One reason for doing this is
#to avoid memory overrun when the result contains a large number of rows. 


#Insert
#cur.execute("INSERT INTO tweetwordcount (word,count) \
#      VALUES ('test', 1)");
#conn.commit()

#Using variables to update
#uCount= self.counts[word]
#uWord= word
#cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (uCount, uWord))
#conn.commit()

#Select
#cur.execute("SELECT word, count from tweetwordcount")
#records = cur.fetchall()
#for rec in records:
#   print "word = ", rec[0]
#   print "count = ", rec[1], "\n"
#conn.commit()

#conn.close()