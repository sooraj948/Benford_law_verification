import benford as b
import webscrape_covid_data as ws
import sys

try:

    # country= input("Enter country name : ")
    country =  sys.argv[1]
    c=ws.CovidData(country)

    choice = int(input("Choose one of the following.\n1-Total cases\n2-Daily new cases\n3-Active cases\n4-Deaths\n"))

    if choice==1:
        l=c.total_case_data()
        t= b.find_percentage(l)
        b.plot_bar_line(t[0],t[1],"total case data")

    elif choice==2:

        l=c.daily_new_case_data()
        t= b.find_percentage(l)
        b.plot_bar_line(t[0],t[1],"daily new case data")

    elif choice==3:

        l=c.active_case_data()
        t= b.find_percentage(l)
        b.plot_bar_line(t[0],t[1],"active case data")

    elif choice==4:

        l=c.deaths_data()
        t= b.find_percentage(l)
        b.plot_bar_line(t[0],t[1],"deaths data")

    else:
        print("pls follow instructions")





    
    
    # b.plot_line(t[0],t[1])    

    # b.plot_bar(t[0],t[1])

    

except IndexError:
    print("Pls enter country name also along with the run command. Eg python3 benford_covid.py india")
    

except Exception as e:
    print(e)

except:
    print("Pls input only the appropriate number")



