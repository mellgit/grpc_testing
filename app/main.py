import grpc
import data.protof.message_pb2 as message
import data.protof.message_pb2_grpc as message_gprc
from google.protobuf import json_format
from concurrent import futures

import time

 

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
TEMP = 0

def function_test(value):
    return True if value > 10 else False


# класса создается такой же, как и в прото файлу название сервиса
class MsgServicer(message_gprc.MsgServiceServicer):

    # метод, который принимает запросы от клиента
    def GetMsg(self, request, context):
        try:
            global TEMP
            TEMP+=1

            print(f'received name: {request.name}({len(request.name)}): {request.number} ')
            
            req = json_format.MessageToDict(request)
            print(req)
            # print(type(request))
            # print(dir(request))
            
            # print(f'result function_test: {function_test(len(request.name))}')

            # print(f'result test: {self.test(request.name)}')

            
            # сообщение, которое возращается клиенту (описанно в прото файле)
            return message.MsgResponse(
                status=200
            )
        # проверка на ошибки, параметры отправлять не обязательно
        except grpc.RpcError as exp:
            return message.MsgResponse(
                details=exp.details()
            )

    def Send(self, request, context):
        try:
            
            print(f'{request.tableName=}')
            print(f'{request.base64Str=}')
            print(f'{request.sourceId=}')
            req = json_format.MessageToDict(request)
            print(req)
            # print(type(request))
            # print(dir(request))
            return message.MsgResponse(
                status=200,
                details=''
            )
        # проверка на ошибки, параметры отправлять не обязательно
        except grpc.RpcError as exp:

            return message.MsgResponse(
                status=500,
                details=exp.details()
            )
        

        
  
    @classmethod
    def test(cls, name):
        return name.upper()


def serve():
    
    # конфигурация сервера
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_gprc.add_MsgServiceServicer_to_server(MsgServicer(), server)
    server.add_insecure_port('[::]:50051') #! порт 
    server.start() # запуск сервера

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
        

if __name__ == '__main__':
    serve()
