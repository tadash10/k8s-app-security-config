import yaml

def generate_deployment(image_tag):
    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": "web-app-deployment",
            "labels": {"app": "web-app"}
        },
        "spec": {
            "replicas": 2,
            "selector": {
                "matchLabels": {"app": "web-app"}
            },
            "template": {
                "metadata": {"labels": {"app": "web-app"}},
                "spec": {
                    "containers": [{
                        "name": "web-app-container",
                        "image": image_tag,
                        "ports": [{"containerPort": 80}]
                    }]
                }
            }
        }
    }
    return deployment

def generate_service():
    service = {
        "apiVersion": "v1",
        "kind": "Service",
        "metadata": {
            "name": "web-app-service"
        },
        "spec": {
            "selector": {"app": "web-app"},
            "ports": [{"port": 80}]
        }
    }
    return service

def generate_role_binding(username, role_name):
    role_binding = {
        "apiVersion": "rbac.authorization.k8s.io/v1",
        "kind": "RoleBinding",
        "metadata": {
            "name": "web-app-role-binding"
        },
        "subjects": [{"kind": "User", "name": username}],
        "roleRef": {
            "kind": "ClusterRole",
            "name": role_name,
            "apiGroup": "rbac.authorization.k8s.io"
        }
    }
    return role_binding

def generate_network_policy():
    network_policy = {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "NetworkPolicy",
        "metadata": {
            "name": "web-app-network-policy"
        },
        "spec": {
            "podSelector": {},
            "policyTypes": ["Ingress"],
            "ingress": []
        }
    }
    return network_policy

if __name__ == "__main__":
    try:
        image_tag = "your/web-app-image:tag"
        username = "user@example.com"
        role_name = "view"
        
        deployment = generate_deployment(image_tag)
        service = generate_service()
        role_binding = generate_role_binding(username, role_name)
        network_policy = generate_network_policy()

        with open("web-app-deployment.yaml", "w") as f:
            yaml.dump(deployment, f)

        with open("web-app-service.yaml", "w") as f:
            yaml.dump(service, f)

        with open("web-app-role-binding.yaml", "w") as f:
            yaml.dump(role_binding, f)

        with open("web-app-network-policy.yaml", "w") as f:
            yaml.dump(network_policy, f)

        print("Configuration files generated successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
