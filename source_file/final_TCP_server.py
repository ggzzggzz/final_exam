# 다중 클라이언트 접속 채팅 프로그램입니다
# 원래는 채팅은 너무 흔해서 다른것을 하려 했지만 아무리 생각해봐도 멀티스레드기반 다중접속이면
# 채팅밖에 생각이 안나서 했습니다.
# 그리고 GUI로 하면 좋을 것 같은데 GUI가 안되서 찾아보니 DISPLAY=:0.0에서 DISPLAY=:0으로도 바꿔보고
# 그렇게 해도 되지가 않아서 GUI부분은 포기했습니다.
import socket   # socket 관련 사용가능하게 하기 위해 사용
import threading    # threading 멀티스레드 기능 구현을 위해 사용
import sys # 시스템의 줄인말로 시스템을 종료시키기 위해 사용
# queue는 선입 선출 FIFO구조이다.
from queue import Queue     # queue를 이용해 다중 접속을 처리 데이터 저장을 위해 사용된다
def Send(connections, send_queue):  # 채팅을 보내는 메서드
    print('Thread Send Start') 
    while True: 
        try: #새롭게 추가된 클라이언트가 있을 경우 Send 쓰레드를 새롭게 만들기 위해 루프를 빠져나감 
            recv = send_queue.get() 
            if recv == 'Connection Changed': 
                print('Connection Changed') 
                break 

            #for 문을 돌면서 모든 클라이언트에게 동일한 메시지를 보냄 
            for conn in connections: 
                msg = 'Client' + str(recv[2]) + ' >> ' + str(recv[0]) 
                if recv[1] != conn: #client 본인이 보낸 메시지는 받을 필요가 없기 때문에 제외시킴 
                    conn.send(bytes(msg.encode()))  # 자기자신제외한 나머지 클라이언트한테 메시지를 보냄
                else: # client가 보낸 메시지가 정상적으로 나오는지 서버에서 확인
                    print(msg)
        except KeyboardInterrupt: # recv에서 queue에서 값을 못가져오면 오류가 발생한다. 또는 클라이언트에서 오류가 발생하면 예외처리
            print('Error Occured')
            sys.exit() # 예외처리발생하면 프로그램 종료

def Recv(conn, count, send_queue): 
    print('Thread Recv' + str(count) + ' Start') 
    while True:
        try:
            data = conn.recv(1024).decode() 
            send_queue.put([data, conn, count]) #각각의 클라이언트의 메시지, 소켓정보, 쓰레드 번호를 send로 보냄 
        except KeyboardInterrupt:
            print('Error Occured')
            sys.exit() #예외처리발생시 프로그램 종료

# TCP Echo Server 
if __name__ == '__main__': # 이 if문은 다른 메서드나 이런것과 구분하기 위해 main일때 실행되는 if문이다.
    print('Waiting Client Connecting...')
    send_queue = Queue()  # queue생성
    HOST = '' # 수신 받을 모든 IP를 의미 
    PORT = 9000 # 수신받을 Port 
    # TCP Server는 socket을 생성 후 bind를 하고 listen상태로 대기하다가 Client 쪽에서 connect요청이 오면
    # accept로 받아 데이터를 주고받는 형식이다.
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET, SOCK_STREAM은 TCP방식으로 하겠다는 의미
    server_sock.bind((HOST, PORT)) # 소켓에 수신받을 IP주소와 PORT를 설정 
    server_sock.listen(10) # 소켓 연결 대기 상태, 여기서 파라미터는 접속수를 의미
    count = 0  # 연결된 클라이언트의 수를 표시하기위한 변수
    connections = [] #연결된 클라이언트의 소켓정보를 리스트로 묶기 위함 
    while True: 
        count = count + 1 
        conn, addr = server_sock.accept() # 해당 소켓을 열고 대기 
        connections.append(conn) #연결된 클라이언트의 소켓정보 
        print('Connected ' + str(addr)) # 연결된 클라이언트의 주소값을 화면으로 출력


        #소켓에 연결된 모든 클라이언트에게 동일한 메시지를 보내기 위한 쓰레드(브로드캐스트) 
        #연결된 클라이언트가 1명 이상일 경우 변경된 connections 리스트로 반영 

        if count > 1: # 클라이언트 접속수가 1개 이상일 경우
            send_queue.put('Connection Changed')    # queue에 Connection Changed 라는 문자열을 넣는다.
            thread1 = threading.Thread(target=Send, args=(connections, send_queue,))  # 메시지를보내는 스레드 생성
            thread1.start() # 스레드 시작
        else: # 클라이언트 접속수가 1개나 없을때
            thread1 = threading.Thread(target=Send, args=(connections, send_queue,)) # 마찬가지로 스레드생성
            thread1.start() # 스레드 시작

        #소켓에 연결된 각각의 클라이언트의 메시지를 받을 쓰레드 
        thread2 = threading.Thread(target=Recv, args=(conn, count, send_queue,)) # 메시지를 받는 스레드
        thread2.start() # 스레드 시작

