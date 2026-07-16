# Integrate Instana with a Microservice Application on OpenShift

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=nodedotjs&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![OpenShift](https://img.shields.io/badge/OpenShift-EE0000?style=flat&logo=redhatopenshift&logoColor=white)
![IBM Instana](https://img.shields.io/badge/IBM%20Instana-052FAD?style=flat&logo=ibm&logoColor=white)

This project demonstrates how to integrate [IBM Instana](https://www.instana.com/) — a fully automated Enterprise Observability and Application Performance Management (APM) platform — with a polyglot microservice travel application deployed on Red Hat OpenShift. By instrumenting each service with Instana collectors and deploying through OpenShift, the pattern provides end-to-end visibility across a realistic, multi-language microservice architecture. Synthetic traffic is generated using [Puppeteer](https://developers.google.com/web/tools/puppeteer/) to exercise the system, and the resulting telemetry is analyzed on the Instana dashboard, making this an ideal reference implementation for teams adopting cloud-native observability on OpenShift.

## Features

- Full observability stack using IBM Instana across a polyglot microservice application
- Auto-instrumentation with `@instana/collector` injected into Node.js services
- Distributed tracing supplemented by DataDog `dd-trace` for cross-service correlation
- Prometheus metrics endpoint exposed per service for additional monitoring flexibility
- Containerized deployment pipeline — Docker images built and pushed to DockerHub, then deployed via OpenShift CLI (`oc`)
- Declarative OpenShift deployment manifests with Instana environment variable configuration (`INSTANA_AGENT_HOST`, `INSTANA_SERVICE_NAME`, etc.)
- Synthetic traffic generation with Puppeteer to produce real observability data for analysis
- Based on the open-source [Bee Travels](https://bee-travels.github.io/) reference application

## Tech Stack

- **Languages:** JavaScript (Node.js), Python, Shell, YAML, HTML
- **Frameworks / Libraries:** Express, React, FastAPI / Flask (hotel service), Pino (logger), Swagger UI
- **Observability:** IBM Instana (`@instana/collector`), DataDog `dd-trace`, Prometheus metrics
- **Containerization:** Docker, DockerHub
- **Orchestration:** Red Hat OpenShift, `oc` CLI
- **Traffic Generation:** Puppeteer
- **Package Management:** npm, pip

## Services

| Service | Language | Version |
|---|---|---|
| Destination | Node.js | v1 |
| Car Rental | Node.js | v1 |
| Hotel | Python | v1 |
| Currency Exchange | Node.js | — |
| UI | Node.js / React | — |

## Getting Started

### Prerequisites

- Red Hat OpenShift cluster with `oc` CLI configured
- Docker and DockerHub account
- IBM Instana agent deployed on the cluster
- Node.js and npm installed locally
- Python 3 and pip installed locally

### 1. Fork and Clone

```bash
git clone https://github.com/katkhedepushpak/instana-openshift.git
cd instana-openshift
```

### 2. Install Node.js Dependencies

```bash
npm install
```

### 3. Install Python Dependencies

If a `requirements.txt` is present in the hotel service directory:

```bash
pip install -r src/services/hotel-v1-python/requirements.txt
```

### 4. Configure Instana

Set the required Instana environment variables. These are referenced in the OpenShift deployment manifests under `config/`:

```bash
export INSTANA_AGENT_HOST=<your-instana-agent-host>
export INSTANA_SERVICE_NAME=<your-service-name>
```

Update the values in the relevant YAML files under `config/` before deploying.

### 5. Build and Deploy to OpenShift

The `build-and-deploy.sh` script builds Docker images for all microservices, pushes them to DockerHub, and deploys them to your OpenShift cluster:

```bash
chmod +x build-and-deploy.sh
./build-and-deploy.sh
```

Ensure you are logged in to both DockerHub (`docker login`) and your OpenShift cluster (`oc login`) before running this script.

## Usage

### Generate Traffic

Once all services are running on OpenShift, use Puppeteer to generate synthetic traffic against the UI service:

```bash
node scripts/puppeteer.js  # path may vary
```

### Analyze in Instana

Open your Instana dashboard and navigate to the **Applications** or **Services** view to inspect:

- Service dependency maps
- Request latency and error rates
- Distributed traces across Node.js and Python services
- Infrastructure health of OpenShift pods and nodes

Refer to the full IBM Developer code pattern for a detailed walkthrough:
[https://developer.ibm.com/patterns/integrating-instana-with-microservice-app-on-openshift/](https://developer.ibm.com/patterns/integrating-instana-with-microservice-app-on-openshift/)

## Screenshots

_Add screenshots of the Instana dashboard, service dependency map, and distributed trace views here._

<!-- Example:
![Instana Service Map](docs/screenshots/service-map.png)
![Distributed Trace View](docs/screenshots/trace-view.png)
-->

## Project Structure

```
instana-openshift/
├── config/                  # OpenShift deployment YAML manifests
├── src/
│   └── services/
│       ├── destination-v1/  # Node.js destination service
│       ├── carrental-v1/    # Node.js car rental service
│       ├── currencyexchange/ # Node.js currency exchange service
│       ├── hotel-v1-python/ # Python hotel service
│       └── ui/              # Node.js/React frontend
├── build-and-deploy.sh      # Build and deploy automation script
└── package.json
```

## References

- [IBM Developer Code Pattern](https://developer.ibm.com/patterns/integrating-instana-with-microservice-app-on-openshift/)
- [Instana Documentation](https://www.instana.com/docs/)
- [Bee Travels Project](https://bee-travels.github.io/)
- [OpenShift CLI Reference](https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html)

## Author

Built by [Pushpak Vijay Katkhede](https://katkhedepushpak.github.io)
