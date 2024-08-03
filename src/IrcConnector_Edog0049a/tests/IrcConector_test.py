import pytest
from IrcConnector_Edog0049a.IrcConnector import IrcConnector
import time
   
ircTestClient = IrcConnector("127.0.0.1",8888, tokenRefillTime=5)
def test_Send_method():
    
    assert(ircTestClient._queue.empty() == True)
    ircTestClient.send("test")
    assert(ircTestClient._queue.empty() == False)
    ircTestClient._queue.get()
    assert(ircTestClient._queue.empty() == True)

def test_queue_max():
    max=ircTestClient._queue.maxsize
    for i in range(max):
        ircTestClient.send(f"test Msg {i}")
    assert(ircTestClient._queue.full()==True)

def test_tokenbucket():
    i = 0
    while ircTestClient._queue.not_empty and ircTestClient._tokenBucket.usetoken:
        data = ircTestClient._queue.get()
        assert(data == f"test Msg {i}\r\n")
        i+=1
    assert(ircTestClient._tokenBucket.isEmpty==True)
    assert(ircTestClient._queue.qsize()==30)
    while ircTestClient._tokenBucket.isEmpty:
        time.sleep(1)
        ircTestClient._tokenBucket._fillBucket()
    assert(ircTestClient._tokenBucket.isFull)   
    

    

    




