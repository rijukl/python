from kubernetes import client, config

# Load the Kubernetes configuration (e.g., from ~/.kube/config)
config.load_kube_config()
#api = client.CoreV1Api()

# Create a Kubernetes API client
api_instance = client.AppsV1Api()

# List pods in a specific namespace
namespace = "nginx"  # Replace with your desired namespace
pods = api_instance.list_namespaced_pod(namespace)

# Print the names of the pods
for pod in pods.items:
    print(pod.metadata.name)

# Define a Deployment object
deployment = client.V1Deployment(
    api_version="apps/v1",
    kind="Deployment",
    metadata=client.V1ObjectMeta(name="sample-deployment"),
    spec=client.V1DeploymentSpec(
        replicas=2,
        selector=client.V1LabelSelector(
            match_labels={"app": "sample-app"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": "sample-app"}),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="sample-container",
                        image="nginx:latest",
                        ports=[client.V1ContainerPort(container_port=80)],
                    )
                ]
            ),
        ),
    ),
)

try:
    # Create the Deployment
    api_instance.create_namespaced_deployment(
        namespace="default", body=deployment
    )
    print("Deployment created successfully.")


    # # List pods in the default namespace
    # pods = api_instance.list_namespaced_pod(namespace="default")
    # print("List of Pods in the default namespace:")
    # for pod in pods.items:
    #     print(f"Pod Name: {pod.metadata.name}")


    # # Delete the Deployment
    # api_instance.delete_namespaced_deployment(
    #     name="sample-deployment", namespace="default"
    # )

    print("Deployment deleted successfully.")
except Exception as e:
    print(f"Error: {str(e)}")