import grpc
from time import time
 

import data.protof.message_pb2 as message
import data.protof.message_pb2_grpc as message_gprc

message64 = "John"

def run():

    req = 1
    start = time()
    for _ in range(req):

        try: 
        
            with grpc.insecure_channel('localhost:50051') as channel:
                stub = message_gprc.MsgServiceStub(channel)
                
                response = stub.GetMsg(message.MsgRequest(
                    name=message64,
                    number=5
                ))
            
            print(f"Client received: {response.status}") # сообщение от сервера MsgResponce
            # print(f'response: {response}')
            # print(dir(response))

            eta = int((time() - start) * 1000)
            print(f'{eta=}ms for {req} requests')
        except grpc.RpcError as exp:
            
            # основные значения в traceback, которые можнов вывести
            print(exp.details())
            print(exp.code())
            print(exp.debug_error_string())
            
            # print(dir(exp))
    
    
    # eta = int((time() - start) * 1000)
    # print(f'{eta=}ms for {req} requests')
    
    # while True:
    #     start = time()
    #     with grpc.insecure_channel('localhost:50051') as channel:
    #         stub = msg_pb2_grpc.MsgServiceStub(channel)
    #         response = stub.GetMsg(msg_pb2.MsgRequest(name='world'))
    #     print("Client received: " + response.msg)
    #     eta = int((time() - start))
    #     print(f'{eta=}')


def send_run():

    try: 
    
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = message_gprc.MsgServiceStub(channel)
            
            response = stub.Send(message.SendRequest(
                tableName='sercher',
                base64Str='asfja;sdhbqerubn',
                sourceId='camera2'
            ))
        
        if response.status == 200:
            print(f"Client received: {response.status}") # сообщение от сервера MsgResponce
        
        # print(f'response: {response}')
        # print(dir(response))

        
    except grpc.RpcError as exp:
        
        
        # основные значения в traceback, которые можнов вывести
        print(f'Error: {exp.details()}')
        # print(exp.code())
        # print(exp.debug_error_string())

if __name__ == '__main__':
    send_run()
    # run()
