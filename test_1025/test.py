# 10초가 지나면 bye 출력
import time

print('hi')
time.sleep(10) # 요청이 도착할때까지 기다렸다가 response에 저장하고 
print('bye') # 그 다음을 실행


# JS
# 요청이 도착하는 것을 기다리지 않고(Web API 던져놓음)
# 그리고 그냥 다음을 실행해버림
# 그리고 도착하면 무엇인가를 함