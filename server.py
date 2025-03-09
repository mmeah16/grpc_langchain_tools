import grpc 
from concurrent import futures 
import protos
from protos import langchain_service_pb2_grpc, langchain_service_pb2

class LangChainServicer(langchain_service_pb2_grpc.LangChainServicer):
    def processQuery(self, request, context):
       response = request.input_text
       print(f'Received request: {response}')
    
       return langchain_service_pb2.QueryResponse(output_text = response)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    langchain_service_pb2_grpc.add_LangChainServicer_to_server(LangChainServicer(), server)

    port = "50051"
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f'gRPC Server running on port {port}...')
    server.wait_for_termination()

if __name__ == "__main__":
    serve()