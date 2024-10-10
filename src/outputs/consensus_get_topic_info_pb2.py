# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: consensus_get_topic_info.proto
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
    'consensus_get_topic_info.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2
from . import query_header_pb2 as query__header__pb2
from . import response_header_pb2 as response__header__pb2
from . import consensus_topic_info_pb2 as consensus__topic__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63onsensus_get_topic_info.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\x1a\x1a\x63onsensus_topic_info.proto\"a\n\x1a\x43onsensusGetTopicInfoQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12\x1f\n\x07topicID\x18\x02 \x01(\x0b\x32\x0e.proto.TopicID\"\x95\x01\n\x1d\x43onsensusGetTopicInfoResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x1f\n\x07topicID\x18\x02 \x01(\x0b\x32\x0e.proto.TopicID\x12,\n\ttopicInfo\x18\x05 \x01(\x0b\x32\x19.proto.ConsensusTopicInfoB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'consensus_get_topic_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_CONSENSUSGETTOPICINFOQUERY']._serialized_start=131
  _globals['_CONSENSUSGETTOPICINFOQUERY']._serialized_end=228
  _globals['_CONSENSUSGETTOPICINFORESPONSE']._serialized_start=231
  _globals['_CONSENSUSGETTOPICINFORESPONSE']._serialized_end=380
# @@protoc_insertion_point(module_scope)