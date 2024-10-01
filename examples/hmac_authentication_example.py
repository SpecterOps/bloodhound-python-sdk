import auth
from auth.hmac_authenticated_client import HMACAuthenticatedClient

from blood_hound_api_client import AuthenticatedClient
from blood_hound_api_client.api.api_info import get_api_version
from blood_hound_api_client.models import GetApiVersionResponse200

def get_version(base_url, token_key, token_id):
    hmac_authenticated_client = HMACAuthenticatedClient(base_url=base_url, token_key=token_key, token_id=token_id)
    client = hmac_authenticated_client

    try:
        response: GetApiVersionResponse200 = get_api_version.sync(client=client)
        print(response.data.api)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    token_key = "CAuAwLgPag3xpjfx5gYt3mEpRpK5DXkL1LGVK+utqMLTnlakVmjeZw=="
    token_id = "5f538a38-fd90-4228-b17b-ee09056c6ade"
    get_version("http://bloodhound.localhost", token_key, token_id)
