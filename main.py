import random, threading, os, time, datetime

answer = False
right = True
try_ = 0
already_fin = False
all_thread_added = False

class test(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global already_fin, answer, right, try_
        
        while not all_thread_added:
            time.sleep(0)
        
        while not answer:
            try_ += 1
            right = True
            for i in range(1, 7):
                if not right:
                    break
                elif i == 3:
                    x_n = 22
                    for y in range(10):
                        if random.randrange(0, 1000) != 1:
                            print('[{}][{}]실패. 시도횟수: {}'.format(self.name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),try_))
                            right = False
                            break
                elif i == 4:
                    x_n = 21
                elif i ==5:
                    x_n = 41
                elif i ==6:
                    x_n = 31
                else:
                    x_n = 46
                        
                for x in range(1, x_n):
                    if random.randrange(1,6) != 1:
                        if not already_fin:
                            print('[{}][{}]실패. 시도횟수: {}'.format(self.name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),try_))
                        right = False
                        break
                
                if i == 6 and right:
                    answer = True
                    break
            
            if answer:
                break
        
        if not already_fin:
            already_fin = True
            print('\n\n\n[{}][{}]성공!! 시도횟수: {}'.format(self.name,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),try_))
            print('실행시간: {}초'.format(time.time() - start_time:.2f))
        pid = os.getpid()
        os.kill(pid, 2)


thread_num = input("스레드 수를 입력하세요: ")
num_len = len(thread_num)
for i in range(int(thread_num)):
    thread_count ='0'*(num_len - len(str(i+1)))+str(i+1)
    t=test('Thread-{}'.format(thread_count))
    t.start()
    print('thread-{} started'.format(thread_count))
    
print("all thread Created.")
print("program will start after 3 seconds.")
time.sleep(3)

all_thread_added = True
start_time = time.time()