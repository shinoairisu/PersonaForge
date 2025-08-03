from typing import List, Tuple

from llm_management.llm_mgr import LLMManager
from chaker.error import ChakerParseError


class ChakerParser:
    """Chaker语言解释器"""

    def __init__(self, chaker_str: str, llm: LLMManager):
        """
        初始化解释器，务必保证联网能访问自己的api
        :param chaker_str:脚本语言
        :param domain:api的域，比如openai
        :param name:api的名字，比如gemini
        :param model:模型的名字，比如gemini-2.5-pro
        """
        self.text = chaker_str

    def _split_line(self) -> List[str]:
        return [line.strip() for line in self.text.strip().splitlines() if line.strip()]

    def parse(self) -> str:
        """解析用户写的chaker脚本，输出最终的人物prompt。

        指令、
        """
        code = self._split_line()
