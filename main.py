import random, threading, os, time, datetime

answer = False
is_answer = True
attempt = 0
finished = False
all_thread_added = False

class test(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global finished, answer, is_answer, attempt
        
        #모든 스레드 추가될때까지 대기
        while not all_thread_added:
            time.sleep(0)
        
        #시뮬레이션 시작
        while not answer:
            attempt += 1
            is_answer = True
            for i in range(1, 7):
                if not is_answer:
                    break
                elif i == 3: #과목: 수학
                    number_of_questions = 22
                    for y in range(10): #단답형
                        if random.randrange(0, 1000) != 1:
                            print('[{}][{}]실패. 시도횟수: {}'.format(self.name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),attempt))
                            is_answer = False
                            break
                elif i == 4:#과목: 한국사
                    number_of_questions = 21
                elif i ==5:#과목: 탐구
                    number_of_questions = 41
                elif i ==6:#과목: 제2외국어
                    number_of_questions = 31
                else: #나머지 과목들
                    number_of_questions = 46
                
                if is_answer: #수학 단답형 틀렸을때 그냥 넘어가도록.
                    for x in range(1, number_of_questions):
                        if random.randrange(1,6) != 1:
                            if not finished: #성공한 후 도배 방지
                                print('[{}][{}]실패. 시도횟수: {}'.format(self.name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),attempt))
                            is_answer = False
                            break
                
                if i == 6 and is_answer:
                    answer = True
                    break
            
            if answer:
                break
        #성공
        finished = True
        print('\n\n\n[{}][{}]성공!! 시도횟수: {}'.format(self.name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),attempt))
        print('실행시간: {:.2f}초'.format(time.time() - start_time))
        
        #모든 스레드 종료
        pid = os.getpid()
        os.kill(pid, 2)


#스레드 생성
thread_num = input("스레드 수를 입력하세요: ")
thread_num_len = len(thread_num)
for i in range(int(thread_num)):
    thread_count ='0'*(thread_num_len - len(str(i+1)))+str(i+1)
    t=test('Thread-{}'.format(thread_count))
    t.start()
    print('thread-{} started'.format(thread_count))
    
#스레드 생성 완료
print("all thread Created.")
print("program will start after 3 seconds.")
time.sleep(3)

all_thread_added = True
start_time = time.time()