from abc import ABC, abstractmethod

class TTSInterface(ABC):
    
    @abstractmethod
    def speak(self, text: str) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass
    