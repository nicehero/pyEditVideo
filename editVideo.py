import os
inputfile = "Tokyo-Hot-n0440.mp4"
audiofile = "input.mp3"
outfile = "out_" + inputfile.split(".")[0] + ".mp4"
command = ""

#啥也不干
#command = f'ffmpeg -hwaccel auto -i {inputfile} {outfile}'

#旋转
#command = f'ffmpeg -hwaccel auto -i {inputfile} -vf transpose=1 {outfile}'

#剪辑
#command = f'ffmpeg -hwaccel auto -i {inputfile} -ss 00:00:03 -t 00:01:27 {outfile}'

#水印
#command = f'ffmpeg -hwaccel auto -i {inputfile}\
# -i ./mask.png\
# -lavfi "overlay=enable=\'mod(t,10)\':y=\'100*mod(t,10)+50\'"\
# {outfile} -y'

#加音频
#command = f'ffmpeg -i {inputfile}\
# -i {audiofile} -map 0 -map 1:a -c:v copy\
# {outfile} -y'

#封面
#os.system(f'ffmpeg -i {inputfile} -ss 00:00:08 -frames:v 1 out.png')
#command = f'ffmpeg -i {inputfile} -i out.png -map 0 -map 1 -c copy -c:v:1 png -disposition:v:1 attached_pic {outfile}'

#去封面
#command = f'ffmpeg -i {inputfile} -c copy -map 0:V -map 0:a {outfile}'

os.system(command)