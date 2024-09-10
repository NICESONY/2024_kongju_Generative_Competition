from flask import Flask, request, render_template, send_from_directory
import os
from datetime import datetime

app = Flask(__name__)

# `frontend` 디렉토리의 경로 설정
frontend_dir = os.path.join(os.path.dirname(__file__), 'frontend')
output_dir = os.path.join(frontend_dir, 'outputs')

# 출력을 저장할 폴더가 없으면 생성
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 메인 페이지 라우팅
@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

# 데이터 처리 및 main_pipe 호출
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # 폼 데이터에서 날짜 추출
        date = request.form.get('date')
        
        # main_pipe 함수를 호출하여 데이터 처리
        output_image_path = main_pipe(date)
        
        # 결과를 HTML 템플릿으로 전달
        return render_template('index.html', image_path=output_image_path)

def main_pipe(date):
    # 예시로 딥러닝 모델을 사용하여 이미지를 생성하는 부분
    # 실제로는 모델 로드 및 예측 코드가 필요
    output_filename = f"output_{date}.png"
    output_path = os.path.join(output_dir, output_filename)
    
    # 딥러닝 모델을 사용하여 date를 기반으로 이미지를 생성하고 저장
    # 예시로 단순 이미지 생성 (실제로는 모델의 출력 저장)
    # 예: generated_image = model.predict(date) 등을 사용
    # 여기에 이미지 생성 로직이 들어갑니다.

    # 예제에서는 빈 이미지 파일을 생성
    from PIL import Image
    img = Image.new('RGB', (100, 100), color = (73, 109, 137))
    img.save(output_path)

    # 생성된 이미지 파일의 경로를 반환
    return output_filename

# 정적 파일 제공 (css, js, 이미지 등)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(frontend_dir, filename)

# 생성된 이미지 파일 제공
@app.route('/outputs/<path:filename>')
def outputs(filename):
    return send_from_directory(output_dir, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
