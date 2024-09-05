
import pymysql
from urllib.parse import urlparse

# 데이터베이스에 접속할 URL
database_url = "mysql+pymysql://root:11111111@ls-f5492fc3bff8be679d69c95f451ce31a484356aa.ctawq4asic5c.ap-northeast-2.rds.amazonaws.com:3306/dbsbb"

# URL을 파싱하여 연결 정보 추출
url = urlparse(database_url)

# 데이터베이스 연결 설정
connection = pymysql.connect(
    host=url.hostname,
    port=url.port,
    user=url.username,
    password=url.password,
    database=url.path[1:],  # Remove the leading '/'
    cursorclass=pymysql.cursors.DictCursor  # DictCursor로 설정하여 결과를 dict 형태로 가져오기
)

try:
    with connection.cursor() as cursor:
        # 쿼리 실행
        sql = "SELECT * FROM your_table_name"
        cursor.execute(sql)
        # 결과 가져오기
        result = cursor.fetchall()
        # 결과 출력
        for row in result:
            print(row)
finally:
    # 연결 종료
    connection.close()
