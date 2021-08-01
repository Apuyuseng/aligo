"""..."""
from dataclasses import dataclass, field
from typing import List

from aligo.types import DataClass, UploadPartInfo
from aligo.types.Enum import *


@dataclass
class CreateFileRequest(DataClass):
    """..."""
    name: str
    file_id: str = None
    type: BaseFileType = 'folder'
    parent_file_id: str = 'root'
    size: int = field(default=None, repr=False)
<<<<<<< HEAD
    check_name_mode: CheckNameMode = field(default='auto_rename', repr=False)
=======
    check_name_mode: CheckNameMode = field(default='refuse', repr=False)
>>>>>>> b_custom_share
    content_hash: str = field(default=None, repr=False)
    content_hash_name: BaseFileContentHashName = field(default='sha1', repr=False)
    content_md5: str = field(default=None, repr=False)
    content_type: str = field(default=None, repr=False)
    description: str = field(default=None, repr=False)
    drive_id: str = field(default=None, repr=False)
    encrypt_mode: str = field(default=None, repr=False)
    hidden: str = field(default=None, repr=False)
    labels: List[str] = field(default=None, repr=False)
    last_updated_at: str = field(default=None, repr=False)
    meta: str = field(default=None, repr=False)
    part_info_list: List[UploadPartInfo] = field(default=None, repr=False)
    pre_hash: str = field(default=None, repr=False)
    user_meta: str = field(default=None, repr=False)
