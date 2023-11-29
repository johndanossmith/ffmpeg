import ffmpeg 
(
    ffmpeg.input("a.mp4")
    .output('b.mp4')
    .run()
)