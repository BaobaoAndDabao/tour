import  datetime
class Utils:
    def getCurrentTimeStr(self):
        now_time = datetime.datetime.now()
        nowStr=datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
        print(nowStr)
        return nowStr