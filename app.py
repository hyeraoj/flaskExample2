# 사전 설치 : pip install flask pymysql requests
from flask import Flask, render_template, request, redirect, url_for
from backend.services.bmi import BMICalculator
from backend.models.db import Database
import atexit   # 애플리케이션 종료시 실행을 요청 (ex. DB연결 종료)

def create_app():
    app = Flask(__name__)   # Flask 앱 초기화
    
    db = Database()   # DB 초기화

    # 애플리케이션 종료 시 DB 연결 종료
    atexit.register(db.close)

    # 라우트 등록
    from backend.routes.bmi_routes import bmi_bp, init_db
    init_db(db) # DB 인스턴스를 라우터에 주입
    app.register_blueprint(bmi_bp)
    return app

# 애플리케이션 생성
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)