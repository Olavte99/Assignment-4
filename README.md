# Experiment Setup Guide

This is what i used to run and test my app on. The instructions provided here are specifically for Ubuntu systems.

## Prerequisites

Ensure that `kubectl` is installed on your system. If not, follow these steps to install it:

```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

## Installing K3s with Calico

To install K3s with Calico networking, execute the following command:

```bash
curl -sfL https://get.k3s.io | K3S_KUBECONFIG_MODE="644" INSTALL_K3S_EXEC="--flannel-backend=none --cluster-cidr=192.168.0.0/16 --disable-network-policy --disable=traefik" sh -
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/tigera-operator.yaml
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/custom-resources.yaml
```

## Testing

To test the setup, monitor the Kubernetes pods across all namespaces:

```bash
watch kubectl get pods --all-namespaces
```

Also, verify the nodes in the cluster:

```bash
kubectl get nodes -o wide
```

## Deploying ArgoCD Manifests

Once Kubernetes and `kubectl` are up and running, deploy the ArgoCD manifests located under `k8s/argocd` with the following command:

```bash
kubectl apply -k .
```

## Accessing ArgoCD

After ArgoCD is deployed and running on port 30520, extract the password using the following command:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

## Note

This project is not complete due to time constraints.
