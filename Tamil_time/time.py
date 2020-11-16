from datetime import datetime
import subprocess

t = datetime.now()
m = t.minute
h = t.hour
hm = t.hour%12+1
am = h<=12
mtst = str(m)+'.mp3'
mst = str(m%10)+'.mp3'
hst = str(hm)+'.mp3'
htst = str(h)+'.mp3'
subprocess.Popen(['mpg123', '-q', 'neram_tharpodhu.mp3']).wait()
if am:
    subprocess.Popen(['mpg123', '-q', 'kaalai.mp3']).wait()
    subprocess.Popen(['mpg123', '-q', htst]).wait()
else:
    subprocess.Popen(['mpg123', '-q', 'maalai.mp3']).wait()
    subprocess.Popen(['mpg123', '-q', hst]).wait()

if m<=20 or m==30 or m==40 or m==50 or m==60:
    subprocess.Popen(['mpg123', '-q', mtst]).wait()
elif m<30:
    subprocess.Popen(['mpg123', '-q', '2_.mp3']).wait()
    subprocess.Popen(['mpg123', '-q', mst]).wait()
elif m<40:
    subprocess.Popen(['mpg123', '-q', '3_.mp3']).wait()
    subprocess.Popen(['mpg123', '-q', mst]).wait()
elif m<50:
    subprocess.Popen(['mpg123', '-q', '4_.mp3']).wait()
    subprocess.Popen(['mpg123', '-q', mst]).wait()
elif m<60:
    subprocess.Popen(['mpg123', '-q', '5_.mp3']).wait()
    subprocess.Popen(['mpg123', '-q', mst]).wait()
