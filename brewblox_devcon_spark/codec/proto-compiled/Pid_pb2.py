# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Pid.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Pid.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\tPid.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xcf\x08\n\x03Pid\x12\x1c\n\x07inputId\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x04\x92?\x02\x38\x10\x12\x1d\n\x08outputId\x18\x02 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x05\x92?\x02\x38\x10\x12\x32\n\ninputValue\x18\x05 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x34\n\x0cinputSetting\x18\x06 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12-\n\x0boutputValue\x18\x07 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12/\n\routputSetting\x18\x08 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x17\n\x07\x65nabled\x18\x0b \x01(\x08\x42\x06\x8a\xb5\x18\x02\x30\x01\x12\x1c\n\x06\x61\x63tive\x18\x0c \x01(\x08\x42\x0c\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x12\x1e\n\x02kp\x18\r \x01(\x11\x42\x12\x8a\xb5\x18\x02\x08\x02\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x17\n\x02ti\x18\x0e \x01(\rB\x0b\x8a\xb5\x18\x02\x08\x03\x92?\x02\x38\x10\x12\x17\n\x02td\x18\x0f \x01(\rB\x0b\x8a\xb5\x18\x02\x08\x03\x92?\x02\x38\x10\x12#\n\x01p\x18\x10 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12#\n\x01i\x18\x11 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12#\n\x01\x64\x18\x12 \x01(\x11\x42\x18\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12-\n\x05\x65rror\x18\x13 \x01(\x11\x42\x1e\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x06\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x32\n\x08integral\x18\x14 \x01(\x11\x42 \x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x0c\x8a\xb5\x18\x05\x10\x80\x80\x84\x07\x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x33\n\nderivative\x18\x15 \x01(\x11\x42\x1f\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02\x08\x08\x8a\xb5\x18\x04\x10\xa2\xc4\x08\x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12/\n\x0e\x64rivenOutputId\x18\x16 \x01(\rB\x17\x8a\xb5\x18\x02\x18\x05\x8a\xb5\x18\x02@\x01\x92?\x02\x38\x10\x8a\xb5\x18\x02(\x01\x12)\n\rintegralReset\x18\x17 \x01(\x11\x42\x12\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12+\n\x0f\x62oilPointAdjust\x18\x18 \x01(\x11\x42\x12\x8a\xb5\x18\x02\x08\x06\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12#\n\rboilMinOutput\x18\x19 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12$\n\x0e\x62oilModeActive\x18\x1a \x01(\x08\x42\x0c\x8a\xb5\x18\x02\x30\x01\x8a\xb5\x18\x02(\x01\x12\x38\n\x10\x64\x65rivativeFilter\x18\x1b \x01(\x0e\x32\x16.blox.Pid.FilterChoiceB\x06\x8a\xb5\x18\x02(\x01\x12(\n\x0estrippedFields\x18\x63 \x03(\rB\x10\x8a\xb5\x18\x02(\x01\x92?\x02\x38\x10\x92?\x02\x10\x04\"p\n\x0c\x46ilterChoice\x12\r\n\tFILT_NONE\x10\x00\x12\x0c\n\x08\x46ILT_15s\x10\x01\x12\x0c\n\x08\x46ILT_45s\x10\x02\x12\x0c\n\x08\x46ILT_90s\x10\x03\x12\x0b\n\x07\x46ILT_3m\x10\x04\x12\x0c\n\x08\x46ILT_10m\x10\x05\x12\x0c\n\x08\x46ILT_30m\x10\x06:\x07\x8a\xb5\x18\x03\x18\xb0\x02\x62\x06proto3'
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])



_PID_FILTERCHOICE = _descriptor.EnumDescriptor(
  name='FilterChoice',
  full_name='blox.Pid.FilterChoice',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILT_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILT_15s', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILT_45s', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILT_90s', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILT_3m', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILT_10m', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILT_30m', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1032,
  serialized_end=1144,
)
_sym_db.RegisterEnumDescriptor(_PID_FILTERCHOICE)


_PID = _descriptor.Descriptor(
  name='Pid',
  full_name='blox.Pid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputId', full_name='blox.Pid.inputId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\004\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputId', full_name='blox.Pid.outputId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\005\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputValue', full_name='blox.Pid.inputValue', index=2,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inputSetting', full_name='blox.Pid.inputSetting', index=3,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputValue', full_name='blox.Pid.outputValue', index=4,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outputSetting', full_name='blox.Pid.outputSetting', index=5,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='blox.Pid.enabled', index=6,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active', full_name='blox.Pid.active', index=7,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kp', full_name='blox.Pid.kp', index=8,
      number=13, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\002\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ti', full_name='blox.Pid.ti', index=9,
      number=14, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='td', full_name='blox.Pid.td', index=10,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\003\222?\0028\020', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p', full_name='blox.Pid.p', index=11,
      number=16, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='i', full_name='blox.Pid.i', index=12,
      number=17, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='d', full_name='blox.Pid.d', index=13,
      number=18, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='blox.Pid.error', index=14,
      number=19, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\006\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integral', full_name='blox.Pid.integral', index=15,
      number=20, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\014\212\265\030\005\020\200\200\204\007\222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='derivative', full_name='blox.Pid.derivative', index=16,
      number=21, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002\010\010\212\265\030\004\020\242\304\010\222?\0028 \212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drivenOutputId', full_name='blox.Pid.drivenOutputId', index=17,
      number=22, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\030\005\212\265\030\002@\001\222?\0028\020\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='integralReset', full_name='blox.Pid.integralReset', index=18,
      number=23, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boilPointAdjust', full_name='blox.Pid.boilPointAdjust', index=19,
      number=24, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002\010\006\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boilMinOutput', full_name='blox.Pid.boilMinOutput', index=20,
      number=25, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\003\020\200 \222?\0028 ', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boilModeActive', full_name='blox.Pid.boilModeActive', index=21,
      number=26, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\0020\001\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='derivativeFilter', full_name='blox.Pid.derivativeFilter', index=22,
      number=27, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strippedFields', full_name='blox.Pid.strippedFields', index=23,
      number=99, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\212\265\030\002(\001\222?\0028\020\222?\002\020\004', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PID_FILTERCHOICE,
  ],
  serialized_options=b'\212\265\030\003\030\260\002',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=1153,
)

_PID.fields_by_name['derivativeFilter'].enum_type = _PID_FILTERCHOICE
_PID_FILTERCHOICE.containing_type = _PID
DESCRIPTOR.message_types_by_name['Pid'] = _PID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Pid = _reflection.GeneratedProtocolMessageType('Pid', (_message.Message,), {
  'DESCRIPTOR' : _PID,
  '__module__' : 'Pid_pb2'
  # @@protoc_insertion_point(class_scope:blox.Pid)
  })
_sym_db.RegisterMessage(Pid)


_PID.fields_by_name['inputId']._options = None
_PID.fields_by_name['outputId']._options = None
_PID.fields_by_name['inputValue']._options = None
_PID.fields_by_name['inputSetting']._options = None
_PID.fields_by_name['outputValue']._options = None
_PID.fields_by_name['outputSetting']._options = None
_PID.fields_by_name['enabled']._options = None
_PID.fields_by_name['active']._options = None
_PID.fields_by_name['kp']._options = None
_PID.fields_by_name['ti']._options = None
_PID.fields_by_name['td']._options = None
_PID.fields_by_name['p']._options = None
_PID.fields_by_name['i']._options = None
_PID.fields_by_name['d']._options = None
_PID.fields_by_name['error']._options = None
_PID.fields_by_name['integral']._options = None
_PID.fields_by_name['derivative']._options = None
_PID.fields_by_name['drivenOutputId']._options = None
_PID.fields_by_name['integralReset']._options = None
_PID.fields_by_name['boilPointAdjust']._options = None
_PID.fields_by_name['boilMinOutput']._options = None
_PID.fields_by_name['boilModeActive']._options = None
_PID.fields_by_name['derivativeFilter']._options = None
_PID.fields_by_name['strippedFields']._options = None
_PID._options = None
# @@protoc_insertion_point(module_scope)
