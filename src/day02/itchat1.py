
# mychat1.py
import itchat
from itchat.content import TEXT

@itchat.msg_register(TEXT)   # 注册处理文本信息
def simple_reply(msg):
    print(msg.text)

itchat.auto_login(hotReload=True)  # hotReload=True表示短时间关闭程序后可重连
itchat.run()