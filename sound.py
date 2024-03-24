import ffmpeg

def audio_convert (input, output):
    ffmpeg.input(input).output(output).run()

if __name__ == '__main__':
    audio_convert('Macroblank.wav', 'Macroblank.mp3')
    