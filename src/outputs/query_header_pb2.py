# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: query_header.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'query_header.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12query_header.proto\x12\x05proto\x1a\x11transaction.proto\"]\n\x0bQueryHeader\x12#\n\x07payment\x18\x01 \x01(\x0b\x32\x12.proto.Transaction\x12)\n\x0cresponseType\x18\x02 \x01(\x0e\x32\x13.proto.ResponseType*e\n\x0cResponseType\x12\x0f\n\x0b\x41NSWER_ONLY\x10\x00\x12\x16\n\x12\x41NSWER_STATE_PROOF\x10\x01\x12\x0f\n\x0b\x43OST_ANSWER\x10\x02\x12\x1b\n\x17\x43OST_ANSWER_STATE_PROOF\x10\x03\x42&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'query_header_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_RESPONSETYPE']._serialized_start=143
  _globals['_RESPONSETYPE']._serialized_end=244
  _globals['_QUERYHEADER']._serialized_start=48
  _globals['_QUERYHEADER']._serialized_end=141
# @@protoc_insertion_point(module_scope)