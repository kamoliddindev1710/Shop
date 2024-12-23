def SecondQuery(self):
          self.cursor.execute("SELECT * from teachers order by salary ,experience dec")
          natija=self.cursor.fetchall()
        #   print(natija)
          for x in natija:
                print(x)
