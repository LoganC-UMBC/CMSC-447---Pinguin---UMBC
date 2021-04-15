import pymongo
import PinguinDB
from datetime import datetime, timedelta

dt = datetime.now()
td = timedelta(days=7)
my_date = td + dt
td = timedelta(days=20)
later_date = td + dt
x = PinguinDB.PinguinDB()
x.login("testEncrypt@gmail.com","admin")
#x.calendar_add("Group2", "one week reminder",later_date)
x.retrieve_calendar_posts("Group2", my_date, "year")
#x.create_group("Group2","My test group")
#x.send_post("Group1", "Test Post")
#x.retrieve_all_posts("Group1")