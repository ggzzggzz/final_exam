# Client는 서버에 접속해서 채팅만 보내면 되기때문에 Server의 코드에 비해서는 간단하다.
import socket # TCP 연결을 하기 위해
import threading # 스레드 사용을 하기 위해
import sys # 시스템의 줄인말로 시스템종료를 위해 사용함
def Send(client_sock): # 서버로 데이터를 송신하기 위한 메서드
    while True:
        try:
            send_data = bytes(input().encode()) # 입력한 값 인코딩 작업
            if not send_data:
                break #만약 send_data값에 아무것도 들어가지 않는다면 반복문 탈출
            client_sock.send(send_data) # Client -> Server 데이터 송신 
        except KeyboardInterrupt:
            print('Error Occured')
            sys.exit() #예외발생하면 프로그램 종료

def Recv(client_sock): # 서버로부터 데이터를 수신하기 위한 메서드
    while True: 
        try:
            recv_data = client_sock.recv(1024).decode() # Server -> Client 데이터 수신 
            if not recv_data: #만약 받은 데이터가 없으면 반복문 탈출 
                break
            print(recv_data) # 받은 데이터를 출력
        except KeyboardInterrupt:
            print('Error Occured')
            sys.exit() #예외발생하면 프로그램 종료

#TCP Client 
if __name__ == '__main__': # 이 프로그램 실행 시 main실행 Send나 Recv가 무한반복이기 때문에 main에는 반복문 필요 X
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP 방식의 소켓
    Host = 'localhost' #통신할 대상의 IP 주소, localhost는 자기 자신의 주소
    Port = 9000 #통신할 대상의 Port 주소 
    client_sock.connect((Host, Port)) #서버로 연결시도 
    print('Connecting to ', Host, Port) #주소와 포트번호를 찍어본다. 

    #Client의 메시지를 보낼 쓰레드 
    thread1 = threading.Thread(target=Send, args=(client_sock, )) # 스레드 생성
    thread1.start() # 스레드 시작

    #Server로 부터 다른 클라이언트의 메시지를 받을 쓰레드 
    thread2 = threading.Thread(target=Recv, args=(client_sock, )) # 스레드 생성
    thread2.start() # 스레드 시작

