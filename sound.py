import pydub
import ffmpeg
from pydub import AudioSegment

class Sound_convert ():
    def __init__(self, output, input):
        self.output = output
        self.input = input
    
    def export (self, output_format):
        input_format = self.input.split('.')
        if self.output == '':
            self.output = str(self.input[0]) + output_format
        input_format = input_format[len(input_format)-1]
        sound = AudioSegment.from_file(self.input, format=input_format)
        sound.export(self.output, format=output_format)

    def ffmaudio (self):
        ffmpeg.input("C:/Users/thoma/OneDrive/Docs/ICAM/Hackathon/Yubaba/Macroblank.mp3").output('C:/Users/thoma/OneDrive/Docs/ICAM/Hackathon/Yubaba/Macroblank.wav').run()
if __name__ == '__main__':
    a = Sound_convert('', 'Macroblank.mp3')
    a.ffmaudio()