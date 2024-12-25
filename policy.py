from azure.identity import ClientSecretCredential
from azure.mgmt.resource import PolicyClient
import os

tenant_id = 'b0f5bbda-5dc8-4ac8-8621-fb81b23db439'  # Azure Active Directory tenant ID
client_id = '9234a681-aeb8-4adc-8a30-6b0831317027'  # Service principal application ID
with open('app-secret.txt', 'r') as file:
    client_secret = file.read()


# Authenticate using the ClientSecretCredential
credential = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=client_secret)

# Initialize PolicyClient
subscription_id = "87eb1361-d59d-47b3-a050-3fb90ffebd63"  # Replace with your Azure subscription ID
policy_client = PolicyClient(credential, subscription_id)

# Get all policy definitions
policy_definitions = policy_client.policy_definitions.list()
built_in_policies = [policy for policy in policy_definitions if policy.policy_type == "BuiltIn"]
formatted_policies = {}
for policy in built_in_policies:
    parameters = policy.parameters or {}
    formatted_params = ""
    for key in parameters:
        print(key)
        print(parameters[key].type)
        
    formatted_policies[policy.name] = {
        "display_name": policy.display_name,
        "description": policy.description,
        "parameters": parameters
    }
    print(formatted_policies[policy.name])