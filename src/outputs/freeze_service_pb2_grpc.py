# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import transaction_pb2 as transaction__pb2
from . import transaction_response_pb2 as transaction__response__pb2

GRPC_GENERATED_VERSION = '1.66.2'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in freeze_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FreezeServiceStub(object):
    """*
    The request and responses for freeze service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.freeze = channel.unary_unary(
                '/proto.FreezeService/freeze',
                request_serializer=transaction__pb2.Transaction.SerializeToString,
                response_deserializer=transaction__response__pb2.TransactionResponse.FromString,
                _registered_method=True)


class FreezeServiceServicer(object):
    """*
    The request and responses for freeze service.
    """

    def freeze(self, request, context):
        """*
        Freezes the nodes by submitting the transaction. The grpc server returns the
        TransactionResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FreezeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'freeze': grpc.unary_unary_rpc_method_handler(
                    servicer.freeze,
                    request_deserializer=transaction__pb2.Transaction.FromString,
                    response_serializer=transaction__response__pb2.TransactionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'proto.FreezeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('proto.FreezeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FreezeService(object):
    """*
    The request and responses for freeze service.
    """

    @staticmethod
    def freeze(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/proto.FreezeService/freeze',
            transaction__pb2.Transaction.SerializeToString,
            transaction__response__pb2.TransactionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)