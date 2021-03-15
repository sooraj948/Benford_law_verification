import benford as b
import webscrape_covid_data as ws
import sys

try:

    # country= input("Enter country name : ")
    country =  sys.argv[1]
    c=ws.CovidData(country)

    l=c.active_case_data()
    
    t= b.find_percentage(l)
    
    # b.plot_line(t[0],t[1])    

    # b.plot_bar(t[0],t[1])

    b.plot_bar_line(t[0],t[1],"active case data")
    

except Exception as e:
    print(e)



