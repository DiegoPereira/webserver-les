import MySQLdb as mdb
import time, datetime, json

class DataHandler:

    def __init__(self, server='localhost', user='root', password='s3y4_de_pegaso', db='mowatcher', table='activites_table'):
        try:
            self.con = mdb.connect(server, user, password, db)
            self.table = table;
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            return None

    def get_data_db(self, user_id):
        cursor = self.con.cursor()
        try:
            query = "select * from activites_table where user_id="+user_id
            cursor.execute(query)
            self.con.commit()
            
            rows = cursor.fetchall()
            ret = []

            for row in rows:
                ret.append({'ano':row[1],'atividade':row[2],'data':row[3],'prioridade':row[4],'semanaDoAno':row[5], 'tempo':row[6], 'tipo':row[7],'user_id':row[8]})

            return json.dumps({'atividades':ret})
        except Exception, e:
            print e
            return None
        finally:
            cursor.close()

    def save_data_db(self, ano,atividade,data,prioridade,semanaDoAno, tempo, tipo, user_id):
        cursor = self.con.cursor()
        try:
            query = 'insert into activites_table(ano,atividade,data,prioridade,semanaDoAno, tempo, tipo, user_id)'+' values '+'(' + str(ano) + ',' +'\"'+ atividade +'\"'+ ',' +'\"'+ data +'\"'+ ',' +'\"'+ prioridade +'\"'+ ',' + str(semanaDoAno) + ',' + str(tempo) + ',' +'\"'+ tipo +'\"'+ ',' +'\"'+ user_id +'\"'+ ');'
            cursor.execute(query)
            self.con.commit()
            
        except Exception, e:
            print e
            return None
        finally:
            cursor.close()
            return True
