from adapter import GTTSAdapter
from interface import TTSInterface

class TTSFactory:
    
    def get_tts(self, tts_type: str = 'gtts', language: str = 'pt', tld: str = 'com.br') -> TTSInterface:
        if tts_type == 'gtts':
            return GTTSAdapter(language=language, tld=tld)
        else:
            raise ValueError("Invalid TTS type")
