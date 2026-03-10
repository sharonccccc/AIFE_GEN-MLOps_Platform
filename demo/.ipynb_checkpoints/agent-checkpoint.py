import time
from pocket import Node,Flow,AsyncFlow,build_mermaid,EXEC

import asyncio
# from pocket.utils import PPrint

# from pocket.utils import Live,extract_json
import time
import os
import json
import json5


class 用戶輸入(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        pass

class LLM_調用(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        if exec_res == 'text':
            return 'text'
        elif exec_res == 'tools':
            return 'tools'

class 返回答案(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        return '答案'

class 調用工具(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        pass

class 正常(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        if exec_res == 'token溢出':
            return 'token溢出'
        elif exec_res == '循環':
            return '循環'

class 提煉(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        if exec_res == '循環':
            return '循環'

class 注入變化(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        pass

class 檢查工具(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        pass

class 添加消息(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        pass

class 提煉消息(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        pass

class 提煉消息(Node):
    def prep(self, shared):
        pass
    def exec(self, prep_res):
        return prep_res
    def post(self, shared, prep_res, exec_res):
        pass

from pocket import ObservableShare
def pocketflow(payload,headers={},doc=False,watch=None):
    shared = ObservableShare(payload,callback=watch)
    # shared['token'] = headers
    One = 用戶輸入()
    Two = LLM_調用()
    Three = 返回答案()
    Four = 調用工具()
    Five = 正常()
    Six = 提煉()
    seven = 注入變化()

    eight = 檢查工具()
    nine = 添加消息()

    
    
    One >> Two
    Two - "text" >> Three
    Two - "tools" >> Four
    
    

    Four >> eight >> nine >> Five

    Five - "token溢出" >> Six
    Five - "循環" >> seven

    Six - "循環" >> Two
    seven >> Two

    
    flow = Flow(start=One)
    
    pocket_graph = build_mermaid(flow)
    from IPython.display import Markdown, display
    display(Markdown(f"```mermaid\r\n{pocket_graph}"))
    docs = {}
    return EXEC(flow,docs,shared,doc)


        