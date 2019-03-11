# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import time
import logging

import grpc

import greet_pb2
import greet_pb2_grpc


def doUnary(channel):
    stub = greet_pb2_grpc.GreetServiceStub(channel)
    response = stub.Greet(greet_pb2.GreetRequest(greeting = greet_pb2.Greeting(first_name='guys', last_name='guys')))
    print("Greeter client received: " + response.result)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        doUnary(channel)

if __name__ == '__main__':
    logging.basicConfig()
    run()