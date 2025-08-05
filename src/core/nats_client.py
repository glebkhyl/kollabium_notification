from core.config import NATS_URL
from faststream import FastStream
from faststream.nats import JStream, NatsBroker

broker = NatsBroker(NATS_URL)
stream = JStream(name="logs")
app = FastStream(broker)
