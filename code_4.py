import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'

def get_big_mac_price_by_year(year,country_code):
    filtered = df[(df['date'].str.startwith(str(year))) & (df['iso_a3'].str.lower() == country_code.lower())]
    return round(filtered['dollar_price'].mean(), 2)

def get_big_mac_price_by_country(country_code):
    filtered = df[df['iso_a3'].str.lower() == country_code.lower()]
    return round(filtered['dollar_price'].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    filtered = df[(df['date'].str.startwith(str(year)))]
    cheapest = filtered.loc[filtered['dollar_price'].idxmin()]
    return f"{cheapest['name']}({cheapest['iso_a3']}): ${round(cheapest['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    filtered = df[df['date'].str.startswith(str(year))]
    expensive = filtered.loc[filtered['dollar_price'].idxmax()]
    return f"{expensive['name']}({expensive['iso_a3']}): ${round(expensive['dollar_price'], 2)}"

if __name__ == "__main__":
    year = input("Enter a year: ")
    country_code = input("Enter a country code: ").lower()

    print(f"\nAverage Big Mac price in {year} for {country_code.upper()}: ${get_big_mac_price_by_year(year, country_code)}")
    print(f"Average Big Mac price in {country_code.upper()}: ${get_big_mac_price_by_year(year, country_code)}")
    print(f"Cheapest Big Mac price in {year}: {get_the_most_expensive_big_mac_price_by_year}")
    print(f"Most expensive Bif Mac price in {year}: {get_the_most_expensive_big_mac_price_by_year(year)}")