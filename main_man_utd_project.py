import pymysql
import pandas as pd

class ManU:
    def dbConnect(self):
        self.connection = pymysql.connect(host='localhost',user='root',password='Dawaw19!',db='man_utd_db',charset='utf8')
        self.c = self.connection.cursor()
    def executeSelect(self,sql):
        self.c.execute(sql)
        for row in self.c.fetchall():
            print(row)
    def executeInsert(self, sql):
        self.c.execute(sql)
        self.connection.commit()

navig = ManU()
navig.dbConnect()
navig.executeSelect("select * from `team`")
#navig.executeInsert("???")

#import danych z csv
data = pd.read_csv("man_utd_scores.csv", sep='\t')
print(data)

#web scraping














