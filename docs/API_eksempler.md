API-eksempler
=============

Eksempler på andre APIer for vanntemperatur og vær.

## Yr.no

Yr har åpne APIer for å hente ut værvarsel på forskjellige lokasjoner:
https://hjelp.yr.no/hc/no/articles/360009342833

F.eks. https://www.yr.no/stad/Norge/Oslo/Oslo/Hoved%C3%B8ya/varsel.xml

Tjenesten svarer med XML som inneholder bl.a. lokasjon, tidsrom og
temperaturer:

```xml
<weatherdata>
  <location>
    <name>Hovedøya</name>
    <type>Øy i sjø</type>
    <country>Noreg</country>
    <timezone id="Europe/Oslo" utcoffsetMinutes="120"/>
    <location altitude="33" latitude="59.8946844242147" longitude="10.7376118657979" geobase="ssr" geobaseid="73946"/>
  </location>
  <!-- ... -->
  <forecast>
    <tabular>
      <time from="2019-04-16T08:00:00" to="2019-04-16T12:00:00" period="1">
        <symbol number="1" numberEx="1" name="Klårvêr" var="01d"/>
        <precipitation value="0"/>
        <windDirection deg="54.6" code="NE" name="Nordaust"/>
        <windSpeed mps="2.9" name="Svak vind"/>
        <temperature unit="celsius" value="4"/>
        <pressure unit="hPa" value="1034.7"/>
      </time>
    </tabular>
  </forecast>
</weatherdata>
```

## Badetemperatur Oslo - gammelt API

Bymiljøetaten hadde tidligere et API for å hente ut badetemperaturer
som var rapportert inn av entreprenørene via en WAP-løsningen:
http://oslokommune.msolution.no/friluft/badetemperaturer.jsp

Denne tjenesten er nå ikke lenger i drift. Tjenesten leverte XML som
inneholdt bl.a. sted (navn, id og koordinater), dato og vanntemperatur:

```xml
<badetemp xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#" xml:lang="en">
  <place id="701">
    <name>
      <![CDATA[ Badedammen ved Grorud ]]>
    </name>
    <link>
      http://www.bymiljoetaten.oslo.kommune.no/article208284.html
    </link>
    <geo:lat>59.975274</geo:lat>
    <geo:long>10.885098</geo:long>
    <temp_vann/>
    <updated/>
  </place>
</badetemp>
```

## Badetemperatur Oslo - delt regnark

Som erstatning for den gamle WAP-løsningen så har Webforvaltningen nå
satt opp et delt Google-regnark hvor entreprenørene manuelt fyller ut
badetemperaturer. Dette inneholder sted (id og navn), dato og
vanntemperatur:

```
Artikkel-ID   Badeplass                 Temperatur   Måledato
8268          Badedammen på Grorud    
8269          Bekkensten                16           30.08.2018
8270          Bestemorstranda           16           30.08.2018
8271          Bogstadvannet   
8265          Brekkedammen ved Frysja   15           30.08.2018
8321          Bygdøy sjøbad   
8374          Fiskevollbukta    
8172          Gressholmen   
8322          Grinidammen               15           30.08.2018
8171          Hovedøya    
8264          Huk                       16           30.08.2018
```

## Badetemperatur Bergen

Bergen kommune har laget et API for å hente ut badetemperaturer for AdO
Arena: https://adoapi.azurewebsites.net/swagger/index.html

Tjenesten svarer med JSON som inneholder lokasjon, navn, tidspunkt og
vanntemperatur:

```json
{
  "values": [
    {
      "location": "Nordnes_Sjobad",
      "name": "Temp_Barnebasseng",
      "value": 23.299999237060547,
      "measureTime": "2019-04-15T11:52:06.329Z",
      "unit": "null"
    }
  ],
  "message": "..."
}
```

## NVE målestasjoner for vanntemperatur

NVE har en nettside med sanntids-vanntemperaturer fra målestasjoner i
forskjellige vassdrag o.l.: http://www2.nve.no/h/hd/plotreal/WT/list.html

Data er tilgjengelig som CSV som inneholder tidspunkt og vanntemperatur:

```csv
Tid;Vanntemperatur(<B0>C)
"72.77.0.1003.1  Fl<E5>m bru  Fra:null Til:null  COMPLETE  Knekkpunkt-verdier  Enhet:<B0>C"
2019-02-15 12:00;     2,305
2019-02-16 12:00;     2,823
2019-02-17 12:00;     2,594
2019-02-18 12:00;     2,967
2019-02-19 12:00;     3,078
2019-02-20 12:00;     2,470
2019-02-21 12:00;     2,157
2019-02-22 12:00;     2,767
```

I tillegg finnes det på nettsiden til hver målestasjon mer informasjon
om plassering osv., f.eks. http://www2.nve.no/h/hd/plotreal/WT/0072.00077.000/index.html

```
Stasjon:                                         Plassering:
Stasjonsnavn          : Flåm bru                 UTM-sone  : 32
Stasjonens h.o.h      : 27.0                     UTM-øst   : 397897
Kartblad (N50-serien) : -1000000-IV                  UTM-nord  : 6746086
                                                 Lengdegrad:  7.12165
                                                 Breddegrad: 60.83693
Nedbørfelt:
Nedbørfeltareal       : 263km²                   Fylke     : Sogn og Fjordane
Sjøprosent            : 4.2                      Kommune   : Aurland
```
