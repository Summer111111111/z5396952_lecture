"""yf_example3.py

The purpose of this module is to

download stock price data for Qantas

for a given year and save the information

in a CSV file"""



import yfinance as yf
import os
import toolkit_config as cfg

def qan_prc_to_csv(year):
    """ Downloads Qantas stock prices from Yahoo Finance and saves the
        information in a CSV file

        Parameters
        ----------
        tic : str
            Ticker

        pth : str
            Location of the output CSV file

        start: str, optional
            Download start date string (YYYY-MM-DD)
            If None (the default), start is set to '1900-01-01'

        end: str, optional
            Download end date string (YYYY-MM-DD)
            If None (the default), end is set to the most current date available
        """


    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    tic = 'QAN.AX'
    df = yf.download(tic, start=start_date, end=end_date)
    file_name = f"qan_prc_{year}.csv"
    pth = os.path.join(cfg.DATADIR, file_name)
    df.to_csv(pth)





if __name__ == "__main__":
    qan_prc_to_csv(2020)






