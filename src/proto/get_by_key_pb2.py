# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: get_by_key.proto
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
    'get_by_key.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import basic_types_pb2 as basic__types__pb2
from . import query_header_pb2 as query__header__pb2
from . import response_header_pb2 as response__header__pb2
from . import crypto_add_live_hash_pb2 as crypto__add__live__hash__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10get_by_key.proto\x12\x05proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\x1a\x1a\x63rypto_add_live_hash.proto\"L\n\rGetByKeyQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12\x17\n\x03key\x18\x02 \x01(\x0b\x32\n.proto.Key\"\xaa\x01\n\x08\x45ntityID\x12%\n\taccountID\x18\x01 \x01(\x0b\x32\x10.proto.AccountIDH\x00\x12#\n\x08liveHash\x18\x02 \x01(\x0b\x32\x0f.proto.LiveHashH\x00\x12\x1f\n\x06\x66ileID\x18\x03 \x01(\x0b\x32\r.proto.FileIDH\x00\x12\'\n\ncontractID\x18\x04 \x01(\x0b\x32\x11.proto.ContractIDH\x00\x42\x08\n\x06\x65ntity\"\\\n\x10GetByKeyResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12!\n\x08\x65ntities\x18\x02 \x03(\x0b\x32\x0f.proto.EntityIDB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'get_by_key_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_GETBYKEYQUERY']._serialized_start=117
  _globals['_GETBYKEYQUERY']._serialized_end=193
  _globals['_ENTITYID']._serialized_start=196
  _globals['_ENTITYID']._serialized_end=366
  _globals['_GETBYKEYRESPONSE']._serialized_start=368
  _globals['_GETBYKEYRESPONSE']._serialized_end=460
# @@protoc_insertion_point(module_scope)