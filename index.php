<!DOCTYPE html>
<html lang="fi">
<head>


  <!-- Basic Page Needs
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta charset="utf-8">
  <title>@MarkkuOpe</title>
  <meta name="description" content="">
  <meta name="author" content="@MarkkuOpe">

  <!-- Mobile Specific Metas
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <!-- FONT
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link href="//fonts.googleapis.com/css?family=Raleway:400,300,600" rel="stylesheet" type="text/css">

  <!-- CSS
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
<!--  <link rel="stylesheet" href="css/normalize.css"> -->
  <link rel="stylesheet" href="css/skeleton.css">
<!--  <link rel="stylesheet" href="css/custom.css"> -->

  <script src="js/jquery.min.js"></script>



<link rel="stylesheet" href="css/default.css">
<script src="js/highlight.pack.js"></script>
<script>hljs.initHighlightingOnLoad();</script>



  <!-- Favicon
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <link rel="icon" type="image/png" href="images/favicon.png">



<style>

.buttons {

}

.targetDiv{
  display:none;
}

</style>


</head>
<body>



  <!-- Primary Page Layout
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->
  <div class="container">


<div class="row">

<div class="twelve columns">


<h1>Peda.net-kirjan arvioinnin yksinkertaistaminen</h1>


<div class="docs-section" id="yleista">
<p>
Eopin pedanet-kirjan oppilaiden tekemien tehtävien arviointi ja yhteenveto on hieman hankalaa. Tässä (lyhyet) ohjeet, kuinka homman sain tehtyä.


</p>

<p>Viimeisestä kohdasta &mdash; yhteenveto &mdash; löytyy valmis ja toimiva Python-skripti. Aiemmat pykälät ovat johdantoa ja skriptin rakentamista. </p>

<p>Kommentteja ja vinkkejä ja virheistä voi kertoa tai kysyä vaikkapa twitteristä @MarkkuOpe. </p>

</div>



<div class="buttons"> <a  class="showSingle" target="1">Ongelma ja korjausehdotus</a> </div>
<div id="div1" class="targetDiv">
<div class="row">
 <div class="twelve columns">
<p>Pedanetin eopin kirjojen tehtävissä on pari pientä ongelmaa, jotka voitaisiin korjata melko yksinkertaisesti. Tässä esitetään Pythonilla tehty kilke, joka helpottaa elämää. Osassa tehtävissä on tietokoneen tekemä automaattikorjaus, mutta nekin opettaja voi korjata jälkikäteen esim. kirjoitusvirheiden takia.</p>
</p>
<div class="row">
 <div class="seven columns">

<p>Kuitenkin, ongelmia on</p>
<ul>
<li>Arvosanan antamisessa. Kone tarkistaa osan, muttei anna arvosanaa, vain pisteet. Pisteet pitäisi muuttaa arvosanaksi katsomalla erillisestä taulukosta, esimerkiksi <a href="http://opinnot.net/yleiset/arvosana.php">arvosanalaskurista</a>. Pisteyttäminen Peda.netissä on helppoa, mutta pisteet täytyy kirjata arvosana-kohtaan.</li>
<li>Yhteenveto tehdyistä tehtävistä, mutta lukuvuonna 18&mdash;19 kirjoihin on tullut osiin tehtävistä hyvä yhteenvetotaulukko, mutta ne on vain kotitehtävistä. Kehitys kehittyy.</li>

<li>Oppilaiden saama yleisarvosana tehtävistä puuttuu kokonaan.</li>

</ul>

</div>
 <div class="five columns">

<p>Kuva: Nykytilanne.</p>
<a href="img/peda3.png"><img class="u-full-width" src="img/peda3.png"></img></a>

</div>
</div>


<div class="row">
 <div class="seven columns">

<p>Ratkaisuehdotus on hyvin yksinkertainen:
</p>
<ul>
<li>Opettaja saa valita, mitkä tehtävät arvioidaan, ja oppilaat näkevät ne.</li>
<li>Pedanetin oppikirja muuttaa pisteet suoraan arvosanaksi, ja näyttää ne sekä opettajalle että oppilaalle.</li>
<li>Oppilaat (ja opettaja) näkevät yhteenvedon arvosanastansa, ja tiedon jos joku tehtävä on vielä tekemättä.
</li>
</ul>

</div>
 <div class="five columns">

<p>Kuva: Ehdotus</p>
<a href="img/peda_ehdotus.png"><img class="u-full-width" src="img/peda_ehdotus.png"></img></a>

</div>
</div>

<div class="row">

<div class="twelve columns">
<p>Tätä ongelmaa korjaamaan väsäsin Python-skriptin, jolla on sama toiminnallisuus, mutta käytettävyys paljon huonompi.</p>


</div>

</div>

 </div>
</div>
</div>









<div class="buttons"> <a  class="showSingle" target="2">Pedanetistä CSV:ksi</a> </div>
<div id="div2" class="targetDiv">
<div class="row">

 
 <div class="six columns">

<p>Tehtävätaulukko löytyy kirjan kohdasta:</p>
<p>Tehtävät &#8594; Näytä arvioinnit &#8594; Yhteenveto.</p>
<a href="img/peda123.png"><img src="img/peda123.png" class="u-full-width"></a>
</div>
 <div class="six columns">

<p>Taulukon voi kopioida valitsemalla (maalaamalla) se ja liittämällä taulukkolaskentaohjelmaan. Tehtävien otsikossa on mainittu luvun numero (L02), tehtävätyyppi (P, S jne ) sekä tehtävän nimi ('Nimeä eläinsolun osat'). Oppilas saa vastata tehtäviin useamman kuin yhden kerran, eli pisteitä voi olla useampi samassa solussa. Tehtävät ovat listassa epämääräisessä järjestyksessä.
</p>
<a href="img/taulukkolaskenta1.png"><img src="img/taulukkolaskenta1.png" class="u-full-width"></a>
<p>Useissa taulukkolaskentaohjelmistoissa csv:ksi tallennetaan tallettamalla ja valitsemalla tiedostomuodoksi csv. Joitain valintoja voinee tehdä.
</p>

<a href="img/export_csv.png"><img src="img/export_csv.png" class="u-full-width"></a>


<p>
Ikävä kyllä, jokaisen kappaleen tehtävät täytyy muutta csv:ksi erikseen, koska pedanetin rakenne ei kykene tuottamaan kaikkea kerralla. 
</p>

 </div>
</div>
</div>

 
 

<div class="buttons"> <a  class="showSingle" target="3">Lue CSV Pythonilla</a> </div>
<div id="div3" class="targetDiv">
<div class="row">

 <div class="six columns">
<pre><code class="python">import csv
readCSV = csv.reader(csvfile, delimiter=',')

</code>
</pre>
<p>Luetaan monta tiedostoa kerralla:</p>




<pre><code class="python">import csv

fil = []
fil.append( 'lk8_1.csv'  )
fil.append( 'lk8_3.csv'  )
fil.append( 'lk8_4.csv'  )
fil.append( 'lk8_5.csv'  )
fil.append( 'lk8_6.csv'  )
fil.append( 'lk8_8.csv'  )

for i, tcsv in enumerate( fil ):
    pinnat = tehtavatPinnat()
    with open( tcsv ) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        #Lue tehtavien nimet
        pinnat.addTitlesNumbers( next( readCSV ) )
        hloid = 0
        for row in readCSV:
            pinnat.addNamePoints( row, hloid )
            hloid=hloid+1


</code></pre>

<p>Pedanetin listauksessa oppilaat ovat aina samassa järjestyksessä, joten sama vaakarivi on aina sama oppilas. Helppoa ja kätevää. Olioon talletetaan oppilaan nimi, tehtävän nimi, pisteet ja kaikkea muuta oleellista. </p>


 </div>

 <div class="six columns">
<p>Pythonin csv-paketilla on helppo lukea csv-muotoista dataa.</p>

<p>Usean tiedoston lukeminen kerralla onnistuu myös. Muodostetaan <code>fil</code>-niminen taulukko, johon talletetaan luettavien tiedostojen nimet.


</p>

<p>
Tietojen käsittelyä varten luodaan luokka <code>tehtavatPinnat</code>, joka mm. lisää muodostettavaan olioon tehtävien nimet <code>next</code>-käskyllä. <code>addNamePoints</code> lisää jokaisen oppilaan nimitiedot ja tehtävistä saadut pisteet.
</p>


<pre><code>import numpy as np

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
              values = [int(i) for i in p.split(',')]
              self.piste[hlo,i] = max(values)
              self.tLkm = i+1
              #print ( "suurin: ", max( values ) )
        #print( self.piste[hlo,:] )
        self.tLkm = self.tLkm-1
</pre></code>

<p>Metodin initialisoinnissa varataan <em>riittävän</em> iso <code>numpy</code>-taulukko, koska sen käyttäminen on helppoa. </p>

 </div>


</div>
</div>


<div class="buttons"> <a  class="showSingle" target="4">Anna arvosana pythonilla</a> </div>
<div id="div4" class="targetDiv">
<div class="row">

<div class="six columns">
<p>Haetaan kunkin tehtävän suurin annettu pistemäärä. Se on maksimi, eli <code>np.max()</code>. Sovitetaan simppeli suora maksimin ja nollan välille:
</p>
<img class="u-full-width" src="img/pisteetNumeroksi.svg"><img>

<p>
Lisäksi siinä on neljänneksen pyöristys, eli funktio antaa arvoja 10, 9,75, 9,5, 9,25 jne.

</p>


 </div>
<div class="six columns">


Lisätään luokkaan <code>class tehtavatPinnat:</code> metodi <code>createGrade</code>:
<pre><code class="python"> def createGrade(self):
   #
   avg = np.max(self.piste, axis=0 )
   #print( avg )
     for i,a in enumerate(avg):
       if a > 0:
          self.arvo[:,i] = ( np.ceil( 4*( 6/a*( self.piste[:,i] -a ) + 10  ) )/4)
</code></pre>
</div>

</div>
</div>



<div class="buttons"> <a  class="showSingle" target="5">Laske keskiarvot ja tulosta</a> </div>
<div id="div5" class="targetDiv">
<div class="row">
 <div class="six columns">
<p>
</p>
<p>
</p>

<pre><code class="python">
fil = []
tul = []
kpl = []


kpl.append( '1: Näe metsä puilta ' )
fil.append( 'lk8_1.csv'  )
tul.append( ['P1','P2'] )

kpl.append( '3: Suomen metsätyypit ' )
fil.append( 'lk8_3.csv'  )
tul.append( ['P1','P2', 'P3', 'P5', 'P6', 'puiston', 'metsien'] )

kpl.append( '4: Sienet luovat metsän perustan ' )
fil.append( 'lk8_4.csv'  )
tul.append( ['P1','P2' ,'P3', 'S4', 'S5', 'P7', 'P8'] )

kpl.append( '5: Kasvien rakenne ja merkitys' )
fil.append( 'lk8_5.csv'  )
tul.append( ['P1','P2' ,'P3', 'P4', 'P5', 'P6', 'P7', 'S8', 'S9'] )

kpl.append( '6: Metsien kasveja' )
fil.append( 'lk8_6.csv'  )
tul.append( ['P1','P2' ,'P3', 'P4', 'P5', 'P6'] )


kpl.append( '8: Metsän selkärankaiset' )
fil.append( 'lk8_8.csv'  )
tul.append( ['P1','P2' ,'P3', 'nisäkkäät', 'lajit'] )
</code></pre>
<pre><code class="python">
    print('-------------')
    print( kpl[i] )
    print('Tehtävät')
    #pinnat.tulostaPisteet( )
    pinnat.createGrade()
    #pinnat.tulostaKaikkiTehtavat()

    ind = pinnat.tulostaOsaTehtavat(tul[i])
    #print( ind )

    #pinnat.tulostaOsanArvostelu( tul[i], ind )
    ka = ka + pinnat.tulostaOsanArvosteluNimi( tul[i], ind,13)
</code></pre>

</div>
 <div class="six columns">


<pre><code class="python">
    def tulostaPisteet(self):
        for i,ni in enumerate(self.nimi):
            print( ni, end='\t' )

            for j,mi in enumerate( self.piste[i,:] ):
               print( mi, end='\t' )
               if j>self.tLkm:
                   break
            print( '', end='\n')
</code></pre>

<p>
</p>

<pre><code class="python">
    def tulostaOsaTehtavat(self, tul):
        ind=[]
        for i,tehtava in enumerate( tul ):
            for j,mi in enumerate( self.tnimi ):
                if mi.find( tehtava )>0:
                    print( self.tnimi[j], end='\n' )
                    ind.append( j )
        return ind
</code></pre>



<pre><code class="python">
    def tulostaOsanArvosteluNimi(self, tul, ind, nInd):
        print('Nimi \t Keskiarvo: \t ', end='')
        for i,ii in enumerate( ind ):
            print( tul[i], end='\t')
        print('')
        ka =math.ceil( 10*np.mean( self.arvo[nInd,ind] ))/10
        print( '  ' +self.nimi[nInd], end='\t' )
        print( ka, end=':\t' )
        print( self.arvo[nInd,ind] )
        return ka
</code></pre>
<p>
</p>

</div>

 </div>
</div>
</div>






<div class="buttons"> <a  class="showSingle" target="8">Koko koodi</a> </div>
<div id="div8" class="targetDiv">
<div class="row">
 <div class="twelve columns">
<p>Tässä on skripti ja ohjeet. Kopioi yhteenvetotaulukko (kts oheinen kuva) taulukkolaskentaan, tallenna CSV-muodossa ja aja oheinen skripti.</p>

<a href="img/peda123.png"><img src="img/peda123.png" class="u-full-width"></a>

<p>Koodi löytyy Githubista &mdash; aina uusin ja toimivin versio. Luultavasti virheitä löytyy.</p>



 </div>
</div>
</div>




<script>

$(document).ready(function(){

    jQuery(function(){
        jQuery('.showSingle').click(function(){
            jQuery('.targetDiv').hide(100);
            jQuery('#div'+$(this).attr('target')).show(200);
        });
    });

});
</script>











<!-- End Document
  –––––––––––––––––––––––––––––––––––––––––––––––––– -->

</div> <!-- columns -->

</div> <!-- row -->

</div> <!-- container -->

</body>
</html>
