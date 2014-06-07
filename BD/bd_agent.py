import json
from bd_data import DataHandler

class ServerData:
    def __init__(self):
        self.__datahandler = DataHandler()

    def get_db(self,user_id):
        return self.__datahandler.get_data_db(user_id)

    def insert_bd(self, ano,atividade,data,prioridade,semanaDoAno, tempo, tipo, user_id):
        return self.__datahandler.save_data_db(ano,atividade,data,prioridade,semanaDoAno, tempo, tipo, user_id)
