from flask import Flask, request
from flask_restx import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from Database.user.user_model import User,get_user
from Database.postgres import session, base
import datetime


app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # JWT 시크릿 키 설정
jwt = JWTManager(app)

#TestData
user = [
    {
        "id": 1, 
        "username": "jung",
        "password": "password"
    },
    {
        'id':2,
        'username':'yura',
        'password':'password',
    }
]

# User Model 에서 해당 username의 로그인 정보 확인
# 일치하면 access_token에 해당 user 정보 담아서 리턴
@api.route('/login')
class Login(Resource):
    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        
        user = session.query(User).filter_by(username=username).first()

        if user is None:
            return {
                "message": "존재하지 않는 사용자입니다"
                }
        if user.password == password:
            access_token = create_access_token(
                identity='user',
                expires_delta=datetime.timedelta(seconds=30), 
                additional_claims={
                    "username": user.username
                }
            )
            return {
                "message": "로그인 성공",
                "access_token": access_token
            }
        else:
            return {
                "message": "비밀번호가 일치하지 않습니다"
            }

@api.route('/protected')
class Protected(Resource):
    @jwt_required()  # 인증이 필요한 API 엔드포인트
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)
