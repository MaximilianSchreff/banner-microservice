import pytest
import grpc
from generated import banner_service_pb2, banner_service_pb2_grpc

pytestmark = pytest.mark.integration

def test_banner_service():
    """Test the locally running banner service."""
    # Connect to the local server
    channel = grpc.insecure_channel("localhost:51234")
    client = banner_service_pb2_grpc.BannerServiceStub(channel)

    # Send a request
    request = banner_service_pb2.GetCurrentBannerRequest(location="US")
    response = client.GetCurrentBanner(request)

    # Validate the response
    print(f"Title: {response.title}")
    print(f"Description: {response.description}")
    assert response.title
    assert response.description

