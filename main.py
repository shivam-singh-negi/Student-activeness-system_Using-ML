import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy

html_text = requests.get("https://www.sanfoundry.com/1000-database-management-system-questions-answers/").text
soup = BeautifulSoup(html_text, 'lxml')
question = []
options = []
answer = []
for wrapper in soup.find_all("p"):
    if re.findall("^[0-9]", wrapper.text):
        question.append(wrapper.text.split("\n")[0])
        try:
            options.append([wrapper.text.split("\n")[1], wrapper.text.split("\n")[2], wrapper.text.split("\n")[3],
                            wrapper.text.split("\n")[4]])
        except:
            options.append(-1)
for wrapper in soup.find_all('div', class_="collapseomatic_content"):
    if re.findall("^Answer:", wrapper.text.lstrip()):
        answer.append(wrapper.text.split("\n")[0][8:])

mcq = {'Question': question, 'Options': options, 'Answer': answer}
df = pd.DataFrame(mcq)
df.drop(df.loc[df['Options'] == -1].index, inplace=True)
print(df["Options"])
print(len(df["Options"]))
li = df.Options.tolist()
option1 = [i[0] for i in li]
option2 = [i[1] for i in li]
option3 = [i[2] for i in li]
option4 = [i[3] for i in li]
df.drop(["Options"], axis=1,inplace=True)

df["Option1"] = option1
df["Option2"] = option2
df["Option3"] = option3
df["Option4"] = option4
print(df)
df.to_csv("final2.csv")

print(option2)
print(len(option2))

question.clear()
options.clear()
answer.clear()
