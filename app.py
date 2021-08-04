# importing libraries
import streamlit as st
import requests
from bs4 import BeautifulSoup


def scrap(c1, c2):
    urls=[]
    for i in range(11):
        stt='https://www.thehindu.com/search/?q=' + c1 + '&order=DESC&sort=publishdate&page='+str(i)
        urls.append(stt)

    xl=[]
    for url in urls:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        news = soup.find_all('div',class_='story-card-news')
        for new in news:
            headlines=new.find('a',class_='story-card75x1-text').text.strip()
            description=new.find('span',class_='light-gray-color story-card-33-text hidden-xs').text.strip()
            #author=new.find('a',class_='story-card-33-author-name.lnk').text
            geography=new.find('a',class_='section-name').text.strip()
            xl.append([headlines,description,geography,c1])
    count = 0
    for i in range(c2):
        count += 1
        st.header("News " + str(count))
        st.markdown("Headline : " + xl[i][0])
        st.write("Description : ",xl[i][1])
        st.write("Geography : ",xl[i][2])
        #st.write("Category : ",xl[i][3])
        st.write("")
        st.write("")
 
def reset():
    st.write("**Web scraping is an automated method used to extract large amounts of data from websites. The data on the websites are unstructured. Web scraping helps collect these unstructured data and store it in a structured form. There are different ways to scrape websites such as online Services, APIs or writing your own code**")
    st.write("In this application we are scrapping live news feed from the different newspapers in India.")
    st.image("pikachu.jpg")
def main():
    st.title("LIVE NEWS SCRAPPER")
    st.write("<< select the options in sidebar >>")

    st.sidebar.header("*Boored at everything, *")
    st.sidebar.header("*have some interesting news!! *")
    st.sidebar.write("")

    
    categories = ["National","International","Sports","Environment","political","tech"]
    choice1 = st.sidebar.selectbox("select type of news", categories)
    activities = [10,20,30,40,50]
    choice2 = st.sidebar.selectbox("select the no. of news", activities)
    if st.sidebar.button("GET"):
        with st.spinner(text="Fetching News"):
            measures = scrap(choice1,choice2)
        st.success('Done')
    if st.sidebar.button("RESET"):       
        reset()
if __name__ == "__main__":
    main()
