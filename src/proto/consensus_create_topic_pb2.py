# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: consensus_create_topic.proto
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
    'consensus_create_topic.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2
from . import duration_pb2 as duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63onsensus_create_topic.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x0e\x64uration.proto\"\xc6\x01\n#ConsensusCreateTopicTransactionBody\x12\x0c\n\x04memo\x18\x01 \x01(\t\x12\x1c\n\x08\x61\x64minKey\x18\x02 \x01(\x0b\x32\n.proto.Key\x12\x1d\n\tsubmitKey\x18\x03 \x01(\x0b\x32\n.proto.Key\x12(\n\x0f\x61utoRenewPeriod\x18\x06 \x01(\x0b\x32\x0f.proto.Duration\x12*\n\x10\x61utoRenewAccount\x18\x07 \x01(\x0b\x32\x10.proto.AccountIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'consensus_create_topic_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_CONSENSUSCREATETOPICTRANSACTIONBODY']._serialized_start=75
  _globals['_CONSENSUSCREATETOPICTRANSACTIONBODY']._serialized_end=273
# @@protoc_insertion_point(module_scope)