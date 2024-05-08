# SEC_10K_Filings_Project
This contains the code for retrieving,cleaning, and processing 10k filings from the SEC Edgar Database to produce a data visualization on risk factors for technology companies. The step-by-step explanation of the implementation is below.
# IMPORTANCE OF RISK FACTORS
Analyzing risk factors in technology companies' 10K filings provides valuable insights into the company's awareness of potential challenges and their proactive strategies for mitigating these risks. This information is crucial for investors, as it helps assess the company's resilience, management's ability to navigate uncertain environments, and the overall sustainability of the business model in a rapidly evolving industry.
# NOTES AND LIMITATIONS ABOUT DATA
We are looking at the risk factors for Apple and Google. For the backend implementation, we referenced a github repository "edgar tools", which allowed for retrieving, cleaning, and analyzing all of the 10K filings for up to 13 years. Due to extensive user testing, pivoting to the use of Langchain, and other implementation constraints, we had run out of free API credits. We were able to accurately represent up to 10 years worth of data. With additional API credits, we would have been able to attain the data and accurately represent it with a visualization for as many years as needed.


## Location of Coding Implementation
Preprocessing and Data Cleaning Code Location: Notebooks --> Edgar_api_item1a.ipynb

Text Parsing Code Location: Notebooks --> getAppleItem1a.ipynb

Streamlit App UI Implementation Location: src --> fintech_demo.py


## References
- [Project Helper Script](https://github.com/roshan-adusumilli/nlp_10-ks/blob/master/project_helper.py)
- [MIT License](https://spdx.org/licenses/MIT.html)
- [Edgar Tools](https://github.com/dgunning/edgartools)
- [Langchain 13 Minutes](https://github.com/rabbitmetrics/langchain-13-min)
- [ChatGPT](https://chatgpt.com/?oai-dm=1)




## DEMO
A demo of the project is in the docs folder within this repository, which is titled screen_recording.mp4
