import os
import ffmpeg

def trim(in_file,out_file,start,end):
    if os.path.exists(out_file):
        os.remove(out_file)

    probe_result = ffmpeg.probe(in_file)
    probe_result.get()

trim("test_videos/input.mp4","test_videos/output.mp4",10,18)