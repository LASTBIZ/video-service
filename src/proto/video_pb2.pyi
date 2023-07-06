from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CreateVideoRequest(_message.Message):
    __slots__ = ["path"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class UpdateVideoRequest(_message.Message):
    __slots__ = ["old_path", "new_path"]
    OLD_PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    old_path: str
    new_path: str
    def __init__(self, old_path: _Optional[str] = ..., new_path: _Optional[str] = ...) -> None: ...

class DeleteVideoRequest(_message.Message):
    __slots__ = ["path"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...

class CreateScreenShotRequest(_message.Message):
    __slots__ = ["path", "site_path"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    SITE_PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    site_path: str
    def __init__(self, path: _Optional[str] = ..., site_path: _Optional[str] = ...) -> None: ...

class UpdateScreenShotRequest(_message.Message):
    __slots__ = ["old_path", "new_path"]
    OLD_PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    old_path: str
    new_path: str
    def __init__(self, old_path: _Optional[str] = ..., new_path: _Optional[str] = ...) -> None: ...

class DeleteScreenShotRequest(_message.Message):
    __slots__ = ["path"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str
    def __init__(self, path: _Optional[str] = ...) -> None: ...
