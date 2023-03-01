import time

from macls.utils.record import RecordAudio

s = input('请输入计划录音秒数：')
record_seconds = int(s)
save_path = "dataset/save_audio/%s.wav" % str(int(time.time()*1000))

record_audio = RecordAudio()
record_audio.record(record_seconds=record_seconds,
                    save_path=save_path)

print('文件保存在：%s' % save_path)
