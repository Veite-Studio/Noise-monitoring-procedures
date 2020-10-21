
from pydub import AudioSegment

file_name = "song.wav"

# sound = AudioSegment.from_file(file_name, "wav")
sound = AudioSegment.from_file(r"C:\\Users\Administrator\Desktop\\沈逸帆\\Python\song.wav",delimiter="\t")




time = sound.duration_seconds
time = int(time)
print(time)
for i in range(1,100):
    
    # print(time / 10 * i )

    sounds = sound[time / 100 * i * 1000 : time / 100 * (i+1) * 1000]
    


    savename = "Python\\" + str(i) + ".wav"
    sounds += 0
    # sounds.export(savename, format="wav")


    

    loudness = sounds.dBFS

    print(loudness)