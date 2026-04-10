"""
CAD管理器文档管理模块
"""

from dataclasses import dataclass
from typing import Optional, Dict, Any
from constants import AcRegenType
from exceptions import ConnectionError

@dataclass
class DocumentInfo:
    """文档信息数据类"""
    name: str
    full_name: str
    path: str
    saved: bool
    read_only: bool
    active: bool


class DocumentMixin:
    """文档管理混合类"""

    def new_document(self, template_name: Optional[str] = None) -> Any:
        """
        创建新文档

        Args:
            template_name: 模板文件名（可选）

        Returns:
            新创建的文档对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        if template_name:
            new_doc = self._acad.Documents.Add(template_name)
        else:
            new_doc = self._acad.Documents.Add()

        # 更新当前文档引用
        self._doc = new_doc
        return new_doc

    def open_document(self, file_path: str) -> Any:
        """
        打开现有文档

        Args:
            file_path: DWG文件路径

        Returns:
            打开的文档对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        doc = self._acad.Documents.Open(file_path)
        self._doc = doc
        return doc

    def save_document(self) -> None:
        """保存当前文档"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.Save()

    def save_document_as(self, file_path: str) -> None:
        """
        将当前文档另存为

        Args:
            file_path: 保存路径
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.SaveAs(file_path)

    def close_document(self, save_changes: bool = True) -> None:
        """
        关闭当前文档

        Args:
            save_changes: 是否保存更改
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.Close(save_changes)
        # 切换到另一个打开的文档或保持为None
        if self._acad.Documents.Count > 0:
            self._doc = self._acad.ActiveDocument
        else:
            self._doc = None

    def get_document_info(self) -> DocumentInfo:
        """
        获取当前文档信息

        Returns:
            DocumentInfo 对象，包含文档信息
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return DocumentInfo(
            name=self._doc.Name,
            full_name=self._doc.FullName,
            path=self._doc.Path,
            saved=self._doc.Saved,
            read_only=self._doc.ReadOnly,
            active=self._doc.Active
        )

    def regen(self, regen_type: int = AcRegenType.acAllViewports) -> None:
        """
        重生成图形

        Args:
            regen_type: 重生成类型 (AcRegenType)
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.Regen(regen_type)

    def purge_all(self) -> None:
        """清理所有未使用的命名对象"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.PurgeAll()

    def send_command(self, command: str) -> None:
        """
        发送命令到AutoCAD命令行

        Args:
            command: AutoCAD命令字符串
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.SendCommand(command)