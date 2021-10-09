# message
```
 fathtpe uTdl, ose-i lda cuoehhninieFrny do axTlyeoees se8 mcwU  hr
opotrucenmvts,nh t rtes  fee gaemUeleictoT y fsF,sr-diw8riorr ioaor
e asens  tsehoccetaq ist  oeiIe t Tmm.i ado.feronceetufs nlnt os bn
piucarieoanreeees ttctsw.nfi  oocab  n reylryo, ueTtm rorhpt hear o
s"eri"t s "taexgostae egn"hoiupe gfi  tuoet  less ttvst seh,dhhlf  a
e tlbraisup eemsbiaevh e d.,ctrosad  nrecdoeeas,ial mfItei  satorp o
 etuiord pboeubadt  uue o kyot  FnrnheUa-deo h8foTtor,   hcvs nlyeah,tia
e aiomoosnssop xtrcsf aguepfluyi gcsn tE euccues astntrsneil .ilute
Thi 8nartes sd  socdamuftsti r- dUor ifteF- flo  aeatshttomteone
roosebi le ingmeie uithrsonpsd rdtshre c iu file.

rendcace oblsi,Ftuinoeo vs lonb lar omnrdy fietmt deTUheTso w-8
 ee ao rcudFi-led,sqneeoo  uclreoo8dncs fnceed el ascyU w cUtesqnecsseT
 cdhneteoF o ofarrhuconpir aU ll tviuTtrc-i 8e ss tnce.

c:oso.6 g 0 n7dcn,Ds,d- 1IS1naO43e2002   tict .aredcivc Ai0o6e
iUtglvi erreFmcentecn  sa dn- e aaTruhhmrme seqetif "eswlna ioe8pl ay
 t iaihosctdr as deaacebieitpuhahseeh stueantrttrt "tte    tpo rtsdand
rsneeaoa i"ht sdtbthtn nat lhichtd heeaetiwr isc coaeaut  r lpbatdsed
ei"iOue sm enmlcuecedeiyvby no cscngd v  . erpoahrp aooat rteh in
mleyfsrrcUeoF - eaeru e8ps  oTi e ac  nemalqdcdn8 eFybTsUdt-oa
h+  h  ce Fn sbvm)olkc(iUhac arrlwFFDt,eoicitak a npniearetleerted
llrbI ik t mbhetnyi oim i,  t osgoarsamdm. oaig tede aurqoas o
Uasd-rat eodcuecyme  l  mini8ng o lfrfeasTFmicq aroseriuvlsuhtly
di Ureti te oue  hbcectus a dcn srcaaehtor nctlerd njoatalainniehtv
v h  0le  goShOntluh6bl yrwetIiu6elea1,-oen4t g1 odnseosfu tf't
ges rdc.tljhoar  s netams Iaifn  i, uetqgnosiemuacnnsea mendyor
oo  o6scbI lO  aaotm,i 1dhacrSrr4cesn0t  nf6eiowallam naultveke
 afeulucd i oefl tgd  ndutc e,issmuadrg acbeoonrgfninion.

scmheea1rlP(,T qceie  rsFhu  el deko ptesnaeeretm 8eUandrshe) cwf-e at
 ey d(ytaaanr e )ael bhtserceclnoeptcrtelrxrnla e2n(e,po me  glscier
o(s ooninu ttqaeehgimadt gn)woaanf3)tieanll  k rva utfqlel,i r an
lcu e yci l -l.ysiUrasti peTdsqpeFece,grdil .le8ae noroper
epzmaneaofcneardr yemcs  ti ttokymlaeaialdi if lnrosemenrhtya
eTE. nysyTs ii,lefnqsaiunfa soe"D hEi l ed" i lo ctn ut'seeNoh  H st
ty ,dh s ss uhhotliecrulodroraemowoehdcfeaa edwyra se , ecoshb  hwebe
cocnanref us roce.

licsii    Ag 7naeullaelh9icpttlylenx s ra e saslrnci  enloft(hrhe te
)aen .lrtnfodif,Iete lhoti tiwe d dsp n"|ti o eel  swdxta ,n "ctehe
ah n e,a1ih.trat.c-oS  bwnd.nn 1 tic loCninA1IpIsc nnoi2l22e.rols
0 lnI0yxddUi+hfeawa0o -hi7 d0t+ y Us i.lif dFphou  nt0itf  aeft0isw,
ecl"s h( dt ae9 |h eosga ccirmhilrhantenigl tlmiu"pnnsl) 7r r ua uo.
 syotate iTdye ole-i sdit uoofhw n kFroy duwtlTsqle hs te8 ,crUuchrhe
vtb yiren suh,ae inlwcatcr   toaseer  nhier mteeeehr rofctcrhach
yee  csqd a eepaeegier lrueesrniebplcadnn ams ltohclraacmmsf cter.

  otttneuvNms r aeftarsnnno  eohtca lqanoei, ta thtuee seol dimaeofed
,sc p fsilh aaentaorerunbodtloepes  staa( ti a ecievteieem ci nsyl n
e)elnroe pptsayib  e tfacuvoomr tl elaidnfeetsaora refdm bon iulrhied
eia lnettts hewye lqmcsar oi recattclse fenwrhogec ytu  aoprhIfa .uin
u eerrec, ee "tore da" synnooohd phlei|g ctlumn.
```
### Microseconds: 17760
# msg
```
This test file can help you examine, how your UTF-8 decoder handles
various types of correct, malformed, or otherwise interesting UTF-8
sequences. This file is not meant to be a conformance test. It does
not prescribe any particular outcome. Therefore, there is no way to
"pass" or "fail" this test file, even though the text does suggest a
preferable decoder behaviour at some places. Its aim is, instead, to
help you think about, and test, the behaviour of your UTF-8 decoder on a
systematic collection of unusual inputs. Experience so far suggests
that most first-time authors of UTF-8 decoders find at least one
serious problem in their decoder using this file.

The test lines below cover boundary conditions, malformed UTF-8
sequences, as well as correctly encoded UTF-8 sequences of Unicode code
points that should never occur in a correct UTF-8 file.

According to ISO 10646-1:2000, sections D.7 and 2.3c, a device
receiving UTF-8 shall interpret a "malformed sequence in the same way
that it interprets a character that is outside the adopted subset" and
"characters that are not within the adopted subset shall be indicated
to the user" by a receiving device. One commonly used approach in
UTF-8 decoders is to replace any malformed UTF-8 sequence by a
replacement character (U+FFFD), which looks a bit like an inverted
question mark, or a similar symbol. It might be a good idea to
visually distinguish a malformed UTF-8 sequence from a correctly
encoded Unicode character that is just not available in the current
font but otherwise fully legal, even though ISO 10646-1 doesn't
mandate this. In any case, just ignoring malformed sequences or
unavailable characters does not conform to ISO 10646, will make
debugging more difficult, and can lead to user confusion.

Please check, whether a malformed UTF-8 sequence is (1) represented at
all, (2) represented by exactly one single replacement character (or
equivalent signal), and (3) the following quotation mark after an
illegal UTF-8 sequence is correctly displayed, i.e. proper
resynchronization takes place immediately after any malformed
sequence. This file says "THE END" in the last line, so if you don't
see that, your decoder crashed somehow before, which should always be
cause for concern.

All lines in this file are exactly 79 characters long (plus the line
feed). In addition, all lines end with "|", except for the two test
lines 2.1.1 and 2.2.1, which contain non-printable ASCII controls
U+0000 and U+007F. If you display this file with a fixed-width font,
these "|" characters should all line up in column 79 (right margin).
This allows you to test quickly, whether your UTF-8 decoder finds the
correct number of characters in every line, that is whether each
malformed sequences is replaced by a single replacement character.

Note that, as an alternative to the notion of malformed sequence used
here, it is also a perfectly acceptable (and in some situations even
preferable) solution to represent each individual byte of a malformed
sequence with a replacement character. If you follow this strategy in
your decoder, then please ignore the "|" column.
```
### Microseconds: 18784

Process finished with exit code 0
