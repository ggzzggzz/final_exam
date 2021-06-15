# final_exam

## 개요

이 프로그램을 만들게 된것은 강의영상을 보면 보통은 채팅을 많이 하는 예제를 보여주었는데 이를 활용하여 더 많은 사용자가 접속 가능한 채팅프로그램을 만들기 위함이다.

### 목적

이 프로그램을 만든 목적은 여려명의 사용자가 접속하여 채팅을 하기 위함이다.

이 채팅프로그램은 서버가 여려명의 사용자를 받고 그 사용자들을 첫번째 들어온 순서부터 Client1라고 이름을 지어준뒤 이 사람이 채팅을 쳤을때 다른 모든 클라이언트에게 채팅이 간다.

#### 아쉬운점

코드를 보시면 예외처리를 다 했는데 KeyboardInterrupt로 채팅을 종료하게 했지만 문제점은 예외처리를 해도 한개는 잘 나가지는데 다른 클라이언트나 서버에 Client1 >> 이런게 여러번 찍히고 나가진다는 것이다.

그리고 GUI를 쓰려했지만 이번 수업에서 했던 예제도 되지를 않아 찾아봤지만 DISPLAY=:0로 바꾸라고 해서 바꿔봤지만 계속 오류가 떴었다.

그래서 GUI를 쓰지 못하고 원래 하던대로 콘솔에서 하는 것으로 결정을 했던 점이 아쉬웠다.

##### 실행화면
![채팅서버 클라이언트 접속후](https://user-images.githubusercontent.com/71123177/121987791-26a46180-cdd4-11eb-93c0-fc00ca7a1d4b.PNG)
![채팅서버 전체화면](https://user-images.githubusercontent.com/71123177/121987829-358b1400-cdd4-11eb-9e84-0fc04e89ec5f.PNG)
![채팅서버 채팅후](https://user-images.githubusercontent.com/71123177/121987843-3b80f500-cdd4-11eb-895b-585e18f92c1b.PNG)
![채팅클라이언트1](https://user-images.githubusercontent.com/71123177/121987850-3e7be580-cdd4-11eb-8c80-caa152b2c3d2.PNG)
![채팅클라이언트2](https://user-images.githubusercontent.com/71123177/121987855-4176d600-cdd4-11eb-8b0c-d3c54d97ac75.PNG)
![채팅클라이언트3](https://user-images.githubusercontent.com/71123177/121987860-450a5d00-cdd4-11eb-9652-251b7582679d.PNG)
![채팅서버 종료후 전체화면](https://user-images.githubusercontent.com/71123177/121987864-49367a80-cdd4-11eb-8be3-acec7e5d9694.PNG)
