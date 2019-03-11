virtualenv venv
source venv/bin/activate
python -m pip install grpcio-tools
python -m grpc_tools.protoc -I ./greetpb/ --python_out=./greetpb/ --grpc_python_out=./greetpb/ ./greetpb/greet.proto