# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: file_service.proto
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
    'file_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66ile_service.proto\" \n\x0b\x46ileRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\"\x19\n\tFileChunk\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x32\x39\n\x0b\x46ileService\x12*\n\x0c\x44ownloadFile\x12\x0c.FileRequest\x1a\n.FileChunk0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILEREQUEST']._serialized_start=22
  _globals['_FILEREQUEST']._serialized_end=54
  _globals['_FILECHUNK']._serialized_start=56
  _globals['_FILECHUNK']._serialized_end=81
  _globals['_FILESERVICE']._serialized_start=83
  _globals['_FILESERVICE']._serialized_end=140
# @@protoc_insertion_point(module_scope)
