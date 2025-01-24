import data_download as dd
import data_plotting as dplt


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д - 1d, 5д - 5d, 1мес - 1mo, 3мес - 3mo, 6мес - 6mo, 1г - 1y, 2г - 3y, 5г - 5y, 10л - 10y, с начала года - ytd, макс - max.")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = input("Введите период для данных (например, '1mo' для одного месяца): ")


    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period)

    print(dd.notify_if_strong_fluctuations(stock_data))

    export = input('Хотите экспортировать выбранные данные? Ответьте Да / Нет')
    if export.lower() == 'a' or export.lower() == 'ano':
        dd.export_data_to_csv(stock_data)

if __name__ == "__main__":
    main()
