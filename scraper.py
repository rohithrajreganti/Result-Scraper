""" python Script ito check  results of all pesit south campus CS students"""
"""http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs124&sem=2"""

from bs4 import BeautifulSoup
import urllib2

files=['http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs106']
resultfile=open(r"/home/rohithrajr/Desktop/results.txt","a")
parsablerf=open(r"/home/rohithrajr/Desktop/parsableresultss.txt","a")



urlstrings=[]
for i in range(00,10) :
        urlstrings.append("http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs"+ str("00"+str(i))+"&sem=2")

for i in range(10,100) :
        urlstrings.append("http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs"+ str("0"+str(i))+"&sem=2")

for i in range(100,190):
        urlstrings.append("http://result.vtu.ac.in/cbcs_results2016.aspx?usn=1pe15cs"+ str(i)+"&sem=2")



for i in urlstrings :
    file1=urllib2.urlopen(i)
    soup=BeautifulSoup(file1,'lxml')

    tag= soup.select("#txtName")
    for i in tag :
      # i is a tag
      p=i['value']
      resultfile.write(p+(30-len(str(p)))*" ")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',
      

    tag2= soup.select("#txtUSN")
    for i in tag2 :
      # i is a tag
      p=i['value']
      resultfile.write(p+"\t")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',


    tag4= soup.select("#txtGP1")
    for i in tag4 :#math
      # i is a tag
      p=i['value']
      resultfile.write(p+"\t")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',


    tag5= soup.select("#txtGP2")
    for i in tag5 :#chem
      # i is a tag
      p=i['value']
      resultfile.write(p+"\t")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',


    tag6= soup.select("#txtGP3")
    for i in tag6 :#pcd
      # i is a tag
      p=i['value']
      resultfile.write(p+"\t")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',


    tag7= soup.select("#txtGP4")
    for i in tag7 :#cad
      # i is a tag
      p=i['value']
      resultfile.write(p+"\t")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',


    tag8= soup.select("#txtGP5")
    for i in tag8 :#basic elec
      # i is a tag
      p=i['value']
      resultfile.write(p+"\t")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',


    tag9= soup.select("#txtGP6")
    for i in tag9 :#pcd lab
      # i is a tag
      p=i['value']
      resultfile.write(p+"\t")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',


    tag10= soup.select("#txtGP7")
    for i in tag10 :#chemlab
      # i is a tag
      p=i['value']
      resultfile.write(p+"\t")
      parsablerf.write(p+"-")

      print i['value']+' '+'-',






    tag3=soup.select("#lblSGPA")
    for i in tag3 :
      # i is a tag
      p=i.string
      resultfile.write(p+"\n")
      parsablerf.write(p+"\n")

      print "SGPA="+i.string,

    print("\n")


resultfile.close()



