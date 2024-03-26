import mysql
import time
import requests
import mysql.connector
import json
class submit_from_mysql:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'pkuinfo',
            'host': '127.0.0.1',
            'database': 'info',
            'raise_on_warnings': True
        }
    def POSTER(self,link):
        headers = {'Content-Type': 'application/json'}
        url = 'http://localhost:9002/'
        data = {'URL': link}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r)
        print(r.text)

    def read_from_table(self):
        records = []
        try:
            connection = mysql.connector.connect(**self.config)
            cursor = connection.cursor()
            query = "SELECT * FROM t_activity_link_active"
            cursor.execute(query)
            records = cursor.fetchall()
            query = "DELETE FROM t_activity_link_active"
            cursor.execute(query)
            connection.commit()
        except mysql.connector.Error as err:
            print("MySQL 错误：", err)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
        return records



if __name__ == '__main__':
    submit_from_mysql = submit_from_mysql()
    while True:
        ALL_INFO = submit_from_mysql.read_from_table()
        for info in ALL_INFO:
            for i in range(5):
                response = submit_from_mysql.POSTER(info[1])
                # print(response)
                # output to LOG FILE with info[1] and response
                with open('LOGS.txt', 'a') as f:
                    f.write(info[1] + ' ' + str(response) + '\n')
                    f.flush()
                time.sleep(3)