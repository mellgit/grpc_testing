# grpc_testing

[офицальная дока grpc](https://grpc.io/)

[Буферы протокола](https://developers.google.com/protocol-buffers/docs/overview)

[Буферы протокола для python](https://developers.google.com/protocol-buffers/docs/pythontutorial)

[Руководство по языку (прото3)](https://developers.google.com/protocol-buffers/docs/proto3)

## command build for proto files 
`python3 -m grpc_tools.protoc -I ./ --python_out=./ --grpc_python_out=./ message.proto `