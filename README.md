# Benford_law_verification

What is Benford's Law:

The law states that in many naturally occurring collections of numbers, the leading digit is likely to be small. In sets that obey the law, the number 1 appears as the leading significant digit about 30% of the time, while 9 appears as the leading significant digit less than 5% of the time. 

https://en.wikipedia.org/wiki/Benford%27s_law

#What I tried as of 15/3/2021:

For our  first sem's final python project I had created a webscraping program which gets data from the website worldometer(https://www.worldometers.info/coronavirus/). Using the datasets that the very same program provides I wanted to verify benford's law. 

#What this project does as of 15/3/2021:

The benford.py is highly polymorphic in my opinion and can be used for many datasets. This program has functions which return list of most signififcant digits from a list of numbers , finds frequency of occurence of these digits , finds percentage of occurence of these digits and also functions which plot graphs of the digits on x axis vs the percentage of occurence of those digits as the most signficant digit on the y axis.

The webscrape_covid_data.py does the actual webscraping and retrieval of coronavirus data. It has functions which can return total case data, daily new case data, active case data and deaths data for any valid country(here i mean if it exists on wolrdometer).

The benford_covid.py imports the above two programs and plots graphs.


#Conclusions:

After a prelimnary examination of a few of the graphs of a few random countries with relatively large datasets , the conclusion I came to was that they don't follow Benford's law very well.Although 1s and 2s do occur more than 8s and 9s the graphs don't follow the logarithmic curve characteristic of datasets which do follow Benford's Law.

Maybe the datasets are not large enough or I have not applied the law correctly.


Libraries used:

Matplotlib: pip install matplotlib

Beautiful Soup: pip install bs4 ; pip install lxml

Might also have to separately install tkinter if it does not get downloaded alongwith matplotlib

tkinter for ubuntu:  sudo apt-get install python-tk







