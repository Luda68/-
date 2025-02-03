import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=translate_period(period))

    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    """ Функция для расчёта средней цены закрытия акций. Принимает DataFrame с данными и выводит среднюю цену закрытия. """
    average_price = data['Close'].mean()  # Среднее значение по колонке 'Close'
    print(f"Средняя цена за период: {average_price:.2f}")


def notify_if_strong_fluctuations(data, threshold=20):
    min_price = data['Close'].min()
    max_price = data['Close'].max()
    average_price = data['Close'].mean()

    dif = max_price - min_price
    percent = (dif / average_price) * 100
    if percent >= threshold:
        return f'Колебания цены акций фирмы превышает заданный порог {threshold}%.'
    else:
        return f'Колебания цены акций фирмы не превышает заданный порог {threshold}%.'


def add_rsi(data, window_length=14):
    delta = data['Close'].diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    average_gain = gain.rolling(window=window_length).mean()
    average_loss = loss.rolling(window=window_length).mean()

    rs = average_gain / average_loss

    data['RSI'] = 100 - (100 / (1 + rs))
    print(data)
    return data


def add_macd(data, short_window=12, long_window=26, signal_window=9):
    data['EMA_12'] = data['Close'].ewm(span=short_window, adjust=False).mean()
    data['EMA_26'] = data['Close'].ewm(span=long_window, adjust=False).mean()
    data['MACD'] = data['EMA_12'] - data['EMA_26']
    data['Signal'] = data['MACD'].ewm(span=signal_window, adjust=False).mean()
    return data



def export_data_to_csv(data, filename="dataframe.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


def translate_period(period):
    if period == '1д':
        return '1d'
    elif period == '5д':
        return '5d'
    elif period == '1мес':
        return '1mo'
    elif period == '3мес':
        return '3mo'
    elif period == '6мес':
        return '6mo'
    elif period == '1г':
        return '1y'
    elif period == '2г':
        return '2y'
    elif period == '5г':
        return '5y'
    elif period == '10л':
        return '10y'
    elif period == 'с начала года':
        return 'ytd'
    elif period == 'макс':
        return 'max'
    else:
        return period



