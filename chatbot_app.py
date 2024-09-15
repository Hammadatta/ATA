import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headlines = []
    for item in soup.select('.titleline a'):
        headlines.append(item.get_text())
    
    return headlines

st.set_page_config(page_title="ATA Scrapper", page_icon=":newspaper:", layout="wide")

st.image("ata_scrapper_logo.png", use_column_width=True)

st.title("ATA Scrapper")

if st.button('Scrape News Headlines'):
    with st.spinner('Scraping...'):
        headlines = scrape_news()
        st.write(f"Found {len(headlines)} headlines:")
        for idx, headline in enumerate(headlines, start=1):
            st.write(f"{idx}. {headline}")

st.write("Click the button above to scrape the latest news headlines.")

