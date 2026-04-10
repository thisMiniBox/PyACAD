"""
CAD管理器自定义异常类
"""

class CadManagerError(Exception):
    """CAD管理器基类异常"""
    pass

class ConnectionError(CadManagerError):
    """连接相关异常"""
    pass

class UserInputError(CadManagerError):
    """用户输入相关异常"""
    pass

class DocumentError(CadManagerError):
    """文档操作相关异常"""
    pass

class EntityError(CadManagerError):
    """实体操作相关异常"""
    pass