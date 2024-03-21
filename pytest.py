import env 
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.conversations import ConversationAnalysisClient

# Parse the JSON file
config_loader = env.ConfigLoader("config.json")  
config_loader.set_environment_variables()

endpoint_key = os.getenv("TEXT_ANALYTICS_ENDPOINT_KEY")
endpoint_url = os.getenv("TEXT_ANALYTICS_ENDPOINT_URL")
project_name = os.environ["AZURE_CONVERSATIONS_PROJECT_NAME"]
deployment_name = os.environ["AZURE_CONVERSATIONS_DEPLOYMENT_NAME"]

client = ConversationAnalysisClient(endpoint_url, AzureKeyCredential(endpoint_key))

with client:
    query = "I like this chicken"
    result = client.analyze_conversation(
        task={
            "kind": "Conversation",
            "analysisInput": {
                "conversationItem": {
                    "participantId": "1",
                    "id": "1",
                    "modality": "text",
                    "language": "en",
                    "text": query
                },
                "isLoggingEnabled": False
            },
            "parameters": {
                "projectName": project_name,
                "deploymentName": deployment_name,
                "verbose": True
            }
        }
    )

# view result
print("query: {}".format(result["result"]["query"]))
print("project kind: {}\n".format(result["result"]["prediction"]["projectKind"]))

print("top intent: {}".format(result["result"]["prediction"]["topIntent"]))
print("category: {}".format(result["result"]["prediction"]["intents"][0]["category"]))
print("confidence score: {}\n".format(result["result"]["prediction"]["intents"][0]["confidenceScore"]))

print("entities:")
for entity in result["result"]["prediction"]["entities"]:
    print("\ncategory: {}".format(entity["category"]))
    print("text: {}".format(entity["text"]))
    print("confidence score: {}".format(entity["confidenceScore"]))
    if "resolutions" in entity:
        print("resolutions")
        for resolution in entity["resolutions"]:
            print("kind: {}".format(resolution["resolutionKind"]))
            print("value: {}".format(resolution["value"]))
    if "extraInformation" in entity:
        print("extra info")
        for data in entity["extraInformation"]:
            print("kind: {}".format(data["extraInformationKind"]))
            if data["extraInformationKind"] == "ListKey":
                print("key: {}".format(data["key"]))
            if data["extraInformationKind"] == "EntitySubtype":
                print("value: {}".format(data["value"]))