# 🚀 Chaos-Driven DevOps Onboarding with Chaos Mesh

Train new DevOps engineers by simulating real-world incidents in a safe, local Kubernetes environment using Chaos Mesh.

---

## 🧰 Prerequisites

Ensure the following are installed:

- Docker
- [`kind`](https://kind.sigs.k8s.io/)
- `kubectl`
- `helm` (v3+)

---

## ⚙️ Step 1: Create a Local Kubernetes Cluster (Kind)

```bash
kind create cluster --name chaos-demo
kubectl cluster-info --context kind-chaos-demo
```
## ⚙️ Step 2: Install Chaos Mesh with Helm
```
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm repo update

kubectl create ns chaos-mesh

helm install chaos-mesh chaos-mesh/chaos-mesh \
  -n chaos-mesh \
  --set dashboard.create=true \
  --set chaosDaemon.runtime=containerd \
  --set chaosDaemon.socketPath=/run/containerd/containerd.sock
```
Access the Chaos Mesh Dashboard:
```
kubectl port-forward -n chaos-mesh svc/chaos-dashboard 2333:2333
# Open http://localhost:2333 in your browser
```
## ⚙️ Step 3: Deploy a Sample App
```bash

kubectl create deployment web --image=nginx
kubectl expose deployment web --port=80 --type=ClusterIP
```
## 🔥 Step 4: Run Chaos Experiments
✅ A. DNS Blackhole Simulation
dns-blackhole.yaml:

```yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: dns-blackhole
spec:
  action: deny
  mode: one
  selector:
    namespaces:
      - default
    labelSelectors:
      app: web
  direction: to
  target:
    externalTargets:
      - "www.google.com"
  duration: "30s"
```
Apply:

```kubectl apply -f dns-blackhole.yaml```
✅ B. Broken Deployment (Crash on Startup)
broken-deploy.yaml:

```yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: broken-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: broken-app
  template:
    metadata:
      labels:
        app: broken-app
    spec:
      containers:
        - name: app
          image: nginx:broken-tag
```
Apply:

```kubectl apply -f broken-deploy.yaml```
✅ C. API Latency Simulation
api-latency.yaml:

```yaml

apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: api-latency
spec:
  action: delay
  mode: one
  selector:
    labelSelectors:
      app: web
  delay:
    latency: '5000ms'
  duration: '30s'
  direction: to
```
Apply:

```bash
kubectl apply -f api-latency.yaml
```
🧹 Cleanup
```
kubectl delete networkchaos dns-blackhole api-latency
kubectl delete deployment broken-app web
kubectl delete service web
kind delete cluster --name chaos-demo
```
