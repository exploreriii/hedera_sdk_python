# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: contract_get_info.proto
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
    'contract_get_info.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import timestamp_pb2 as timestamp__pb2
from . import duration_pb2 as duration__pb2
from . import basic_types_pb2 as basic__types__pb2
from . import query_header_pb2 as query__header__pb2
from . import response_header_pb2 as response__header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x63ontract_get_info.proto\x12\x05proto\x1a\x0ftimestamp.proto\x1a\x0e\x64uration.proto\x1a\x11\x62\x61sic_types.proto\x1a\x12query_header.proto\x1a\x15response_header.proto\"a\n\x14\x43ontractGetInfoQuery\x12\"\n\x06header\x18\x01 \x01(\x0b\x32\x12.proto.QueryHeader\x12%\n\ncontractID\x18\x02 \x01(\x0b\x32\x11.proto.ContractID\"\x80\x05\n\x17\x43ontractGetInfoResponse\x12%\n\x06header\x18\x01 \x01(\x0b\x32\x15.proto.ResponseHeader\x12\x41\n\x0c\x63ontractInfo\x18\x02 \x01(\x0b\x32+.proto.ContractGetInfoResponse.ContractInfo\x1a\xfa\x03\n\x0c\x43ontractInfo\x12%\n\ncontractID\x18\x01 \x01(\x0b\x32\x11.proto.ContractID\x12#\n\taccountID\x18\x02 \x01(\x0b\x32\x10.proto.AccountID\x12\x19\n\x11\x63ontractAccountID\x18\x03 \x01(\t\x12\x1c\n\x08\x61\x64minKey\x18\x04 \x01(\x0b\x32\n.proto.Key\x12(\n\x0e\x65xpirationTime\x18\x05 \x01(\x0b\x32\x10.proto.Timestamp\x12(\n\x0f\x61utoRenewPeriod\x18\x06 \x01(\x0b\x32\x0f.proto.Duration\x12\x0f\n\x07storage\x18\x07 \x01(\x03\x12\x0c\n\x04memo\x18\x08 \x01(\t\x12\x0f\n\x07\x62\x61lance\x18\t \x01(\x04\x12\x0f\n\x07\x64\x65leted\x18\n \x01(\x08\x12\x38\n\x12tokenRelationships\x18\x0b \x03(\x0b\x32\x18.proto.TokenRelationshipB\x02\x18\x01\x12\x11\n\tledger_id\x18\x0c \x01(\x0c\x12/\n\x15\x61uto_renew_account_id\x18\r \x01(\x0b\x32\x10.proto.AccountID\x12(\n max_automatic_token_associations\x18\x0e \x01(\x05\x12(\n\x0cstaking_info\x18\x0f \x01(\x0b\x32\x12.proto.StakingInfoB&\n\"com.hederahashgraph.api.proto.javaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'contract_get_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hederahashgraph.api.proto.javaP\001'
  _globals['_CONTRACTGETINFORESPONSE_CONTRACTINFO'].fields_by_name['tokenRelationships']._loaded_options = None
  _globals['_CONTRACTGETINFORESPONSE_CONTRACTINFO'].fields_by_name['tokenRelationships']._serialized_options = b'\030\001'
  _globals['_CONTRACTGETINFOQUERY']._serialized_start=129
  _globals['_CONTRACTGETINFOQUERY']._serialized_end=226
  _globals['_CONTRACTGETINFORESPONSE']._serialized_start=229
  _globals['_CONTRACTGETINFORESPONSE']._serialized_end=869
  _globals['_CONTRACTGETINFORESPONSE_CONTRACTINFO']._serialized_start=363
  _globals['_CONTRACTGETINFORESPONSE_CONTRACTINFO']._serialized_end=869
# @@protoc_insertion_point(module_scope)