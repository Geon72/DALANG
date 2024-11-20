# Django에서 한국수출입은행 API를 활용하여 24.11.18 기준 이전 1년치 데이터 불러오기
import requests
# from django.shortcuts import render
from datetime import datetime, timedelta
from .models import ExchangeRate

def fetch_exchange_rates():
    # 한국수출입은행 OPEN API URL
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON"
    api_key = "tRC7RzqBa0ttDTcmKoU8G0cxd4vZxahD"  # 발급받은 API 키를 입력하세요.

    # 오늘 날짜를 기준으로 1년 전까지의 날짜를 생성
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    current_date = start_date
    target_currencies = ["USD", "JPY(100)", "EUR", "CNH"]

    while current_date <= end_date:
        search_date = current_date.strftime("%Y%m%d")
        params = {
            "authkey": api_key,
            "searchdate": search_date,
            "data": "AP01"
        }

        try:
            response = requests.get(url, params=params)
            data = response.json()

            for rate in data:
                if rate["cur_unit"] in target_currencies:
                    # 기존 데이터가 있는지 확인하고 없으면 저장
                    if not ExchangeRate.objects.filter(currency_unit=rate["cur_unit"], date=current_date.date()).exists():
                        ExchangeRate.objects.create(
                            currency_unit=rate["cur_unit"],
                            exchange_rate=float(rate["deal_bas_r"].replace(",", "")),
                            date=current_date.date()
                        )
        except Exception as e:
            print(f"{search_date} 데이터 가져오는 중 오류 발생: {e}")

        # 하루를 더합니다.
        current_date += timedelta(days=1)

def exchange_rate_view(request):
    # 데이터를 불러오는 함수를 호출하여 1년치 데이터를 적재
    fetch_exchange_rates() # 이미 불러와서 주석처리 / 20241118 1638 완료

    # 최근 데이터 10개를 가져옵니다.
    exchange_rates = ExchangeRate.objects.all().order_by('-date')[:10]

    return render(request, 'exchange_rate/exchange_rate.html', {'exchange_rates': exchange_rates})


# Django에서 1년치 국가별 환율 추이 꺾은선 그래프로 표현
import matplotlib
matplotlib.use('Agg')  # GUI 백엔드를 사용하지 않도록 설정
import matplotlib.pyplot as plt
import pandas as pd
from django.shortcuts import render
from io import BytesIO
import base64
from .models import ExchangeRate

def plot_exchange_rate_trends():
    # Fetch data from the ExchangeRate model
    data = ExchangeRate.objects.all().values('currency_unit', 'exchange_rate', 'date')
    df = pd.DataFrame(data)
    
    # Check if data is empty
    if df.empty:
        print("DataFrame is empty. No data to plot.")
        return None

    # Convert date to datetime and sort by date
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date')

    # Define the target currencies, simplified keys, and colors
    target_currencies = {
        "USD": {"key": "USD", "color": "blue"},
        "JPY(100)": {"key": "JPY", "color": "red"},
        "EUR": {"key": "EUR", "color": "green"},
        "CNH": {"key": "CNH", "color": "orange"}
    }
    graphs = {}

    # Create a figure for each currency
    for full_key, details in target_currencies.items():
        subset = df[df['currency_unit'] == full_key]
        plt.figure(figsize=(10, 6))
        plt.plot(subset['date'], subset['exchange_rate'], label=full_key, color=details['color'])
        plt.title(f'Exchange Rate Trend for {full_key}', fontsize=14)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Exchange Rate', fontsize=12)
        plt.legend()
        plt.grid(visible=True, linestyle='--', alpha=0.5)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot to a BytesIO object
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        
        # Encode the image to base64 and store in the dictionary with simplified key
        graphs[details['key']] = base64.b64encode(image_png).decode('utf-8')

        # Close the plot to free memory
        plt.close()

    return graphs

def exchange_rate_chart_view(request):
    # Generate the graphs
    graphs = plot_exchange_rate_trends()

    # Check if graphs are None
    if not graphs:
        return render(request, 'exchange_rate/exchange_rate_chart.html', {'graphs': None})
    
    return render(request, 'exchange_rate/exchange_rate_chart.html', {'graphs': graphs})