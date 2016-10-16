"""The Python implementation of the GRPC grammar_service.GrammarService client."""

import grpc
import grammar_service_pb2

_TIMEOUT_SECONDS = 10

def grammar_correct(text):
    channel = grpc.insecure_channel('%s:%d' % ('0.0.0.0', 50054))
    stub = grammar_service_pb2.GrammarServiceStub(channel)
    while True:
        if text == 'exit': break
        response = stub.GrammarCorrect(grammar_service_pb2.GrammarCorrectRequest(content = text, error_type = ""), _TIMEOUT_SECONDS)
        return "Correct result", response.message
