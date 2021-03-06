# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: greet.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='greet.proto',
  package='greet',
  syntax='proto3',
  serialized_options=_b('Z\007greetpb'),
  serialized_pb=_b('\n\x0bgreet.proto\x12\x05greet\"1\n\x08Greeting\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\"1\n\x0cGreetRequest\x12!\n\x08greeting\x18\x01 \x01(\x0b\x32\x0f.greet.Greeting\"\x1f\n\rGreetResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\":\n\x15GreetManyTimesRequest\x12!\n\x08greeting\x18\x01 \x01(\x0b\x32\x0f.greet.Greeting\"(\n\x16GreetManytimesResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"5\n\x10LongGreetRequest\x12!\n\x08greeting\x18\x01 \x01(\x0b\x32\x0f.greet.Greeting\"#\n\x11LongGreetResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"9\n\x14GreetEveryoneRequest\x12!\n\x08greeting\x18\x01 \x01(\x0b\x32\x0f.greet.Greeting\"\'\n\x15GreetEveryoneResponse\x12\x0e\n\x06result\x18\x01 \x01(\t\"=\n\x18GreetWithDeadlineRequest\x12!\n\x08greeting\x18\x01 \x01(\x0b\x32\x0f.greet.Greeting\"+\n\x19GreetWithDeadlineResponse\x12\x0e\n\x06result\x18\x01 \x01(\t2\x87\x03\n\x0cGreetService\x12\x34\n\x05Greet\x12\x13.greet.GreetRequest\x1a\x14.greet.GreetResponse\"\x00\x12Q\n\x0eGreetManyTimes\x12\x1c.greet.GreetManyTimesRequest\x1a\x1d.greet.GreetManytimesResponse\"\x00\x30\x01\x12\x42\n\tLongGreet\x12\x17.greet.LongGreetRequest\x1a\x18.greet.LongGreetResponse\"\x00(\x01\x12P\n\rGreetEveryone\x12\x1b.greet.GreetEveryoneRequest\x1a\x1c.greet.GreetEveryoneResponse\"\x00(\x01\x30\x01\x12X\n\x11GreetWithDeadline\x12\x1f.greet.GreetWithDeadlineRequest\x1a .greet.GreetWithDeadlineResponse\"\x00\x42\tZ\x07greetpbb\x06proto3')
)




_GREETING = _descriptor.Descriptor(
  name='Greeting',
  full_name='greet.Greeting',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='greet.Greeting.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='greet.Greeting.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=22,
  serialized_end=71,
)


_GREETREQUEST = _descriptor.Descriptor(
  name='GreetRequest',
  full_name='greet.GreetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='greet.GreetRequest.greeting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=73,
  serialized_end=122,
)


_GREETRESPONSE = _descriptor.Descriptor(
  name='GreetResponse',
  full_name='greet.GreetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='greet.GreetResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=124,
  serialized_end=155,
)


_GREETMANYTIMESREQUEST = _descriptor.Descriptor(
  name='GreetManyTimesRequest',
  full_name='greet.GreetManyTimesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='greet.GreetManyTimesRequest.greeting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=157,
  serialized_end=215,
)


_GREETMANYTIMESRESPONSE = _descriptor.Descriptor(
  name='GreetManytimesResponse',
  full_name='greet.GreetManytimesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='greet.GreetManytimesResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=217,
  serialized_end=257,
)


_LONGGREETREQUEST = _descriptor.Descriptor(
  name='LongGreetRequest',
  full_name='greet.LongGreetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='greet.LongGreetRequest.greeting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=259,
  serialized_end=312,
)


_LONGGREETRESPONSE = _descriptor.Descriptor(
  name='LongGreetResponse',
  full_name='greet.LongGreetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='greet.LongGreetResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=314,
  serialized_end=349,
)


_GREETEVERYONEREQUEST = _descriptor.Descriptor(
  name='GreetEveryoneRequest',
  full_name='greet.GreetEveryoneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='greet.GreetEveryoneRequest.greeting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=351,
  serialized_end=408,
)


_GREETEVERYONERESPONSE = _descriptor.Descriptor(
  name='GreetEveryoneResponse',
  full_name='greet.GreetEveryoneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='greet.GreetEveryoneResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=410,
  serialized_end=449,
)


_GREETWITHDEADLINEREQUEST = _descriptor.Descriptor(
  name='GreetWithDeadlineRequest',
  full_name='greet.GreetWithDeadlineRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='greeting', full_name='greet.GreetWithDeadlineRequest.greeting', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=451,
  serialized_end=512,
)


_GREETWITHDEADLINERESPONSE = _descriptor.Descriptor(
  name='GreetWithDeadlineResponse',
  full_name='greet.GreetWithDeadlineResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='greet.GreetWithDeadlineResponse.result', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=514,
  serialized_end=557,
)

_GREETREQUEST.fields_by_name['greeting'].message_type = _GREETING
_GREETMANYTIMESREQUEST.fields_by_name['greeting'].message_type = _GREETING
_LONGGREETREQUEST.fields_by_name['greeting'].message_type = _GREETING
_GREETEVERYONEREQUEST.fields_by_name['greeting'].message_type = _GREETING
_GREETWITHDEADLINEREQUEST.fields_by_name['greeting'].message_type = _GREETING
DESCRIPTOR.message_types_by_name['Greeting'] = _GREETING
DESCRIPTOR.message_types_by_name['GreetRequest'] = _GREETREQUEST
DESCRIPTOR.message_types_by_name['GreetResponse'] = _GREETRESPONSE
DESCRIPTOR.message_types_by_name['GreetManyTimesRequest'] = _GREETMANYTIMESREQUEST
DESCRIPTOR.message_types_by_name['GreetManytimesResponse'] = _GREETMANYTIMESRESPONSE
DESCRIPTOR.message_types_by_name['LongGreetRequest'] = _LONGGREETREQUEST
DESCRIPTOR.message_types_by_name['LongGreetResponse'] = _LONGGREETRESPONSE
DESCRIPTOR.message_types_by_name['GreetEveryoneRequest'] = _GREETEVERYONEREQUEST
DESCRIPTOR.message_types_by_name['GreetEveryoneResponse'] = _GREETEVERYONERESPONSE
DESCRIPTOR.message_types_by_name['GreetWithDeadlineRequest'] = _GREETWITHDEADLINEREQUEST
DESCRIPTOR.message_types_by_name['GreetWithDeadlineResponse'] = _GREETWITHDEADLINERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Greeting = _reflection.GeneratedProtocolMessageType('Greeting', (_message.Message,), dict(
  DESCRIPTOR = _GREETING,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.Greeting)
  ))
_sym_db.RegisterMessage(Greeting)

GreetRequest = _reflection.GeneratedProtocolMessageType('GreetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GREETREQUEST,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.GreetRequest)
  ))
_sym_db.RegisterMessage(GreetRequest)

GreetResponse = _reflection.GeneratedProtocolMessageType('GreetResponse', (_message.Message,), dict(
  DESCRIPTOR = _GREETRESPONSE,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.GreetResponse)
  ))
_sym_db.RegisterMessage(GreetResponse)

GreetManyTimesRequest = _reflection.GeneratedProtocolMessageType('GreetManyTimesRequest', (_message.Message,), dict(
  DESCRIPTOR = _GREETMANYTIMESREQUEST,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.GreetManyTimesRequest)
  ))
_sym_db.RegisterMessage(GreetManyTimesRequest)

GreetManytimesResponse = _reflection.GeneratedProtocolMessageType('GreetManytimesResponse', (_message.Message,), dict(
  DESCRIPTOR = _GREETMANYTIMESRESPONSE,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.GreetManytimesResponse)
  ))
_sym_db.RegisterMessage(GreetManytimesResponse)

LongGreetRequest = _reflection.GeneratedProtocolMessageType('LongGreetRequest', (_message.Message,), dict(
  DESCRIPTOR = _LONGGREETREQUEST,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.LongGreetRequest)
  ))
_sym_db.RegisterMessage(LongGreetRequest)

LongGreetResponse = _reflection.GeneratedProtocolMessageType('LongGreetResponse', (_message.Message,), dict(
  DESCRIPTOR = _LONGGREETRESPONSE,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.LongGreetResponse)
  ))
_sym_db.RegisterMessage(LongGreetResponse)

GreetEveryoneRequest = _reflection.GeneratedProtocolMessageType('GreetEveryoneRequest', (_message.Message,), dict(
  DESCRIPTOR = _GREETEVERYONEREQUEST,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.GreetEveryoneRequest)
  ))
_sym_db.RegisterMessage(GreetEveryoneRequest)

GreetEveryoneResponse = _reflection.GeneratedProtocolMessageType('GreetEveryoneResponse', (_message.Message,), dict(
  DESCRIPTOR = _GREETEVERYONERESPONSE,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.GreetEveryoneResponse)
  ))
_sym_db.RegisterMessage(GreetEveryoneResponse)

GreetWithDeadlineRequest = _reflection.GeneratedProtocolMessageType('GreetWithDeadlineRequest', (_message.Message,), dict(
  DESCRIPTOR = _GREETWITHDEADLINEREQUEST,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.GreetWithDeadlineRequest)
  ))
_sym_db.RegisterMessage(GreetWithDeadlineRequest)

GreetWithDeadlineResponse = _reflection.GeneratedProtocolMessageType('GreetWithDeadlineResponse', (_message.Message,), dict(
  DESCRIPTOR = _GREETWITHDEADLINERESPONSE,
  __module__ = 'greet_pb2'
  # @@protoc_insertion_point(class_scope:greet.GreetWithDeadlineResponse)
  ))
_sym_db.RegisterMessage(GreetWithDeadlineResponse)


DESCRIPTOR._options = None

_GREETSERVICE = _descriptor.ServiceDescriptor(
  name='GreetService',
  full_name='greet.GreetService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=560,
  serialized_end=951,
  methods=[
  _descriptor.MethodDescriptor(
    name='Greet',
    full_name='greet.GreetService.Greet',
    index=0,
    containing_service=None,
    input_type=_GREETREQUEST,
    output_type=_GREETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GreetManyTimes',
    full_name='greet.GreetService.GreetManyTimes',
    index=1,
    containing_service=None,
    input_type=_GREETMANYTIMESREQUEST,
    output_type=_GREETMANYTIMESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='LongGreet',
    full_name='greet.GreetService.LongGreet',
    index=2,
    containing_service=None,
    input_type=_LONGGREETREQUEST,
    output_type=_LONGGREETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GreetEveryone',
    full_name='greet.GreetService.GreetEveryone',
    index=3,
    containing_service=None,
    input_type=_GREETEVERYONEREQUEST,
    output_type=_GREETEVERYONERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GreetWithDeadline',
    full_name='greet.GreetService.GreetWithDeadline',
    index=4,
    containing_service=None,
    input_type=_GREETWITHDEADLINEREQUEST,
    output_type=_GREETWITHDEADLINERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETSERVICE)

DESCRIPTOR.services_by_name['GreetService'] = _GREETSERVICE

# @@protoc_insertion_point(module_scope)
