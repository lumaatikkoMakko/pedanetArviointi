#Python3

import csv
import math
import glob
import numpy as np

class tehtavatPinnat:
    nimi = []
    tnimi = []
    maxIndex = 19

    def __init__(self):
        self.nimi = []
        self.tnimi = []
        self.tlyh = []
        self.oLkm =1
        self.tLkm = 1
        self.piste = np.zeros((100,100))
        self.arvo = np.zeros((100,100))

    def find_element_in_list(self, element, list_element):
        try:
            index_element = list_element.index(element)
            return index_element
        except ValueError:
            return -1

    def addTitlesNumbers(self, titles):
        for title in titles[1:]:
            self.tnimi.append(title)

    def addNamePoints(self, row, hlo):
        self.nimi.append( row[0] )
        self.oLkm = self.oLkm+1
        #print( row[0] )
        #print( "nimi", self.nimi )

        for i,p in enumerate( row[1:] ):
            points = p
            if "Ei" not in p:
              #print( p )
              values = [int(i) for i in p.split(',')]
              #print( values );
              self.piste[hlo,i] = max(values)
              self.tLkm = i+1
              #print ( "suurin: ", max( values ) )
        #print( self.piste[hlo,:] )
        self.tLkm = self.tLkm-1

    def setGrade(self, x):
        #Input 0...1, output: 4...10
        #y = (y0-y1)/(x0-x1)(x-x0) + y0
        #y0=10, y1 = 4; x0 = 1; x1 = 0.1
        y = math.ceil( 4*( 6/(1-0.1)*(x-1)+10 ))/4
        if y < 4:
            y=4
        return y

    def setGrade2( self, avg, i):
        arvosana = []
        self.piste[j,i]


    def createGrade(self):
        #
        avg = np.max(self.piste, axis=0 )
        #print( avg )
        for i,a in enumerate(avg):
            if a > 0:
                self.arvo[:,i] = ( np.ceil( 4*( 6/(1-0.1)*( self.piste[:,i]/a -1 ) + 10  ) )/4)
        aa = self.arvo < 4
        self.arvo[aa] = 4

    def tulostaKaikkiTehtavat(self):
        for j,mi in enumerate( self.tnimi ):
            print( self.tnimi[j], end='\n' )


    def tulostaOsaTehtavat(self, tul):
        ind=[]
        for i,tehtava in enumerate( tul ):
            #print( 'AAA' + tehtava )
            for j,mi in enumerate( self.tnimi ):
                #print( '   ' + mi )
                if mi.find( tehtava )>=0:
                    print( self.tnimi[j], end='\n' )
                    ind.append( j )
        #print("BBBB" )
        #print( ind )
        return ind



    def tulostaPisteet(self):
        for i,ni in enumerate(self.nimi):
            print( ni, end='\t' )

            for j,mi in enumerate( self.piste[i,:] ):
               print( mi, end='\t' )
               if j>self.tLkm:
                   break
            print( '', end='\n')


    def tulostaKaikkiArvostelu(self):
        print('Nimi \t Keskiarvo: \t ', end='')
        for j,mi in enumerate( self.arvo[0,:] ):
            print( self.tnimi[j], end='\t' )
            #print( j+1, end='\t' )
            if j>=self.tLkm:
               break
        print('')
        for i,ni in enumerate(self.nimi):
            print( ni, end='\t' )

            #print( ( self.arvo[i,0:self.tLkm] ), end='\t' )
            print( math.ceil( 4*np.mean( self.arvo[i,0:self.tLkm] ))/4, end=':\t' )

            for j,mi in enumerate( self.arvo[i,:] ):
               print( mi, end=' \t ' )
               if j>=self.tLkm:
                   break
            print( '', end='\n')




    def tulostaOsanArvostelu(self, tul, ind):
        #print( ind )
        print('Nimi \t Keskiarvo: \t ', end='')
        for i,ii in enumerate( ind ):
            print( tul[i], end='\t')
        print('')
        for i,ni in enumerate(self.nimi):
            print( ni, end='\t' )
            print( math.ceil( 10*np.mean( self.arvo[i,ind] ))/10, end=':\t' )
            print( self.arvo[i,ind] )


    def tulostaOsanArvosteluNimi(self, tul, ind, nInd):
        print('Nimi \t Keskiarvo: \t ', end='')
        for i,ii in enumerate( ind ):
            print( tul[i], end='\t')
        print('')
        ka=math.ceil( 10*np.mean( self.arvo[nInd,ind] ))/10
        print( '  ' +self.nimi[nInd], end='\t' )
        print( ka, end=':\t' )
        print( self.arvo[nInd,ind] )
        return ka


    def isName(self, name):

        NameIndx = self.find_element_in_list( name, self.nimet )

        if( NameIndx == -1):
            self.nimet.append(name)
            NameIndx = self.nimet.__len__()-1
        #print("NIMET:")
        #print( self.nimet )
        return NameIndx



#
#
#
#
#

fil = []
tul = []
kpl = []

if ( 1 ==0 ):
    kpl.append( 'I: Syksyinen luonto' )
    fil.append( 'ym3_1.csv' )
    tul.append( ['1. Puun termit', 'Tunnista eläimet ', '1. Täydennä','2. Miksi linnut muuttavat', '3. Muuttolintuja', '4. Muuttolintujen ', '1. Nimeä marjat', '2. Milloin ', '3. Marjat ovat', '4. Merkitse väärät', '1. Mitä marjoja ', '2. Mitä viljoja' ] )


    kpl.append( 'II: Kotiseudun kasveja ja eläimiä' )
    fil.append( 'ym3_2.csv' )
    tul.append( ['1. Aukko', '2. Aukko', '3. Kasvin','4. Aukko', '1. Mistä', '2. Kimalaiset', '3. Hyttyset', '4. Kukkak', '5. Täyd', '6. Määritys', '2. Leppä', '3. Perho', '1. Hämä', '2. Lukit', '3. Punkki' ] )

    kpl.append( 'III: Talvi' )
    fil.append( 'ym3_3.csv' )
    tul.append( ['1. Merkitse', '2. Talvi', '1. Lintulaudan lintu','2. Lintu', '3. Tunnista', '4. Tunnista', '1. Oravan', '2. Oravan' ] )



#
#
#


if ( 1 ==0 ):
    kpl.append( 'I: Kesäinen luonto' )
    fil.append( 'ym4_1.csv' )
    tul.append( ['1/Luku1/1. Kesä', '2. Ukkonen', '1. Sää','2. Mistä johtuu', '3. Sateen', '4. Tuulen', '5. Ukkonen', '1. Yötön', '2. Yölaulajat', '3. Eläimiä', '4. Kasvitkin', '1. Oikein', '2. Hyttysen mu', '3. Mitä tauteja','1. Kuinka', '2. Mitkä', '3. Mistä', '4. Täydennä', '1. Järvikalat', '2. Muita kaloja', '3. Kalan osat',  '5. Kalaretki','6. Kalama', '1. Nurmikko', '2. Rastaat', '3. Kasteliero'   ] )


    kpl.append( 'II: Mistä ruokamme tulee?' )
    fil.append( 'ym4_2.csv' )
    tul.append( ['1. Lehmä', '2. Sika', '1. Leipä','2. Vehnä', '3. Ohra', '4. Kaura' ])


if (1==0):
    kpl.append( 'I: Niityt' )
    fil.append( 'ym5_1.csv' )
    tul.append( ['1. Kasvien luokittelu kukan','2. Kasvien luokittelu lehtien ', '3. Kasvien luokittelu koon', '1. Oikein', '2. Nimeä eläin' ] )

    kpl.append( 'II: Puistot' )
    fil.append( 'ym5_2.csv' )
    tul.append( ['1. Väittämiä', '2. Nimeä','2. Puiston', '3. Tunnistus', 'Luku2/1', 'Luku2/2', 'Luku2/3', 'Luku3/2', 'Luku5/1','Luku5/2' ] )

    kpl.append( 'III: Eurooppa' )
    fil.append( 'ym5_3.csv' )
    tul.append( ['1. Koordinaatit', '2. Maanosat ja meret','3. Maanosat', '4. Tunnistatko'  ] )

    kpl.append( 'IV: Ihminen' )
    fil.append( 'ym5_4.csv' )
    tul.append( ['01/1','01/2', '01/3', '1. Perittyä', '2. Ihon osat','3. Kysymyksiä', '5. Urheilulajit', '02/1.',  '03/1.', '03/2.'  ] )

#
#
#
#

if (1==0):
    kpl.append( 'I: Metsät. Puut ovat tuottajia' )
    fil.append( 'ym6_1_1.csv'  )
    tul.append( ['Piirrä puu', 'Mistä energia','1. Oikein', '2. Kerro yht', '3. Määrittele', '4. Ravintok' ] )

    kpl.append( 'I: Metsät. Metsien monia lehtipuita' )
    fil.append( 'ym6_1_3.csv'  )
    tul.append( ['2. Ky', '4.', '6.' ] )

    kpl.append( 'I: Metsät. Jäkäliä, sammalia, sieniä' )
    fil.append( 'ym6_1_5.csv'  )
    tul.append( ['1. Väittämiä', '2. Sammal', '3.', '1. Jäkälä' ] )

    kpl.append( 'I: Metsät. Hyönteiset ja hämähäkit' )
    fil.append( 'ym6_1_6.csv'  )
    tul.append( ['1. Muurahaiset', '2. Hämähäkit', '1. Muurahaisten', '2. Hämähäkin' ] )

    kpl.append( 'II: Materiaalit' )
    fil.append( 'ym6_2.csv'  )
    tul.append( ['2. Täydennä1' ] )

    kpl.append( 'III: Turvallisuus' )
    fil.append( 'ym6_3.csv'  )
    tul.append( ['2/1.','3/1', '1. Avoimia'] )



#
#
#
#
#

if (1):

    kpl.append( '1: Elävä solu ' )
    fil.append( 'bg7_1.csv'  )
    tul.append( ['P1','P2', 'P3', 'P4', 'S5', 'S6','S7'] )

    kpl.append( '4: Levät ja planktoneläimet' )
    fil.append( 'bg7_4.csv'  )
    tul.append( ['P1','P2', 'P3', 'P4', 'S5', 'S6','S7', 'Bakteereista'] )

    kpl.append( '5: Kasvit' )
    fil.append( 'bg7_5.csv' )
    tul.append( ['P1.','P2', 'P3', 'P4', 'P5', 'P6','P7', 'P8', 'P9', 'P10'] )

    kpl.append( '6: Selkärangattomia eläimiä' )
    fil.append( 'bg7_6.csv' )
    tul.append( ['P1.','P2', 'P3', 'P4', 'P5', 'P6','P7'] )

    kpl.append( '7: Kiehtovat kalamme' )
    fil.append( 'bg7_7.csv' )
    tul.append( ['P1.','P2', 'P3', 'P4', 'S5', 'S6','S7'] )

#
#
#
#

if (0):
    kpl.append( '2: Karttatietoutta' )
    fil.append( 'ge7_2.csv'  )
    tul.append( ['P1','P2', 'P3', 'S4', 'S5', 'S6'] )

    kpl.append( '5: Valtameret erottavat mantereita' )
    fil.append( 'ge7_5.csv'  )
    tul.append( ['P1','P2', 'P3', 'S5', 'S6' ,'S7'] )

    kpl.append( '6: Levoton maankuori' )
    fil.append( 'ge7_6.csv'  )
    tul.append( ['P1.','P2', 'P3', 'P5', 'P6' ,'P7', 'P8', 'P9', 'P10', 'P11', 'S14'] )

    kpl.append( '7: Vuoristot ovat syntyneet' )
    fil.append( 'ge7_7.csv'  )
    tul.append( ['P4.','P5', 'S6' ,'S7', 'S8'] )

    kpl.append( '8: Miten vesi, jää ja tuuli kuluttuvat' )
    fil.append( 'ge7_8.csv'  )
    tul.append( ['P1.','P2', 'P3' ,'P4', 'P5'] )

    kpl.append( 'Väliarviointi' )
    fil.append( 'ge7_its.csv'  )
    tul.append( ['Luvut'] )

#
#

if ( 0):
    kpl.append( '4: Väestönkasvu' )
    fil.append( 'ge8_4.csv'  )
    tul.append( ['P1.','P2', 'P3' ,'P4', 'P5', 'P6'] )

    kpl.append( '5: Ihmiset muuttavat' )
    fil.append( 'ge8_5.csv'  )
    tul.append( ['P1.','P2', 'P3' ,'S5', 'S7'] )

    kpl.append( '6: Kaupungistuminen' )
    fil.append( 'ge8_6.csv'  )
    tul.append( ['P1.','P2', 'P3' ,'S4', 'S6'] )

    kpl.append( '7: Ravinnontuotanto' )
    fil.append( 'ge8_7.csv'  )
    tul.append( ['P1.','P2', 'P3' ,'P4', 'P5' ] )

    kpl.append( '8: Luonnonvarat' )
    fil.append( 'ge8_8.csv'  )
    tul.append( ['P1.','P2', 'P3' ,'S4' ] )


#
#
#

if (0):
    kpl.append( '1: Miten soluja tutkitaan' )
    fil.append( 'bg9_1.csv'  )
    tul.append( ['P1.','P2' ] )

    kpl.append( '2: Solut' )
    fil.append( 'bg9_2.csv'  )
    tul.append( ['P1.','P2', 'S3' ] )

    kpl.append( '3: Kudokset' )
    fil.append( 'bg9_3.csv'  )
    tul.append( ['P1.','P2', 'S3' ] )

    kpl.append( '4: Luusto' )
    fil.append( 'bg9_4.csv'  )
    tul.append( ['P1.','P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8'] )

    kpl.append( '5: Lihakset' )
    fil.append( 'bg9_5.csv'  )
    tul.append( ['P1.', 'P3', 'P4', 'P5', 'P6', 'S7', 'P8'] )

    kpl.append( '6: Ruuansulatus' )
    fil.append( 'bg9_6.csv'  )
    tul.append( ['P1.','P2', 'P3', 'P4', 'P5', 'P6', 'S7'] )

    kpl.append( '7: Hengitys' )
    fil.append( 'bg9_7.csv'  )
    tul.append( ['P1.', 'P2', 'P3', 'S4', 'S6'] )

    kpl.append( '8: Veri' )
    fil.append( 'bg9_8.csv'  )
    tul.append( ['P3.', 'P4', 'P5', 'S6'] )

    kpl.append( '9: Sydän ja verenkierto')
    fil.append( 'bg9_9.csv'  )
    tul.append( ['P1.', 'P3', 'P5', 'P6', 'P7', 'S8', 'S9' ] )

    kpl.append( '10: Maksa ja munuaiset')
    fil.append( 'bg9_10.csv'  )
    tul.append( ['P2.', 'P3', 'P4', 'P5', 'S6' ] )

    kpl.append( '11: Umpirauhaset')
    fil.append( 'bg9_11.csv'  )
    tul.append( ['P1.', 'P2', 'P3', 'S5' ] )


#
#
#

#
#
#
ka = 0
lkm = 0

print('Hei')
print('Mantsan tehtäväsi tähän mennessä. Lopussa arvosana seisoo.')
print('Tarkista ainakin, että olet tehnyt ne mitkä olen merkinnyt arvosanalla neljä (4).')
print('Jos olet tehnyt, mútta arvosana on 4, kerro minulle. ')
print('Saat parannella ja lisäillä, jos haluat.')
print('Muista, että nyt ei ollut koetta, joten aika lailla tämän mukaan annan arvosanan.')
for i, tcsv in enumerate( fil ):
    lkm = lkm + 1
    pinnat = tehtavatPinnat()
    with open( tcsv ) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        #Lue tehtavien nimet
        pinnat.addTitlesNumbers( next( readCSV ) )

        hloid = 0
        for row in readCSV:
            pinnat.addNamePoints( row, hloid )
            hloid=hloid+1

    print('-------------')
    print( kpl[i] )
    print('Tehtävät')
    #pinnat.tulostaPisteet( )
    pinnat.createGrade()
    #pinnat.tulostaKaikkiTehtavat()

    ind = pinnat.tulostaOsaTehtavat(tul[i])
    #print( ind )

    #pinnat.tulostaOsanArvostelu( tul[i], ind )
    ka = ka + pinnat.tulostaOsanArvosteluNimi( tul[i], ind,8)


print('---------------')
print( 'Kaikkien tehtävien keskiarvo: ', math.ceil( ka/lkm*10)/10 )

