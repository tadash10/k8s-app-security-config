import yaml
from deployment import generate_deployment
from service import generate_service
from rbac import generate_role_binding
from network_policy import generate_network_policy

def write_to_file(filename, data):
    with open(filename, "w") as f:
        yaml.dump(data, f)

def main():
    try:
        image_tag = "your/web-app-image:tag"
        username = "user@example.com"
        role_name = "view"

        deployment = generate_deployment(image_tag)
        service = generate_service()
        role_binding = generate_role_binding(username, role_name)
        network_policy = generate_network_policy()

        write_to_file("web-app-deployment.yaml", deployment)
        write_to_file("web-app-service.yaml", service)
        write_to_file("web-app-role-binding.yaml", role_binding)
        write_to_file("web-app-network-policy.yaml", network_policy)

        print("Configuration files generated successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
