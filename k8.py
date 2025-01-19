from kubernetes import client, config

# Load kube config (e.g., from local kubeconfig file)
config.load_kube_config()

# Instantiate the CoreV1Api
v1 = client.CoreV1Api()

# List pods in a specific namespace
namespace = "nginx"  # Replace with your desired namespace
pods = v1.list_namespaced_pod(namespace)

# Print the names of the pods
for pod in pods.items:
    print(pod.metadata.name)
