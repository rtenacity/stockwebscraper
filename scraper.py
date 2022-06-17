from bs4 import BeautifulSoup
import requests

def StockScraper(name, mainurl):
  main = requests.get(mainurl)
  doc1 = BeautifulSoup(main.text, "html.parser")
  file1 = open("values.txt","a")
  print(name)
  
  fairvalue = doc1.find('div', {"class" : "Fw(b) Fl(end)--m Fz(s) C($primaryColor"})
  try:
    fairvaluevar = fairvalue.string
    print(fairvaluevar)
  except:
    print(name + " was missing information. click here: " + mainurl)
  
  estreturn = doc1.find('div', {"class" : "IbBox Ta(start) C($tertiaryColor)"})
  try:
    estreturnvar = estreturn.string
    print(estreturnvar)
  except:
    print(name + " was missing information. click here: " + mainurl)
    
  esgscore = doc1.find('div', {"class" : "Fz(27px) Fw(600) D(ib)"})
  try:
    esgscorevar = esgscore.string
    print(esgscorevar)
  except:
    print(name + " was missing information. click here: " + mainurl)

  recrating = doc1.find('div', {"class": "B(8px) Pos(a) C(white) Py(2px) Px(0) Ta(c) Bdrs(3px) Trstf(eio) Trsde(0.5) Arrow South Bdtc(i)::a Fw(b) Bgc($buy) Bdtc($buy)"})
  try:
    recratingvar = recrating.string + " \n"
    print(recratingvar)
  except:
    recratingvar = name + " was missing information. click here: " + mainurl + " \n"
    print(recratingvar)
  try:
    file1.write(name + "; ")
    file1.write(fairvalue.string + "; ")
    file1.write(estreturn.string + "; ")
    file1.write(esgscore.string + "; ")
    file1.write(recratingvar)
  except:
    print(name + " was missing information")
StockScraper("American Express Company", "https://finance.yahoo.com/quote/AXP/") 
StockScraper("Amgen, Inc.", "https://finance.yahoo.com/quote/AMGN/") 
StockScraper("Apple Inc", "https://finance.yahoo.com/quote/AAPL/") 
StockScraper("Boeing Co", "https://finance.yahoo.com/quote/BA/")
StockScraper("Caterpillar Inc.", "https://finance.yahoo.com/quote/CAT/")
StockScraper("Cisco Systems Inc", "https://finance.yahoo.com/quote/CSCO/")
StockScraper("Chevron Corporation", "https://finance.yahoo.com/quote/CVX/")
StockScraper("Goldman Sachs Group Inc", "https://finance.yahoo.com/quote/GS/")
StockScraper("Home Depot Inc", "https://finance.yahoo.com/quote/HD/")
StockScraper("Honeywell International Inc", "https://finance.yahoo.com/quote/HON/")
StockScraper("IBM Common Stock", "https://finance.yahoo.com/quote/IBM/")
StockScraper("Intel Corporation", "https://finance.yahoo.com/quote/INTC/")
StockScraper("Johnson & Johnson", "https://finance.yahoo.com/quote/JNJ/")
StockScraper("Coca-Cola Co", "https://finance.yahoo.com/quote/KO/")
StockScraper("JPMorgan Chase & Co", "https://finance.yahoo.com/quote/JPM/")
StockScraper("McDonald's Corp", "https://finance.yahoo.com/quote/MCD/")
StockScraper("3M Co", "https://finance.yahoo.com/quote/MMM/")
StockScraper("Merck & Co., Inc.", "https://finance.yahoo.com/quote/MRK/")
StockScraper("Microsoft Corporation", "https://finance.yahoo.com/quote/MSFT/")
StockScraper("Nike Inc", "https://finance.yahoo.com/quote/NKE/")
StockScraper("Procter & Gamble Co", "https://finance.yahoo.com/quote/PG/")
StockScraper("Travelers Companies Inc", "https://finance.yahoo.com/quote/TRV/")
StockScraper("UnitedHealth Group Inc", "https://finance.yahoo.com/quote/UNH/")
StockScraper("Salesforce Inc", "https://finance.yahoo.com/quote/CRM/")
StockScraper("Verizon Communications Inc.", "https://finance.yahoo.com/quote/VZ/")
StockScraper("Visa Inc", "https://finance.yahoo.com/quote/V/")
StockScraper("Walgreens Boots Alliance Inc", "https://finance.yahoo.com/quote/WBA/")
StockScraper("Walmart Inc", "https://finance.yahoo.com/quote/WMT/")
StockScraper("Walt Disney Co", "https://finance.yahoo.com/quote/DIS/")
StockScraper("Dow Inc", "https://finance.yahoo.com/quote/DOW/")
