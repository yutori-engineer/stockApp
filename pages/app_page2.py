import streamlit as st
import streamlit_gchart as gchart

cat_data = [
    ['Phrases'],
    ['cats are better than dogs'],
    ['cats eat kibble'],
    ['cats are better than hamsters'],
    ['cats are awesome'],
    ['cats are people too'],
    ['cats eat mice'],
    ['cats meowing'],
    ['cats in the cradle'],
    ['cats eat mice'],
    ['cats in the cradle lyrics'],
    ['cats eat kibble'],
    ['cats for adoption'],
    ['cats are family'],
    ['cats eat mice'],
    ['cats are better than kittens'],
    ['cats are evil'],
    ['cats are weird'],
    ['cats eat mice']
]
    
gchart.gchart(key="cat_chart", data=cat_data, chartType="WordTree", 
    width=600, height=400, wordtree={"format": "implicit", "word": "cats"})