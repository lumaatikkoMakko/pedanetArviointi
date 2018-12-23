'''
Created on 12. apr 2018

@author: MarkkuLeino
'''
import csv
import math
import glob
import numpy as np

def setGrade(x):
    #Input 0...1, output: 4...10
    #y = (y0-y1)/(x0-x1)(x-x0) + y0
    #y0=10, y1 = 4; x0 = 1; x1 = 0.1
    y = math.ceil( 4*( 6/(1-0.1)*(x-1)+10 ))/4
    if y < 4:
        y=4
    return y


def getPoints(t):
    summaSarake = 4     #E
    etunimiSarake = 3   #C
    sukunimiSarake = 2  #D

    with open(t, 'r') as f:
        data = list(csv.reader(f, delimiter=';'))

        #Pythonic way
        #https://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops#522578

        #Non pythonic way
    maxPoint = 0;
    num = 0
    points = []
    for i in range(1, len(data)):
        #print( data[i][summaSarake] )
        num = int(data[i][summaSarake])
        points.append( [ data[i][etunimiSarake], num] )
        if ( num > maxPoint ):
            maxPoint = num
            #print (num)
    #print (t + ' suurin: ' + str(maxPoint))

    grade = []
    for idx,val in enumerate(points):
        #print(val)
        if maxPoint == 0:
            grade.append([val[0], 0])
        else:
            grade.append( [val[0], setGrade( float( val[1] ) / float( maxPoint ) )] )

    #print( grade )
    return grade


class tehtavatPinnat:
    nimet = []
    #pisteet = np.zeros(shape=(16,20))
    #tehtavaNro = np.zeros(shape=(20,1)) 
    maxIndex = 19

    def __init__(self, pit):
        self.nimet = []
        self.pisteet = np.zeros(shape=(16,pit))+4
        self.tehtavaNro = []

    def find_element_in_list(self, element, list_element):
        try:
            index_element = list_element.index(element)
            return index_element
        except ValueError:
            return -1

    def isName(self, name):

        NameIndx = self.find_element_in_list( name, self.nimet )

        if( NameIndx == -1):
            self.nimet.append(name)
            NameIndx = self.nimet.__len__()-1
        #print("NIMET:")
        #print( self.nimet )
        return NameIndx


    def add(self, indx, assignNro, points):
        #print( 'Lisaa pisteet:')
        #print( points )
        self.tehtavaNro.append(assignNro)

        for idx,pinnat in enumerate( points ):
            NameIndx = self.isName( points[idx][0] )
            #print( 'NimiIndx: ', NameIndx )
            if ( points[idx][1]> self.pisteet[NameIndx][indx] ):
                self.pisteet[NameIndx][indx] = points[idx][1]
                #print( 'Sinne meni', points[idx][1])

        #print( self.pisteet )

    def mean(self):
        return np.mean(self.pisteet[:, :], axis=1)


    def printIt(self, title):
        avg = self.mean()

        print(title, self.tehtavaNro)
        #for idx,pinnat in enumerate( self.pisteet[0:15,:]):
        #   print(self.nimet[idx], round( avg[idx],2) , pinnat[:])

        for idx, nimi in enumerate( self.nimet ):
            print( nimi, round( avg[idx],2), self.pisteet[idx,:] )


    def printName(self, name, title):
        avg = self.mean()

        summa = 0

        print(title, self.tehtavaNro)
        #for idx,pinnat in enumerate( self.pisteet[0:15,:]):
        #   print(self.nimet[idx], round( avg[idx],2) , pinnat[:])

        for idx, nimi in enumerate( self.nimet ):
            if (name == nimi):
                print( nimi, round( avg[idx],2), self.pisteet[idx,:] )
                summa = summa + round( avg[idx], 2)

        return summa
#
#
#




nimet = ['Ida','Nanda','Rasmus','Jussi','Olivia','Lauri','Emil','eemeli','Aleksandra', 'Arina', 'Alina']
nim=8
kappaleet = [1]



summa = 0;
lkm = 0;

print('Pisteet tahan mennessa. Saa lisailla ja parannella, jos haluaa.')
for i,t in enumerate( kappaleet ):
    #print( t )
    files = glob.glob('t'+ str(t) + '_*.csv')
    #files = glob.glob('t*.csv')
    #print(files)
    g1a = tehtavatPinnat( files.__len__() );


    for idx,fname in enumerate( files ):
        # Get the number:
        i1 = fname.find('_')
        i2 = fname.find('.')
        assignNro =  int( fname[i1+1:i2])
        #print( '   ',fname, ':')
        g1a.add( idx, assignNro, getPoints(fname) )

    
    #g1a.printIt('Kappale ' + str(t)+': tehtavat')
    #print('')
    summa = summa + g1a.printName(nimet[nim], 'Kappale ' + str(t)+': tehtavat')
    lkm = lkm +1
    
    

print( 'KA: ' , round(summa/lkm,2), ' -> ', round(summa/lkm,2)+1 )
quit()
