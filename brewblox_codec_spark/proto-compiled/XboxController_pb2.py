# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: XboxController.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='XboxController.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14XboxController.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\"\xe9\x03\n\x0eXboxController\x12-\n\x07\x62uttons\x18\x01 \x01(\x0b\x32\x1c.blox.XboxController.Buttons\x12-\n\tleftStick\x18\x02 \x01(\x0b\x32\x1a.blox.XboxController.Stick\x12.\n\nrightStick\x18\x03 \x01(\x0b\x32\x1a.blox.XboxController.Stick\x12&\n\x04\x64Pad\x18\x04 \x01(\x0b\x32\x18.blox.XboxController.Pad\x12\x12\n\nleftBumper\x18\x05 \x01(\r\x12\x13\n\x0brightBumper\x18\x06 \x01(\r\x12\x13\n\x0bleftTrigger\x18\x07 \x01(\r\x12\x14\n\x0crightTrigger\x18\x08 \x01(\r\x1a\x61\n\x07\x42uttons\x12\t\n\x01\x61\x18\x01 \x01(\r\x12\t\n\x01\x62\x18\x02 \x01(\r\x12\t\n\x01x\x18\x03 \x01(\r\x12\t\n\x01y\x18\x04 \x01(\r\x12\x0c\n\x04\x62\x61\x63k\x18\x05 \x01(\r\x12\r\n\x05guide\x18\x06 \x01(\r\x12\r\n\x05start\x18\x07 \x01(\r\x1a,\n\x05Stick\x12\t\n\x01x\x18\x01 \x01(\x11\x12\t\n\x01y\x18\x02 \x01(\x11\x12\r\n\x05\x63lick\x18\x03 \x01(\r\x1a<\n\x03Pad\x12\n\n\x02up\x18\x01 \x01(\r\x12\x0c\n\x04\x64own\x18\x02 \x01(\r\x12\x0c\n\x04left\x18\x03 \x01(\r\x12\r\n\x05right\x18\x04 \x01(\rb\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,])




_XBOXCONTROLLER_BUTTONS = _descriptor.Descriptor(
  name='Buttons',
  full_name='blox.XboxController.Buttons',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='a', full_name='blox.XboxController.Buttons.a', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='b', full_name='blox.XboxController.Buttons.b', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='blox.XboxController.Buttons.x', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='blox.XboxController.Buttons.y', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='back', full_name='blox.XboxController.Buttons.back', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guide', full_name='blox.XboxController.Buttons.guide', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='blox.XboxController.Buttons.start', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=331,
  serialized_end=428,
)

_XBOXCONTROLLER_STICK = _descriptor.Descriptor(
  name='Stick',
  full_name='blox.XboxController.Stick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='blox.XboxController.Stick.x', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='blox.XboxController.Stick.y', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='click', full_name='blox.XboxController.Stick.click', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=430,
  serialized_end=474,
)

_XBOXCONTROLLER_PAD = _descriptor.Descriptor(
  name='Pad',
  full_name='blox.XboxController.Pad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='up', full_name='blox.XboxController.Pad.up', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='down', full_name='blox.XboxController.Pad.down', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='blox.XboxController.Pad.left', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='blox.XboxController.Pad.right', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=476,
  serialized_end=536,
)

_XBOXCONTROLLER = _descriptor.Descriptor(
  name='XboxController',
  full_name='blox.XboxController',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buttons', full_name='blox.XboxController.buttons', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leftStick', full_name='blox.XboxController.leftStick', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rightStick', full_name='blox.XboxController.rightStick', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dPad', full_name='blox.XboxController.dPad', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leftBumper', full_name='blox.XboxController.leftBumper', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rightBumper', full_name='blox.XboxController.rightBumper', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='leftTrigger', full_name='blox.XboxController.leftTrigger', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rightTrigger', full_name='blox.XboxController.rightTrigger', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_XBOXCONTROLLER_BUTTONS, _XBOXCONTROLLER_STICK, _XBOXCONTROLLER_PAD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=536,
)

_XBOXCONTROLLER_BUTTONS.containing_type = _XBOXCONTROLLER
_XBOXCONTROLLER_STICK.containing_type = _XBOXCONTROLLER
_XBOXCONTROLLER_PAD.containing_type = _XBOXCONTROLLER
_XBOXCONTROLLER.fields_by_name['buttons'].message_type = _XBOXCONTROLLER_BUTTONS
_XBOXCONTROLLER.fields_by_name['leftStick'].message_type = _XBOXCONTROLLER_STICK
_XBOXCONTROLLER.fields_by_name['rightStick'].message_type = _XBOXCONTROLLER_STICK
_XBOXCONTROLLER.fields_by_name['dPad'].message_type = _XBOXCONTROLLER_PAD
DESCRIPTOR.message_types_by_name['XboxController'] = _XBOXCONTROLLER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

XboxController = _reflection.GeneratedProtocolMessageType('XboxController', (_message.Message,), dict(

  Buttons = _reflection.GeneratedProtocolMessageType('Buttons', (_message.Message,), dict(
    DESCRIPTOR = _XBOXCONTROLLER_BUTTONS,
    __module__ = 'XboxController_pb2'
    # @@protoc_insertion_point(class_scope:blox.XboxController.Buttons)
    ))
  ,

  Stick = _reflection.GeneratedProtocolMessageType('Stick', (_message.Message,), dict(
    DESCRIPTOR = _XBOXCONTROLLER_STICK,
    __module__ = 'XboxController_pb2'
    # @@protoc_insertion_point(class_scope:blox.XboxController.Stick)
    ))
  ,

  Pad = _reflection.GeneratedProtocolMessageType('Pad', (_message.Message,), dict(
    DESCRIPTOR = _XBOXCONTROLLER_PAD,
    __module__ = 'XboxController_pb2'
    # @@protoc_insertion_point(class_scope:blox.XboxController.Pad)
    ))
  ,
  DESCRIPTOR = _XBOXCONTROLLER,
  __module__ = 'XboxController_pb2'
  # @@protoc_insertion_point(class_scope:blox.XboxController)
  ))
_sym_db.RegisterMessage(XboxController)
_sym_db.RegisterMessage(XboxController.Buttons)
_sym_db.RegisterMessage(XboxController.Stick)
_sym_db.RegisterMessage(XboxController.Pad)


# @@protoc_insertion_point(module_scope)
