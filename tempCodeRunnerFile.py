from flask import Flask, render_template, request    # 匯入 flask 相關套件
from flask_socketio import SocketIO, emit # 匯入 flask SocketIO 相關套件
app = Flask(__name__)
# 初始化 SocketIO ，允許跨域連線，並指定使用 eventlet 非同步模式
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")
@app.route("/")
def index():
  return render_template("index.html")

clients = {} # 紀錄線上使用者 { sid: {"username": str} }
# ===== SocketIO📡 事件處理區 =====
# 計算目前線上已設定使用者名稱的數量，並廣播更新給所有人
def broadcast_user_count():
  emit("user_count",
    {"count": len([c for c in clients.values() if c["username"]])},broadcast=True)

if __name__ == "__main__":
   socketio.run(app, host="0.0.0.0", port=5000, debug=True)