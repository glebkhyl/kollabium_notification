from faststream import FastStream

from core.nats_client import broker
from worker.metrics import start_metrics_server
from worker.routers.airdrop import router as airdrop_router
from worker.routers.donats import router as donat_router

fs = FastStream(broker)
broker.include_router(airdrop_router)
broker.include_router(donat_router)


@fs.on_startup
async def setup_metrics():
    start_metrics_server(9100)
    print("✅ Prometheus metrics server started on :9100")
