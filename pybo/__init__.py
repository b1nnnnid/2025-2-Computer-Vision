from flask import Flask, send_from_directory, render_template, request
from werkzeug.utils import secure_filename
import os	
import cv2
import numpy as np
from .img_proc import otsu_binarization, histogram_equalization, clahe_equalization, gaussian_blur, sharpening
from .img_proc import bilateral, edge_preserving, style_filter

def create_app() :
    app = Flask(__name__) 	# app이라는 flask application 생성
            # __name__ : 실행되는 모듈이 담기는 변수 , 우리는 pybo 모듈을 실행할 예정

    app.secret_key = os.urandom(24) # 세션 및 쿠키 사용을 위한 비밀 키 생성
    app.config['RESULT_FOLDER'] = 'result_images'   # 결과 이미지 저장 폴더 (미리 생성 필요)
    app.config['UPLOAD_FOLDER'] = 'uploads'         # 업로드 이미지 저장 폴더 (미리 생성 필요)

    @app.route('/upload_img/<filename>') # 예, http://127.0.0.1:5000/upload_img/eagle.jpg
    def upload_img(filename):		# 업로드된 이미지를 브라우저에 보여줌
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    @app.route('/result_img/<filename>') # 예, http://127.0.0.1:5000/result_img/eagle_otsu_119.jpg
    def result_img(filename):       # 처리된 결과 이미지를 브라우저에 보여줌
        return send_from_directory(app.config['RESULT_FOLDER'], filename)
    
    @app.route('/img_result', methods=['GET', 'POST'])  # 예, http://127.0.0.1:5000/img_result
    def img_result():
        if request.method == 'POST':    # POST 요청에서 파일 가져오기

            # HTML 폼에서 선택한 이미지 처리 스타일 가져오기
            style = request.form.get('style')       
            print(f"style: {style}")

            # 파일을 uploads 폴더에 저장
            f = request.files['file']
            basepath = os.path.dirname(__file__)
            file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename)) # 예, C:\....\pybo\uploads\eagle.jpg
            f.save(file_path)
            file_name = os.path.basename(file_path)	# 예, eagle.jpg
            print(file_path)		# 업로드된 파일 경로 출력
            print(file_name)		# 업로드된 파일 이름 출력
            
            # 업로드된 이미지 읽기
            img = cv2.imread(file_path)

            # style 값에 따라 이미지 처리 방식 결정
            
            # 과제1: Otsu, 히스토그램 평활화, CLAHE 실행
            if style == "Otsu": # Otsu 이진화
                th, processed = otsu_binarization(img)

                title = f"Otsu 이진화 (임계값: {int(th)})"
                result_fname = os.path.splitext(file_name)[0] + "_otsu_" + str(int(th)) + ".jpg"		# 예, eagle_otsu_119.jpg

            elif style == "Equalization":   # 히스토그램 평활화
                processed = histogram_equalization(img)

                title = "히스토그램 평활화"
                result_fname = os.path.splitext(file_name)[0] + "_equalization.jpg"		# 예, eagle_equalization.jpg

            elif style == "CLAHE":   # CLAHE (Contrast Limited Adaptive Histogram Equalization)
                processed = clahe_equalization(img)

                title = "CLAHE (적응형 히스토그램 평활화)"
                result_fname = os.path.splitext(file_name)[0] + "_clahe.jpg"		# 예, eagle_clahe.jpg
            
            # 과제2) 영역처리 연산 5개 추가
            #가우시안 블러 함수 추가(스무딩 중 택 1)
            elif style == "Gaussian":
                processed = gaussian_blur(img)
                
                title = "Gaussian Blur"
                result_fname = os.path.splitext(file_name)[0] + "_gaussian.jpg"
            
            #샤프닝 함수 추가(에지 필터 중 택 1)    
            elif style == "Sharpening":
                processed = sharpening(img)
                
                title = "Sharpening"
                result_fname = os.path.splitext(file_name)[0] + "_sharpening.jpg"
            
            #양방향, 에지 보존, 스타일 함수 추가(특수효과 필터 중 택3)
            elif style == "Bilateral":
                processed = bilateral(img)
                
                title = "Bilateral Filter"
                result_fname = os.path.splitext(file_name)[0] + "_bilateral.jpg"
                
            elif style == "Edge Preserving":
                processed = edge_preserving(img)
                
                title = "Edge Preserving Filter"
                result_fname = os.path.splitext(file_name)[0] + "_edgep.jpg"
                
            elif style == "Style":
                processed = style_filter(img)
                
                title = "Style Filter"
                result_fname = os.path.splitext(file_name)[0] + "_style.jpg"
                
            # 처리된 이미지를 result_images 폴더에 저장
            result_path = os.path.join(basepath, 'result_images', secure_filename(result_fname))
            fname = os.path.basename(result_path)
            cv2.imwrite(result_path, processed)

            # 결과 페이지 렌더링 : 클라이언트에게 보여줌
            return render_template('img_result.html', file_name=file_name, result_file=fname, style_title=title)

    @app.route("/") 	# ()안의 주소에 접속하면 그 바로 아랫줄에 있는 함수를 호출
                        # /는 https://ip주소/ 를 의미
    #def hello_pybo():
    #    return 'Hello__ Pybo'
    def index():
        return render_template('index.html')    # templates/index.html 파일을 읽어서 브라우저에 보여줌

    return app