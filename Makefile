venv:
	python3 -m venv venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt

proto:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/langchain_service.proto

run-server: 
	python3 -m server

run-client: 
	python3 -m client