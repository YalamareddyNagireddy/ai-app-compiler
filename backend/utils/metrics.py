class Metrics:
    def __init__(self):
        self.total_requests = 0
        self.failed_requests = 0
        self.repair_count = 0
        self.total_latency = 0

    def log_request(self, success: bool, latency: float, repair_used: bool = False):
        self.total_requests += 1
        self.total_latency += latency

        if not success:
            self.failed_requests += 1

        if repair_used:
            self.repair_count += 1

    def get_report(self):
        success_rate = (
            (self.total_requests - self.failed_requests) / self.total_requests
            if self.total_requests > 0 else 0
        )

        avg_latency = (
            self.total_latency / self.total_requests
            if self.total_requests > 0 else 0
        )

        return {
            "total_requests": self.total_requests,
            "failed_requests": self.failed_requests,
            "repair_count": self.repair_count,
            "success_rate": round(success_rate * 100, 2),
            "avg_latency_ms": round(avg_latency, 2)
        }