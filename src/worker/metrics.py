from prometheus_client import Counter, start_http_server

logs_publish_total = Counter(
    "logs_publish_total",
    "Count of log messages published",
    labelnames=("subject", "channel", "kind"),
)

logs_publish_failed_total = Counter(
    "logs_publish_failed_total",
    "Count of failed log publishes",
    labelnames=("subject", "error"),
)

logs_consume_total = Counter(
    "logs_consume_total",
    "Count of consumed log messages",
    labelnames=("subject", "kind"),
)

logs_consume_failed_total = Counter(
    "logs_consume_failed_total",
    "Count of failed log message processing",
    labelnames=("subject", "kind", "error"),
)


def start_metrics_server(port: int = 9100):
    start_http_server(port)
