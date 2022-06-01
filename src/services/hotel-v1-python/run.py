from app import app
from ddtrace.runtime import RuntimeMetrics


if __name__ == "__main__":
    RuntimeMetrics.enable()
    app.run(host="0.0.0.0", port=9101)
