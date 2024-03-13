from io import BytesIO
from gtts import gTTS
from pydub import AudioSegment, playback

class TTS:
    def __init__(self):
        pass

    def speak(self, text):
        mp3 = BytesIO()
        tts = gTTS(text=self.__clean_text(text), lang='pt', tld='com.br')
        tts.write_to_fp(mp3)
        mp3.seek(0)

        audio_segment = AudioSegment.from_file(mp3, format="mp3")
        playback.play(audio_segment)
        mp3.close()
        return
        
    def __clean_text(self, text):
        return text.strip().replace('\n', ' ').replace('\r', '').replace('\t', '').replace('\v', '').replace('\f', '').replace('\b', '').replace('*', '')
