from flask import Flask, request
from flask_restx import Api, Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)
api = Api(app)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # JWT 시크릿 키 설정
jwt = JWTManager(app)

user = [
    {"id": 1, "username": "jung", "password": "password"}
]

@api.route('/login')
class Login(Resource):
    def post(self):
        # 로그인 로직
        # 유저 인증 성공 시
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        
        if username == "jung" and password == "password":
          access_token = create_access_token(identity='user')
          return {'access_token': access_token}
        else:
          return False,401

@api.route('/protected')
class Protected(Resource):
    @jwt_required()  # 인증이 필요한 API 엔드포인트
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)
