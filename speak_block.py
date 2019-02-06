import pyttsx3
from nio import TerminatorBlock
from nio.properties import IntProperty, FloatProperty, StringProperty, \
                           VersionProperty


class Speak(TerminatorBlock):

    message = StringProperty(title="Message to speak",
                             default="{{ $message }}")
    rate = IntProperty(title="Words per Minute (1-200)",
                       default=200,
                       advanced=True)
    volume = FloatProperty(title="Volume (0-1.0)",
                           default=1.0,
                           advanced=True)
    version = VersionProperty('0.2.0')

    def __init__(self):
        super().__init__()
        self.engine = None

    def configure(self, context):
        super().configure(context)
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", self.rate())
        self.engine.setProperty("volume", self.volume())

    def process_signals(self, signals):
        for signal in signals:
            msg = self.message(signal)
            self.engine.say(msg)
        self.engine.runAndWait()

    def stop(self):
        self.engine.stop()
        super().stop()
