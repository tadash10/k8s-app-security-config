import yaml

def generate_deployment():
    deployment = {
        "apiVersion": "apps/v1",
        "kind": "Deployment",
        "metadata": {
            "name": "web-app",
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
                        "name": "web-app",
                        "image": "your/web-app-image:tag",
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

def generate_role_binding():
    role_binding = {
        "apiVersion": "rbac.authorization.k8s.io/v1",
        "kind": "RoleBinding",
        "metadata": {
            "name": "web-app-read-only"
        },
        "subjects": [{"kind": "User", "name": "user@example.com"}],  # Replace with actual user
        "roleRef": {
            "kind": "ClusterRole",
            "name": "view",  # Replace with appropriate role
            "apiGroup": "rbac.authorization.k8s.io"
        }
    }
    return role_binding

def generate_network_policy():
    network_policy = {
        "apiVersion": "networking.k8s.io/v1",
        "kind": "NetworkPolicy",
        "metadata": {
            "name": "deny-ingress"
        },
        "spec": {
            "podSelector": {},
            "policyTypes": ["Ingress"],
            "ingress": []
        }
    }
    return network_policy

if __name__ == "__main__":
    deployment = generate_deployment()
    service = generate_service()
    role_binding = generate_role_binding()
    network_policy = generate_network_policy()

    with open("web-app-deployment.yaml", "w") as f:
        yaml.dump(deployment, f)

    with open("web-app-service.yaml", "w") as f:
        yaml.dump(service, f)

    with open("web-app-role-binding.yaml", "w") as f:
        yaml.dump(role_binding, f)

    with open("web-app-network-policy.yaml", "w") as f:
        yaml.dump(network_policy, f)
