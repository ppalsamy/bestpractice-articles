# 🚀 Chaos-Driven DevOps Onboarding with Chaos Mesh

Train new DevOps engineers by simulating real-world incidents in a safe, local Kubernetes environment using Chaos Mesh.

---

## 🧰 Prerequisites

Ensure the following are installed:

- Docker
  - `brew install --cask docker`
- [`kind`](https://kind.sigs.k8s.io/)
  - `brew install kind`
- `kubectl`
  - `brew install kubectl`
- `helm` (v3+)
   - `brew install helm` 

---

## ⚙️ Step 1: Create a Local Kubernetes Cluster (Kind)

```bash
kind create cluster --name dev-cluster
kubectl cluster-info --context kind-dev-cluster
```
## ⚙️ Step 2: Install Chaos Mesh with Helm
1. Install Chaos Mesh
```
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm repo update
```
2. Create Namespace
```
kubectl create ns chaos-mesh
```
3. Create Chaos Mesh Dashboard
```
helm install chaos-mesh chaos-mesh/chaos-mesh \
  -n chaos-mesh \
  --set dashboard.create=true \
  --set chaosDaemon.runtime=containerd \
  --set chaosDaemon.socketPath=/run/containerd/containerd.sock
```
4. Create Service Account to access Chaos Mesh Dashboard:
   
   Follow the steps [provided here](https://chaos-mesh.org/docs/manage-user-permissions/)
6. Access the Chaos Mesh Dashboard (localhost:2333):
```
kubectl port-forward -n chaos-mesh svc/chaos-dashboard 2333:2333
# Open http://localhost:2333 in your browser
```
## ⚙️ Step 3: Install Prometheus + Grafana (Operator)

  ```
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update

    # Create a namespace for monitoring
    kubectl create ns monitoring

    # Install kube-prometheus-stack
    helm install kube-prometheus prometheus-community/kube-prometheus-stack -n monitoring \
      --set grafana.service.type=NodePort \
      --set grafana.service.nodePort=30001 \
      --set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false 

   ```
That serviceMonitorSelectorNilUsesHelmValues=false is important—it lets Prometheus discover ServiceMonitor objects from other namespaces

ServiceMonitor setup (serviceMonitor_all.yaml)
```
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: all-services
  namespace: monitoring
spec:
  selector:
    matchLabels:
      monitoring: enabled
  namespaceSelector:
    any: true
  endpoints:
    - port: http
      path: /metrics
      interval: 15s
```
apply it
```
kubectl apply -f servicemonitor_all.yaml

```
   Access Grafana - localhost:3000
   ```
   kubectl port-forward -n monitoring svc/kube-prometheus-grafana 3000:80
   ```
   Get Admin Creds
   ```
   kubectl get secret kube-prometheus-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
   ```
## ⚙️ Step 4: Deploy a Sample App

Below steps to deploy app using [stefanprodan/podinfo](https://github.com/stefanprodan/podinfo/tree/master?tab=readme-ov-file#helm)
```
helm repo add podinfo https://stefanprodan.github.io/podinfo

#Create test namespace
kubectl create ns test

#install frontend podinfo in test namespace
helm upgrade --install --wait frontend \
--namespace test \
--set replicaCount=2 \
--set backend=http://backend-podinfo:9898/echo \
 --set service.labels.monitoring=enabled \
podinfo/podinfo

helm test frontend --namespace test

#install backend podinfo in test namespace
helm upgrade --install --wait backend \
--namespace test \
--set redis.enabled=true \
 --set service.labels.monitoring=enabled \
podinfo/podinfo

``` 
Access Frontend - localhost:8080
```
   kubectl port-forward -n monitoring svc/frontend-podinfo 8080:9898
```
Access Backend - localhost:8090
```
   kubectl port-forward -n monitoring svc/frontend-podinfo 8090:9898
```
## 🔥 Step 5: Run Chaos Experiments
Follow the experiment 
~~~
https://chaos-mesh.org/docs/simulate-network-chaos-on-kubernetes/
~~~

🧹 Cleanup
```
kubectl delete networkchaos dns-blackhole api-latency
kubectl delete deployment broken-app web
kubectl delete service web
kind delete cluster --name chaos-demo
```
