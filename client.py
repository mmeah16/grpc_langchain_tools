import grpc

from protos import langchain_service_pb2_grpc, langchain_service_pb2

def run():
    """Sends a request to the gRPC server and prints the response."""

    channel = grpc.insecure_channel("localhost:50051")
    stub = langchain_service_pb2_grpc.LangChainStub(channel)

    user_input = input('Enter your name!')
    response = stub.processQuery(langchain_service_pb2.QueryRequest(input_text = user_input))

    print(f'Server response: {response.output_text}')

if __name__ == "__main__":
    run()