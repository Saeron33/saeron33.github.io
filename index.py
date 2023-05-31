from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # 웹 페이지 접근
    url = 'https://debatingday.com/status/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 테이블 찾기
    table = soup.find('table', {'class': 'table table-bordered text-center status-table'})

    # 결과를 저장할 리스트
    results = []

    # 행과 열 찾기
    for row in table.find('tbody').find_all('tr'):
        columns = row.find_all('td')
        if len(columns) > 1:  # 2번째 컬럼이 있을 경우
            a_tag = columns[1].find('a')
            if a_tag:  # a 태그가 있을 경우
                results.append(a_tag.text)  # a 태그의 텍스트를 리스트에 추가

    random_choice = random.choice(results)
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('index.html', results=results, random_choice=random_choice, current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True)
