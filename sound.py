import pydub
from pydub import AudioSegment

class Sound_convert ():
    def __init__(self, output, input):
        self.output = output
        self.input = input
    
    def export (self, format):
        if self.output == '':
            self.output = self.input + format
        input_format = self.input.split('.')
        input_format = input_format[len(input_format)-1]
        if input_format == 'wav':
            sound = AudioSegment.from_wav(self.input)
        if input_format == 'mp3':
            sound = AudioSegment.from_mp3(self.input)
        if input_format == 'raw':
            sound = AudioSegment.from_raw(self.input)
        sound.export(self.output, format=format)


if __name__ == '__main__':
    a = Sound_convert('', 'C:/Users/thoma/OneDrive/Docs/ICAM/Hackathon/Yubaba/audios/Macroblank-VANDAL_CLUB-01_vandal.mp3')
    a.export('wav')