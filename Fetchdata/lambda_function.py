import json
import requests
import pprint
import mysql.connector
#Connecting to Database
def db_connection():
  mydb = mysql.connector.connect(host='** Your AWS Database host name **',
                                 user="** Your Database User name **",
                                 password="** Your Database Password **",
                                 database="** Your AWS MYSQL Database name **")
  print("I am connecting")
  return mydb

def lambda_handler(event, context):
   
    #Fetching Data

    try:
      response = requests.get('http://api.open-notify.org/iss-now.json')
      repo = response.json()
      print("===================== fetched Data In JSON format ============================================")
      pprint.pprint(repo)
      message=repo['message']
      if message == "success":
        timestamp = repo['timestamp']
        latitude = repo['iss_position']['latitude']
        longitude = repo['iss_position']['longitude']


#=================================== GETTING DATABASE CONNECTION ==================================================
        mydb = db_connection()

        mycursor = mydb.cursor()

#SQL Query to Create Table (Run only one time)

        #mycursor.execute("CREATE TABLE open_api (timestamp VARCHAR(100), latitude VARCHAR(5),longitude VARCHAR(100))")

# SQL Query to insert fetched data to MySQL database

        sql = "INSERT INTO open_api (timestamp,latitude,longitude) VALUES (%s, %s, %s)"
        val = (timestamp,latitude,longitude)
        mycursor.execute(sql, val)
        mydb.commit()
        mycursor.close()
        mydb.close()

      else:
       raise Exception("Error occurred in server")
    except:
       raise Exception("Error occurred in server")



