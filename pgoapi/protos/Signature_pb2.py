# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Signature.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Signature.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0fSignature.proto\"\xf6\r\n\tSignature\x12\x1d\n\x15timestamp_since_start\x18\x02 \x01(\x04\x12,\n\x0clocation_fix\x18\x04 \x03(\x0b\x32\x16.Signature.LocationFix\x12+\n\x08gps_info\x18\x05 \x01(\x0b\x32\x19.Signature.AndroidGpsInfo\x12*\n\x0bsensor_info\x18\x07 \x01(\x0b\x32\x15.Signature.SensorInfo\x12*\n\x0b\x64\x65vice_info\x18\x08 \x01(\x0b\x32\x15.Signature.DeviceInfo\x12\x32\n\x0f\x61\x63tivity_status\x18\t \x01(\x0b\x32\x19.Signature.ActivityStatus\x12\x16\n\x0elocation_hash1\x18\n \x01(\r\x12\x16\n\x0elocation_hash2\x18\x14 \x01(\r\x12\r\n\x05unk22\x18\x16 \x01(\x0c\x12\x11\n\ttimestamp\x18\x17 \x01(\x04\x12\x14\n\x0crequest_hash\x18\x18 \x03(\x04\x1a\xec\x01\n\x0bLocationFix\x12\x10\n\x08provider\x18\x01 \x01(\t\x12\x1d\n\x15timestamp_since_start\x18\x02 \x01(\x04\x12\x10\n\x08latitude\x18\r \x01(\x02\x12\x11\n\tlongitude\x18\x0e \x01(\x02\x12\x1b\n\x13horizontal_accuracy\x18\x14 \x01(\x02\x12\x10\n\x08\x61ltitude\x18\x15 \x01(\x02\x12\x19\n\x11vertical_accuracy\x18\x16 \x01(\x02\x12\x17\n\x0fprovider_status\x18\x1a \x01(\x04\x12\r\n\x05\x66loor\x18\x1b \x01(\r\x12\x15\n\rlocation_type\x18\x1c \x01(\x04\x1a\xaf\x01\n\x0e\x41ndroidGpsInfo\x12\x13\n\x0btime_to_fix\x18\x01 \x01(\x04\x12\x16\n\x0esatellites_prn\x18\x02 \x03(\x05\x12\x0b\n\x03snr\x18\x03 \x03(\x02\x12\x0f\n\x07\x61zimuth\x18\x04 \x03(\x02\x12\x11\n\televation\x18\x05 \x03(\x02\x12\x13\n\x0bhas_almanac\x18\x06 \x03(\x08\x12\x15\n\rhas_ephemeris\x18\x07 \x03(\x08\x12\x13\n\x0bused_in_fix\x18\x08 \x03(\x08\x1a\xbe\x03\n\nSensorInfo\x12\x1a\n\x12timestamp_snapshot\x18\x01 \x01(\x04\x12\x16\n\x0emagnetometer_x\x18\x03 \x01(\x01\x12\x16\n\x0emagnetometer_y\x18\x04 \x01(\x01\x12\x16\n\x0emagnetometer_z\x18\x05 \x01(\x01\x12\x1a\n\x12\x61ngle_normalized_x\x18\x06 \x01(\x01\x12\x1a\n\x12\x61ngle_normalized_y\x18\x07 \x01(\x01\x12\x1a\n\x12\x61ngle_normalized_z\x18\x08 \x01(\x01\x12\x13\n\x0b\x61\x63\x63\x65l_raw_x\x18\n \x01(\x01\x12\x13\n\x0b\x61\x63\x63\x65l_raw_y\x18\x0b \x01(\x01\x12\x13\n\x0b\x61\x63\x63\x65l_raw_z\x18\x0c \x01(\x01\x12\x17\n\x0fgyroscope_raw_x\x18\r \x01(\x01\x12\x17\n\x0fgyroscope_raw_y\x18\x0e \x01(\x01\x12\x17\n\x0fgyroscope_raw_z\x18\x0f \x01(\x01\x12\x1a\n\x12\x61\x63\x63\x65l_normalized_x\x18\x10 \x01(\x01\x12\x1a\n\x12\x61\x63\x63\x65l_normalized_y\x18\x11 \x01(\x01\x12\x1a\n\x12\x61\x63\x63\x65l_normalized_z\x18\x12 \x01(\x01\x12\x1a\n\x12\x61\x63\x63\x65lerometer_axes\x18\x13 \x01(\x04\x1a\xda\x02\n\nDeviceInfo\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12\x1a\n\x12\x61ndroid_board_name\x18\x02 \x01(\t\x12\x1a\n\x12\x61ndroid_bootloader\x18\x03 \x01(\t\x12\x14\n\x0c\x64\x65vice_brand\x18\x04 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x05 \x01(\t\x12\x1f\n\x17\x64\x65vice_model_identifier\x18\x06 \x01(\t\x12\x19\n\x11\x64\x65vice_model_boot\x18\x07 \x01(\t\x12\x1d\n\x15hardware_manufacturer\x18\x08 \x01(\t\x12\x16\n\x0ehardware_model\x18\t \x01(\t\x12\x16\n\x0e\x66irmware_brand\x18\n \x01(\t\x12\x15\n\rfirmware_tags\x18\x0c \x01(\t\x12\x15\n\rfirmware_type\x18\r \x01(\t\x12\x1c\n\x14\x66irmware_fingerprint\x18\x0e \x01(\t\x1a\xbb\x01\n\x0e\x41\x63tivityStatus\x12\x15\n\rstart_time_ms\x18\x01 \x01(\x04\x12\x16\n\x0eunknown_status\x18\x02 \x01(\x08\x12\x0f\n\x07walking\x18\x03 \x01(\x08\x12\x0f\n\x07running\x18\x04 \x01(\x08\x12\x12\n\nstationary\x18\x05 \x01(\x08\x12\x12\n\nautomotive\x18\x06 \x01(\x08\x12\x0f\n\x07tilting\x18\x07 \x01(\x08\x12\x0f\n\x07\x63ycling\x18\x08 \x01(\x08\x12\x0e\n\x06status\x18\t \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SIGNATURE_LOCATIONFIX = _descriptor.Descriptor(
  name='LocationFix',
  full_name='Signature.LocationFix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='Signature.LocationFix.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_since_start', full_name='Signature.LocationFix.timestamp_since_start', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Signature.LocationFix.latitude', index=2,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Signature.LocationFix.longitude', index=3,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='horizontal_accuracy', full_name='Signature.LocationFix.horizontal_accuracy', index=4,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='Signature.LocationFix.altitude', index=5,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertical_accuracy', full_name='Signature.LocationFix.vertical_accuracy', index=6,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='provider_status', full_name='Signature.LocationFix.provider_status', index=7,
      number=26, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='floor', full_name='Signature.LocationFix.floor', index=8,
      number=27, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_type', full_name='Signature.LocationFix.location_type', index=9,
      number=28, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=400,
  serialized_end=636,
)

_SIGNATURE_ANDROIDGPSINFO = _descriptor.Descriptor(
  name='AndroidGpsInfo',
  full_name='Signature.AndroidGpsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_to_fix', full_name='Signature.AndroidGpsInfo.time_to_fix', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='satellites_prn', full_name='Signature.AndroidGpsInfo.satellites_prn', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snr', full_name='Signature.AndroidGpsInfo.snr', index=2,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='azimuth', full_name='Signature.AndroidGpsInfo.azimuth', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elevation', full_name='Signature.AndroidGpsInfo.elevation', index=4,
      number=5, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_almanac', full_name='Signature.AndroidGpsInfo.has_almanac', index=5,
      number=6, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_ephemeris', full_name='Signature.AndroidGpsInfo.has_ephemeris', index=6,
      number=7, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='used_in_fix', full_name='Signature.AndroidGpsInfo.used_in_fix', index=7,
      number=8, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=639,
  serialized_end=814,
)

_SIGNATURE_SENSORINFO = _descriptor.Descriptor(
  name='SensorInfo',
  full_name='Signature.SensorInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_snapshot', full_name='Signature.SensorInfo.timestamp_snapshot', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magnetometer_x', full_name='Signature.SensorInfo.magnetometer_x', index=1,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magnetometer_y', full_name='Signature.SensorInfo.magnetometer_y', index=2,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magnetometer_z', full_name='Signature.SensorInfo.magnetometer_z', index=3,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_normalized_x', full_name='Signature.SensorInfo.angle_normalized_x', index=4,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_normalized_y', full_name='Signature.SensorInfo.angle_normalized_y', index=5,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='angle_normalized_z', full_name='Signature.SensorInfo.angle_normalized_z', index=6,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accel_raw_x', full_name='Signature.SensorInfo.accel_raw_x', index=7,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accel_raw_y', full_name='Signature.SensorInfo.accel_raw_y', index=8,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accel_raw_z', full_name='Signature.SensorInfo.accel_raw_z', index=9,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gyroscope_raw_x', full_name='Signature.SensorInfo.gyroscope_raw_x', index=10,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gyroscope_raw_y', full_name='Signature.SensorInfo.gyroscope_raw_y', index=11,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gyroscope_raw_z', full_name='Signature.SensorInfo.gyroscope_raw_z', index=12,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accel_normalized_x', full_name='Signature.SensorInfo.accel_normalized_x', index=13,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accel_normalized_y', full_name='Signature.SensorInfo.accel_normalized_y', index=14,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accel_normalized_z', full_name='Signature.SensorInfo.accel_normalized_z', index=15,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='accelerometer_axes', full_name='Signature.SensorInfo.accelerometer_axes', index=16,
      number=19, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=817,
  serialized_end=1263,
)

_SIGNATURE_DEVICEINFO = _descriptor.Descriptor(
  name='DeviceInfo',
  full_name='Signature.DeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='Signature.DeviceInfo.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='android_board_name', full_name='Signature.DeviceInfo.android_board_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='android_bootloader', full_name='Signature.DeviceInfo.android_bootloader', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_brand', full_name='Signature.DeviceInfo.device_brand', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_model', full_name='Signature.DeviceInfo.device_model', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_model_identifier', full_name='Signature.DeviceInfo.device_model_identifier', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_model_boot', full_name='Signature.DeviceInfo.device_model_boot', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hardware_manufacturer', full_name='Signature.DeviceInfo.hardware_manufacturer', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hardware_model', full_name='Signature.DeviceInfo.hardware_model', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_brand', full_name='Signature.DeviceInfo.firmware_brand', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_tags', full_name='Signature.DeviceInfo.firmware_tags', index=10,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_type', full_name='Signature.DeviceInfo.firmware_type', index=11,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='firmware_fingerprint', full_name='Signature.DeviceInfo.firmware_fingerprint', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1266,
  serialized_end=1612,
)

_SIGNATURE_ACTIVITYSTATUS = _descriptor.Descriptor(
  name='ActivityStatus',
  full_name='Signature.ActivityStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time_ms', full_name='Signature.ActivityStatus.start_time_ms', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown_status', full_name='Signature.ActivityStatus.unknown_status', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='walking', full_name='Signature.ActivityStatus.walking', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='running', full_name='Signature.ActivityStatus.running', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stationary', full_name='Signature.ActivityStatus.stationary', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='automotive', full_name='Signature.ActivityStatus.automotive', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tilting', full_name='Signature.ActivityStatus.tilting', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cycling', full_name='Signature.ActivityStatus.cycling', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Signature.ActivityStatus.status', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1615,
  serialized_end=1802,
)

_SIGNATURE = _descriptor.Descriptor(
  name='Signature',
  full_name='Signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp_since_start', full_name='Signature.timestamp_since_start', index=0,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_fix', full_name='Signature.location_fix', index=1,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gps_info', full_name='Signature.gps_info', index=2,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sensor_info', full_name='Signature.sensor_info', index=3,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_info', full_name='Signature.device_info', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_status', full_name='Signature.activity_status', index=5,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_hash1', full_name='Signature.location_hash1', index=6,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='location_hash2', full_name='Signature.location_hash2', index=7,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unk22', full_name='Signature.unk22', index=8,
      number=22, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='Signature.timestamp', index=9,
      number=23, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_hash', full_name='Signature.request_hash', index=10,
      number=24, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATURE_LOCATIONFIX, _SIGNATURE_ANDROIDGPSINFO, _SIGNATURE_SENSORINFO, _SIGNATURE_DEVICEINFO, _SIGNATURE_ACTIVITYSTATUS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=1802,
)

_SIGNATURE_LOCATIONFIX.containing_type = _SIGNATURE
_SIGNATURE_ANDROIDGPSINFO.containing_type = _SIGNATURE
_SIGNATURE_SENSORINFO.containing_type = _SIGNATURE
_SIGNATURE_DEVICEINFO.containing_type = _SIGNATURE
_SIGNATURE_ACTIVITYSTATUS.containing_type = _SIGNATURE
_SIGNATURE.fields_by_name['location_fix'].message_type = _SIGNATURE_LOCATIONFIX
_SIGNATURE.fields_by_name['gps_info'].message_type = _SIGNATURE_ANDROIDGPSINFO
_SIGNATURE.fields_by_name['sensor_info'].message_type = _SIGNATURE_SENSORINFO
_SIGNATURE.fields_by_name['device_info'].message_type = _SIGNATURE_DEVICEINFO
_SIGNATURE.fields_by_name['activity_status'].message_type = _SIGNATURE_ACTIVITYSTATUS
DESCRIPTOR.message_types_by_name['Signature'] = _SIGNATURE

Signature = _reflection.GeneratedProtocolMessageType('Signature', (_message.Message,), dict(

  LocationFix = _reflection.GeneratedProtocolMessageType('LocationFix', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATURE_LOCATIONFIX,
    __module__ = 'Signature_pb2'
    # @@protoc_insertion_point(class_scope:Signature.LocationFix)
    ))
  ,

  AndroidGpsInfo = _reflection.GeneratedProtocolMessageType('AndroidGpsInfo', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATURE_ANDROIDGPSINFO,
    __module__ = 'Signature_pb2'
    # @@protoc_insertion_point(class_scope:Signature.AndroidGpsInfo)
    ))
  ,

  SensorInfo = _reflection.GeneratedProtocolMessageType('SensorInfo', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATURE_SENSORINFO,
    __module__ = 'Signature_pb2'
    # @@protoc_insertion_point(class_scope:Signature.SensorInfo)
    ))
  ,

  DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATURE_DEVICEINFO,
    __module__ = 'Signature_pb2'
    # @@protoc_insertion_point(class_scope:Signature.DeviceInfo)
    ))
  ,

  ActivityStatus = _reflection.GeneratedProtocolMessageType('ActivityStatus', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATURE_ACTIVITYSTATUS,
    __module__ = 'Signature_pb2'
    # @@protoc_insertion_point(class_scope:Signature.ActivityStatus)
    ))
  ,
  DESCRIPTOR = _SIGNATURE,
  __module__ = 'Signature_pb2'
  # @@protoc_insertion_point(class_scope:Signature)
  ))
_sym_db.RegisterMessage(Signature)
_sym_db.RegisterMessage(Signature.LocationFix)
_sym_db.RegisterMessage(Signature.AndroidGpsInfo)
_sym_db.RegisterMessage(Signature.SensorInfo)
_sym_db.RegisterMessage(Signature.DeviceInfo)
_sym_db.RegisterMessage(Signature.ActivityStatus)


# @@protoc_insertion_point(module_scope)
