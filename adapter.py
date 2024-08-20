import time
from io import BytesIO
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from multiprocessing import Process
from interface import TTSInterface

class GTTSAdapter(TTSInterface):
    
    def __init__(self, language: str = 'pt', tld: str = 'com.br') -> None:
        self.language = language
        self.tld = tld
        self.audio_segment = None
        self.playback_process = None

    def speak(self, text: str) -> None:
        clean_text = self._clean_text(text)
        self._generate_speech(clean_text)
        self._play_audio_in_background()

    def stop(self) -> None:
        if self.playback_process and self.playback_process.is_alive():
            self._stop_audio()
        else:
            raise ValueError("No audio is currently playing.")

    def _clean_text(self, text: str) -> str:
        return text.strip().replace('\n', ' ').replace('\r', '').replace('\t', '').replace('\v', '').replace('\f', '').replace('\b', '').replace('*', '')

    def _generate_speech(self, text: str) -> None:
        mp3 = BytesIO()
        tts = gTTS(text=text, lang=self.language, tld=self.tld)
        tts.write_to_fp(mp3)
        mp3.seek(0)
        self.audio_segment = AudioSegment.from_file(mp3, format="mp3")
        mp3.close()

    def _play_audio(self) -> None:
        if self.audio_segment:
            play(self.audio_segment)
        else:
            raise ValueError("No audio segment to play. Generate speech first.")

    def _play_audio_in_background(self) -> None:
        if self.playback_process and self.playback_process.is_alive():
            self._stop_audio()

        self.playback_process = Process(target=self._play_audio)
        self.playback_process.start()

    def _stop_audio(self) -> None:
        if self.playback_process.is_alive():
            self.playback_process.terminate()
            self.playback_process.join()
            self.playback_process = None
