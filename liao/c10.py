#第三方模块安装及使用
#每间隔多长时间执行一次操作任务
import schedule
import time


def job():
    print('哈哈----------------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
