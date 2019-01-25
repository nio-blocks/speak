import pyttsx3
from nio import TerminatorBlock
from nio.properties import StringProperty, VersionProperty


class Speak(TerminatorBlock):

    message = StringProperty(title="Message to speak",
                             default="{{ $message }}")
    version = VersionProperty('0.1.0')

    def __init__(self):
        super().__init__()
        self.engine = None

    def configure(self, context):
        super().configure(context)
        self.engine = pyttsx3.init()
        self.engine.setProperty("volume", 1)

    def process_signals(self, signals):
        for signal in signals:
            msg = self.message(signal)
            self.engine.say(msg)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()
        super().stop()
