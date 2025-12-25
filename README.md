# All-About-Elements-and-Compound
You can search periodic table and chemical properties here, just by asking what do you want to know. (This is my final report for my academic so don't mind it if it's seems so bad, I'm just a beginner)

(1)程式的功能與技術原理

There are 3 equations 1.)Heat of Reaction: q = mcΔt 2.)Gibbs Free Energy: ΔG = ΔH-TΔS 3.)Electrochemical Energy: -nFE.
I use "def" and return the answer as the equation write.

(2)使用方式

Get your API key named it as "APIkey.txt" or change the name in line 33 then put the file in the same folder.

select mode: There are 3 mode

1. periodic table

2. chemical properties

3. energy calculation

if choose 1 the simple periodic table will show up
if choose 2 there are 2 choices in yes no:

y. specific property

n. all the properties

if press y then input your element/compound and the properties you want to know.

if press n then input your element/compound only

if press others the programme stopped.

when you press n remember to type "exit", "quit",or "bye" then the monitor show up goodbye to end the programme, or the programme continue

if choose 3 there are 3 kind of energy to calculate:

x. Heat of Reaction (Calorimetry)
y. Gibbs Free Energy (ΔG)
z. Electrochemical Energy

find the one you need

after calculate finished the programme ended

(3)程式的架構

I use a lot of "def" in the code the first one is for the periodic table which has the size of picture 12*6 select the style and the length width of table

GEMINI KEYS has the form from "
Unveilling LLM Power with Python: Create your own LLM-powered agent" in the lecture of class

second "def" is for the chemical properties GENAI will print everythings     
    - Full name
    - Formula
    - Atomic mass
    - Boiling point
    - Melting point
    - Appearance
    - Density
    - Solubility
    - Properties
    - Dangerousness
user can added others if needed

Third"def" is for specific information so we don't lose too much time on searching too  much things

the 4,5,6 "def are the equation of energy which return the equation itself

then the main code started by asking which kind of function you like using "if" and "elif" function elif a == "2" has a loop so it won't stop unless you type exit", "quit",or "bye" or make it error by typing others letters in the question"Do you want specific property? y/n "

(4)開發過程

The idea came from the chemistry lab that I need to search the chemical properties and mostly one website didn't include all of the properties so I need to search for a long time.So if there is some that's mycode might look alike that's an accident.

I didn't install the google package in my labtop so I can't used the code "from google import genai" and I didn't remember the name which professor said that "pip install ????" so I install a lot of wrong package include install google, google.generativeai etc. Sometimes AI don't give the correct answer. So I solved it by asking AI repeatly and finally I install the correct package!:D

The code that Copilot gave wasn't correct so I need to detect it again carefully

I wish that 'a=="3"' can have a loop but the code always error so I give it up

Typing element is really tiring and at last prof. tell me that you can ask AI to help you write down these(Ah, my godness)

(5)參考資料來源

All the information come from copilot and the lectures of prof. Lin (林祥泰)

(6)程式修改或增強的內容
The loop is my thinking and I quite don't understand why I can use in 'a=="2"' but can't in ' a =="3"'
'elif a == "3"' I ask the structure from Copilot but others I added them by myself and my thinking so it might seems to be a lot of typing letters rather than other











