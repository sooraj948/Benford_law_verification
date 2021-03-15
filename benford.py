
import matplotlib.pyplot as pl

def benford(l):#l is a list of numbers 
    
    n=[str(i)[0] for i in l]

    return n #returns list of first digits(that is leftmost digits)

def count_of_dig(n):
    d={}
    for i in n:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    return d#returns a dictionary which maps digits to number of times they occur in list

def find_percentage(l):

    n=benford(l)
    length=len(l)
    d=count_of_dig(n)
    keys=list(d.keys())
    keys.sort()
    valuesper=[d[i]/length*100 for i in keys]#finds percentage of occurence of each of the digits

    return (keys,valuesper)#returns tuple 

def plot_line(keys,valuesper,title):#plots line graph with x axis as keys and y axis as valuesper

    pl.plot(keys,valuesper,color="red")
    pl.xlabel("Digits")
    pl.ylabel("Percentage of occurence")
    pl.title(title)

    pl.show()

def plot_bar(keys,valuesper,title):#bar graph

    pl.bar(keys,valuesper)
    pl.xlabel("Digits")
    pl.ylabel("Percentage of occurence")
    pl.title(title)

    pl.show()

def plot_bar_line(keys,valuesper,title):#plots both in same graph

    pl.plot(keys,valuesper,color="red")
    pl.bar(keys,valuesper)
    pl.xlabel("Digits")
    pl.ylabel("Percentage of occurence")
    pl.title(title)

    pl.show()



if __name__=="__main__":

    l=benford([123,2,5,3,2,4,2223,1])

    print(l)

    fp=find_percentage(l)
    print(fp)

    plot_bar_line(fp[0],fp[1])


