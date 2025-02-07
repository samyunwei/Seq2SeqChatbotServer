# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SimpleChatbot.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='SimpleChatbot.proto',
    package='simplechatbot',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=b'\n\x13SimpleChatbot.proto\x12\rsimplechatbot\"(\n\x0b\x43hatRequest\x12\x0b\n\x03ids\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"&\n\tChatReply\x12\x0b\n\x03ids\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t2S\n\x13SimpleChatBotServer\x12<\n\x04\x43hat\x12\x1a.simplechatbot.ChatRequest\x1a\x18.simplechatbot.ChatReplyb\x06proto3'
)

_CHATREQUEST = _descriptor.Descriptor(
    name='ChatRequest',
    full_name='simplechatbot.ChatRequest',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='ids', full_name='simplechatbot.ChatRequest.ids', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='simplechatbot.ChatRequest.data', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=38,
    serialized_end=78,
)

_CHATREPLY = _descriptor.Descriptor(
    name='ChatReply',
    full_name='simplechatbot.ChatReply',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='ids', full_name='simplechatbot.ChatReply.ids', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='simplechatbot.ChatReply.data', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=b"".decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=80,
    serialized_end=118,
)

DESCRIPTOR.message_types_by_name['ChatRequest'] = _CHATREQUEST
DESCRIPTOR.message_types_by_name['ChatReply'] = _CHATREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChatRequest = _reflection.GeneratedProtocolMessageType('ChatRequest', (_message.Message,), {
    'DESCRIPTOR': _CHATREQUEST,
    '__module__': 'SimpleChatbot_pb2'
    # @@protoc_insertion_point(class_scope:simplechatbot.ChatRequest)
})
_sym_db.RegisterMessage(ChatRequest)

ChatReply = _reflection.GeneratedProtocolMessageType('ChatReply', (_message.Message,), {
    'DESCRIPTOR': _CHATREPLY,
    '__module__': 'SimpleChatbot_pb2'
    # @@protoc_insertion_point(class_scope:simplechatbot.ChatReply)
})
_sym_db.RegisterMessage(ChatReply)

_SIMPLECHATBOTSERVER = _descriptor.ServiceDescriptor(
    name='SimpleChatBotServer',
    full_name='simplechatbot.SimpleChatBotServer',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=120,
    serialized_end=203,
    methods=[
        _descriptor.MethodDescriptor(
            name='Chat',
            full_name='simplechatbot.SimpleChatBotServer.Chat',
            index=0,
            containing_service=None,
            input_type=_CHATREQUEST,
            output_type=_CHATREPLY,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_SIMPLECHATBOTSERVER)

DESCRIPTOR.services_by_name['SimpleChatBotServer'] = _SIMPLECHATBOTSERVER

# @@protoc_insertion_point(module_scope)
