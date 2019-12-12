#!/usr/bin/env python3

import re

regex = r"(?:\b(?:W(?:P:(?:[!%~]|N(?:O(?:T(?:C(?:O(?:MPULSORY|OKBOOK|URT)|A(?:TALOG(?:UE)?|SE)|RYSTA(?:LBAL)?L|(?:ENSORE|S)D|HANGELOG|LICKBAIT|V)|P(?:R(?:O(?:MO(?:TION)?|PAGANDA)|ESSRELEASE)|A(?:PERS?|RT)|UBLICFIGURE|L(?:OT|UG)|ERFECT|OINTy)|S(?:T(?:AT(?:S(?:BOOK)?|UTE)|ORAGE|UPID)|O(?:CIAL(?:NETWORK|MEDIA)?|APBOX)|PECULATION|CANDAL)|B(?:UR(?:EAU(?:CRACY)?|O)|ATTLE(?:GROUND)?|RO(?:CHURE|KEN)|IBLIOGRAPHY|LOG)|D(?:I(?:R(?:ECTORY)?|ARY|C)|A(?:TINGSERVICE|B)|EM(?:OCRACY)?|UPE?)|R(?:E(?:(?:LIABL|CIP|SUM)E|POSITORY|QUIRED)|ADIOGUIDE|UMOR|S)|F(?:A(?:CTIONS|NSITE|Q)|I(?:SHING|LM)|REESPEECH|UTURE|ORUM)|G(?:E(?:NEALOGY|TTINGIT)|A(?:MEHOST|LLERY)|OSSIP|UIDE)|A(?:D(?:V(?:ERTISING|OCACY|ICE)|IARY)|NARCHY|MB)|T(?:E(?:MPORARY|XTBOOK)|VGUIDE|RAVEL)|E(?:S(?:SAY|AL)|VERYTHING|WORTHY)?|M(?:A(?:DEUP|NUAL)|EMORIAL|IRROR)|W(?:H(?:OSWHO|ITE)|EBHOST|IKIA)|L(?:INK(?:FARM)?|A[BW]|YRICS)|O(?:BITUARY|NLYFREE|PINION)|#DIC(?:T(?:IONARY)?|DEF)|NE(?:WS(?:PAPER)?|O)|V(?:AND(?:ALISM)?)?|J(?:OURNAL|ARGON)|HO(?:STING|WTO)|(?:IMAG|QUOT)E|YELLOW|3RR)?|N(?:S(?:TANDARDCLASS|ENSE)|ENG(?:PLAG|EL)?|DEF(?:INING)?|PROFIT|LATIN|FREE)|C(?:HINESEITALICS|ON(?:SENSUS)?|ITE)|(?:H(?:IDDENAD|OAXE)|DISCLAIMER)S|P(?:R(?:IMARY)?|A(?:GE|Y)|UNISH)|A(?:(?:BSTRAC|T)T|RTICLE)|(?:-PREEMP|FULLTEX)T|I(?:NDICSCRIPT|CONS)|S(?:ALESMEN|HARING)|V(?:ELPLOT|STY)|B(?:IGDEAL|AN)|E(?:MOJI|NG)|LY(?:MPICS)?|R(?:ESVAND)?|QUORUM|YEAR|OB|UN)|C(?:-(?:C(?:H(?:INA|N)|OLONS?|N)|S(?:HIPS?|LASH|oJ)|B(?:[CK]|ASE)|T(?:IBET|V)|PLSTATIONS|ELECT|GAL|KO|ZH)|A(?:(?:RME(?:NIA)?)?N|IR(?:CRAFT)?|(?:ST|C)RO|U(?:RD|ST))?|P(?:L(?:ACE(?:DAB)?|URAL)|HILIPPINE|ARTY|DAB|EER|P)?|C(?:O(?:MICS|RP)|A(?:PS|T)|/THE|DAB|HEM|ST?|PT|L)|L(?:(?:O(?:WERCASEFIR|NGLI)|I)ST|ANG|DS|L)?|M(?:A(?:NU(?:SCRIPT)?|C)|USIC|DAB|ED|ON)?|F(?:A(?:LKLAND|UNA)?|I(?:LMS?|A)|LORA)?|R(?:I(?:C(?:K(?:ET)?)?|ME)|A?N|OY)|B(?:[CK]|RITPEER|OOKS|ASE|IO)?|G(?:A(?:MES(?:DAB)?|L)|REEK|N)|H(?:E(?:BREW|M)?|ASHTAG|URCH)|S(?:P(?:LITLIST)?|HIP |AL|T)?|U(?:RL(?:ING)?|KSTATIONS|E)|E(?:T(?:/A)?|VENTS|LECT)?|O(?:LLATH|NCERT|PERA|RP)?|D(?:A(?:TES|B)|URATION)|I(?:N(?:D(?:IC)?)?|H)|T(?:V(?:U[KS])?|HE|R)|N(?:[TZ]|U?M|OB)|KO(?:REAN)?|YC(?:LING)?|(cultivar)|VG(?:DAB)?|W[BCS]|(WS)|:TV)|A(?:M(?:E(?:(?:LIS|SOR)T|CHANGES)|INGCRITERIA|B)|ST(?:ALIQ|CRIT|HELP|RO)|T(?:URAL(?:NES|DI)S|H)|V(?:NOREDIRECT|BOX)|C(?:ADEMIC|TOR|D)|RROWCAT|LBUMS?|FL|D)|F(?:[FP]|C(?:[IP]|#(?:UU(?:LP|I)|CS)|C(?:EG?|P))?|O(?:OT(?:BALL|Y)|E)?|(?:SOURCE|LIST)S|E(?:XMP|AT)|T(?:ABLE)?|(?:UR)?G|RINGE|ILM)?|E(?:W(?:S(?:(?:BLO|OR)G|T(?:ART|UB)|EVENT)|MESSAGE|BIES)|(?:GATIVESPI|QUESTRIA)N|VE(?:RUNBLOCK|NTS )|UTRAL|XIST|O)|P(?:[FSV]|O(?:V(?:(?:TITL|NAM)E|(?:VIE|HO)W|FACT)?|SSIBLE|L)|A(?:#WHATIS)?|RO(?:DUCT|F)|LT)|B(?:A(?:S(?:KETBALL|E)|D(?:MINTON)?)|O(?:X(?:ING)?|OK)|UILD(?:ING)?|IO|Z)?|S(?:PORT(?:S(?:EVENT)?)?|(?:INGL|KAT)E|O(?:CCER|NG)|EASONS|CHOOL|UMO|10|4)|G(?:EO(?:G(?:RAPHY)?)?|YMNAST(?:ICS)?|O(?:LF)?|RIDIRON|AELIC|S)|H(?:O(?:RSERACING|CKEY|OPS|AX)|S(?:PHSATH|CHOOL))|M(?:O(?:TORSPORT|DEL)|E(?:DIA)?|USIC|MA|G)?|T(?:R(?:IATHLON|ACK)|E(?:NNIS|AM|MP)|OUR|V)|R(?:IVALRY|ODEO|VE?|U)|V(?:IDEOGAMES|G)|L(?:ISTITEM|S)|D(?:[AT]|ESC)|U(?:MBER|SC)|W(?:FCTM|EB)|N(?:EWS|C)?|ICKNAME|KICK|(E)|/CA)?|C(?:[1G]|O(?:N(?:T(?:E(?:NT(?:FORK(?:ING)?|DISPUTE)|XT(?:MATTERS|BOT)|STED)|INUEDCOVERAGE|N)|DU(?:CT(?:TOBANNED|DISPUTE)|NBLOCK)|A(?:CHIEVE|DMIN)|L(?:IMITED|EVEL)|(?:EXCEP|FLIC)T|C(?:EPTDAB|ISE)|(?:SORT)?S)?|I(?:(?:A(?:TTRIBUT|DVIC)|RESPONS)E|C(?:O(?:PYRIGHT|IN)|AMPAIGN)|P(?:AYDISCLOSE|OLITICAL)| is not simply bias|DISCLOSEPAY|NOTBIAS|LEGAL|EDIT|SELF|TALK|BLP|U)?|M(?:P(?:OS(?:ITIONDAB|ER)|U(?:LSORY|NITS)|ANY |NOW)|M(?:ON(?:MATH|NAME)|ADIS)|ICS?PLOT)|P(?:Y(?:LINKS?|OTHERS|WITHIN|VIOEL|EXP)|S(?:EP)?|DEF|#N|/S)?|O(?:RDINATES|LDOWN)|RP(?:DEPTH|NAME)?|VER(?:AGE|T)|SMETICBOT|LLATERAL|UNCIL/G|GNOMEN|WORKER)|MOS(?:#(?:S(?:TRUCTURE(?:-(?:(?:FICTIONALOBJ|SECTIONTITLE|CHARACTER|TEAM)S|PUBLICATION))?|PECIFIC|OURCES)|L(?:S(?:(?:PLI|OR)T|ECTION)|ISTS|NAME|F)|(?:C(?:IT(?:ESTYL)?|ATNAM|O)|BOXIMAG)E|P(?:RECISE|LOT|OP)|I(?:NFOBOX|SH)|N(?:ESTED|AME)|T(?:ITLES|EAM)))?|A(?:T(?:/(?:EGRS|GRS |R)|DEF(?:INING)?|G(?:ENDER|RS)|EG(?:ORY|RS)|V(?:ER)?|#[TV]|NAME)?|N(?:P(?:O[LP]|LACE|RIVY)|ST(?:ATION|YLE)|DIDATECAT|FRENCH|TFIX|CAN|VAS)?|P(?:CONTEXT|LENGTH|FRAG|TION|WORD)?|S(?:TLIST|CADE)|(?:UTIOU|E)S|MPAIGN|REFUL|LC)|H(?:A(?:RT(?:MATH|TRAJ)?|LLENGE|NGESC|IN|OS)|E(?:CKAFTERCREATE|M(?:NAME|MOS))|INESE(?:CHARACTERS)?|O(?:KING|ICE)|RONO|UG)|I(?:TE(?:S(?:HORT|TYLE|PAM)|(?:BUNDL|TYP)E|CONSENSUS|FOOT|HOW|MED|VAR|WEB)?|RC(?:ULAR)?|V(?:IL)?)|R(?:EAT(?:EU(?:SER(?:#SUB|BOX)|BX)|IVE)|I(?:M(?:INAL|E)?|TERIA)|YSTA(?:LBAL)?L|OSS-POST|D)|U(?:(?:LTIVA|RATO)R|(?:EM)?OS|STOMSIG|BL)|L(?:IC(?:KHER|H)E|EANSTART|AIM|NT?|UB)|rown(?: copy(?:right)?|copy)|S(?:[CK]|D(?:#F1)?)?|B(?:A(?:LL|N)|LANK)|V(?:TOOLS|AN|UT)|YC(?:LING)?/N|ENSOR(?:ED)?|F(?:ORK|RD)|C(?:SD|C)|TDAPE|DB|WW)|S(?:I(?:G(?:#(?:N(?:[LT]|o(?:Templates|n-Latin|CAT))|CustomSig|[DE]L)|L(?:EN(?:GTH)?|INK)|N(?:(?:ATU|HE)RE)?|FO(?:RGE|NT)|IMAGE|PROB|APP|COV|HOW)?|NG(?:LE(?:N(?:ETWORK|AME)|VENDOR|EVENT)|ER(?:DAB)?|ULAR)|(?:DEB|MIL)AR|A(?:NOTDAB)?|S(?:TER|P)?|LVERLOCK|ZERULE)|P(?:[BS]|O(?:RT(?:S(?:PERSON|EVENT)|BASIC|CRIT|FLAG)|IL(?:ER(?:ALERT)?)?|NSORED|TVAN)|E(?:LL(?:CHECK|BOT|ING)?|AKENGLISH|CULATION|EDY)|AM(?:LINKS?|#LINK|BAIT|NAME|MER)?|(?:URIOUSPROTEC|LITLIS)T|I(?:NO(?:FF|UT)|P)|CU|NC)?|U(?:B(?:ST(?:(?:MUS|NO)T|ANTIATE)?|JECT(?:IVE(?:CAT)?)?|(?:CA|NO)T|ARTICLE|TITLES?|POV)?|P(?:P(?:LEMENTAL|RESS)|ER(?:PROTEC|CA)T)|S(?:TAINED|PECT)|R(?:VIVEDBY)?|ICIDE|MMARY|LF)|O(?:F(?:T(?:(?:SIS|TEM)P|DELETE|BLOCK|REDIR)|IXIT)|URCE(?:(?:ACCES|TYPE)?S|LI(?:NKS|ST))?|C(?:K(?:#NOTIFY|LEGIT)?|IALMEDIA)|VEREIGN(?:FLAG)?|AP(?:BOX)?|NGDAB|RTKEY)|T(?:A(?:LE(?:DRAFT)?|ND(?:ALONE)?|GENAME|RNAMES)|U(?:B(?:S(?:PACING)?|DEF|IFY)?|DENTMEDIA)|R(?:ONGPASS|AWSOCK|UCTURE)|E(?:WARDSHIP|ALTH)|ICK(?:TOSOURCE|Y)|ONEWALL)|E(?:LF(?:P(?:UB(?:LISH)?|ROMOTE)|(?:SOURC|CIT)E|BLOCK|RED)?|C(?:OND(?:ARY)?|UREADMIN)|T(?:NOTDAB|INDEX|CAT)|(?:NSATIONA|ARCHDE)L|EKHELP|PARATE|MI)|H(?:I(?:P(?:PRONOUNS|NAME|DAB)|T)|ARE(?:D(?:ACCOUNT|NAME))?|O(?:UT(?:ING)?|RT)|E(?:4SHIPS|PHERD))|C(?:O(?:TLANDPLACE|PEWAR)|R(?:ABBLE|UTINY)|HOLAR(?:SHIP)?|(?:ICIT|LOS)E|JARGON|NAMES|G)?|A(?:Y(?:WHERE(?:YOU(?:READ|GOT)IT)?)?|L(?:ORDER|LEAD|A?T)?|NCTIONGAM(?:ING|E)|MPLE|ID)|K(?:(?:#NO|CRI)T|YBLUELOCK|ATER)?|Y(?:N(?:TH(?:ESIS)?|C)?|SOP)|M(?:ALL(?:DETAILS|CAT)?|I)|N(?:OOKER/(?:MOS|NF)|EAKY)|R(?:(?:BPLAC)?E|TA|D)|ignature forgery|W(?:Y[GR]T| )|(?:BA|F)N|VSP|S)|B(?:L(?:P(?:R(?:E(?:(?:QUEST(?:RESTOR|DELET)|MOV)E|LATED)|S)|S(?:E(?:LF(?:PUB)?|EALSO)|OURCES?|TYLE|PS)|C(?:O(?:MPLAINT?|I)|(?:RIM|IT)E|AT)|P(?:R(?:I(?:MAR|VAC)Y|OD)|UBLIC)|N(?:AM(?:EABUS)?E|OTE )|F(?:R(?:INGE)?|AMILY)|D(?:EL(?:ETE)?|S)|A(?:DMINS|BUSE)|G(?:OSSI|ROU)P|(?:BALANC|1)E|KIND(?:NESS)?|E(?:DIT|L)|TALK)?|O(?:CK(?:EV(?:IDENCE|ASION)|P(?:REVENTATIVE)?|NO(?:TPUNITIVE)?|DETERRENT|BANDIFF|ME)?|GS)|A(?:NK(?:ANDREDIRECT|ING)?|CKL(?:IST|OCK)|ZON|R)|UELOCK|Z)|O(?:T(?:(?:US(?:ERSPAC)?|REQUIR|ISSU)E|A(?:PP(?:ROV|E)AL|SSIST|CC)|(?:TOMPOS|SCRIP|PCA)T|CO(?:NFIG|MM)|MULTIOP|BLOCK|FLAG|DEF)|OK(?:S(?:TORE|PAM)|P(?:LOT|ROD)|LINKS|CRIT|DAB)|LD(?:NOTOBLIGATORY)?|WDLERIZE)|A(?:N(?:D(?:LOGO|NAME|DAB)?|BLOCKDIFF|LENGTH|REVERT|POL|EX)?|D(?:CHARTS|IDEA|NAME|SOCK)|L(?:A(?:NCED?|SP)|L)|S(?:E(?:BALL)?/N|IC)|TTLE(?:GROUND)?|GREQ)|I(?:O(?:DEL(?:ETE)?|RELATED|FAMILY|SELF|1E)?|BLIOGRAPH(?:IES|Y)|ASED(?:SOURCES)?|DI(?:RECTIONAL)?|LLBOARDCHARTS|(?:GDELE)?TE|RTHDOY|SHOP)|U(?:(?:TIDONTKNOWABOUTI|LLE(?:TLIS)?)T|R(?:MESE|DEN|EAU|O)|NDLING)|R(?:O(?:AD(?:C(?:ONCEP|AS)T)?|CHURE)|EAKING|ANCH|INT)|K(?:CR(?:YSTAL|IT)|MERGE|ST|TS|D)?|E(?:FOREBLOCK(?:ING)?|STSOURCES)?|DP(?:LACE)?|CA(?:ST)?|P(?:ROD)?|M?B|NO)|M(?:O(?:S(?:C(?:O(?:NVERSIONS|MM)|A(?:[NT]|PS )|HEM(?:/NAME)?|PT |UE)|-(?:(?:BIBLI|K)O|NOVELS|AM|JA)|L(?:AYOUT|YRICS|EAD|INK|OGO)|M(?:USIC(?:CAPS)?|AC3?|ED)|S(?:OPHOMORE|NOOKER|IS|G)?|T(?:[MV]|UNINGS|ITLE|EXT)?|I(?:S(?:LAM)?|(?:CO)?N)|P(?:(?:HI|O)L|A?K|RON)|F(?:I(?:LM|A)|LAG|R)|DA(?:TESGP|B)|A(?:BBR|T)|HAWAII|KOREA|BIO|NUM|WTW|VG)?|N(?:O(?:TYPICF(?:AUN|LOR)A|NYM)|TAGE)?|V(?:IE(?:PLOTS| )|EVANDAL|P)|P(?:RIGHTS|FIGHT)?|DERNPLACENAME|RMON)|I(?:L(?:MOS(?:#(?:C(?:O(?:DE(?:STYL|NAM)E|NFLICTS)|A(?:MPAIGNS|TNAME)|IT(?:ESTYL)?E)|B(?:A(?:TTLES(?:IN)?|SENAME)|PROJ)|N(?:A(?:V(?:PROBLEMS)?|ME)|ESTED)|S(?:PECIFIC|ECTLEN|OURCES)|(?:OPCAT|FLAG|TANK|WAR)S|IN(?:TERSECTION|FOBOX)|(?:DATERANG|PRECIS)E|UNIT(?:NAME|S)|APP))?|(?:(?:CI|DA)T|NAM)E|S(?:OURCE|G)|FORMAT|APP)|S(?:C(?:ELLAN(?:EA|Y))?|LEADNAME)|(?:DDL(?:ENAM)?|NESTYL)E)|E(?:D(?:S(?:E(?:CTIONS|ARCH)|CI)|C(?:O(?:PY|I)|ASE)|P(?:RI(?:CE)?|OP)|A(?:NIMAL|SSESS)|B(?:IAS|OOK)|R(?:E[FV]|S)|D(?:ATE|EF)|LE(?:AD|DE)|OR(?:DER|G)|TRIVIA|INDY|MOS)|A(?:T(?:(?:PUPPE|BO)T)?|SUREMENT)|TRIC)|U(?:S(?:IC(?:/(?:CHARTS|TABLE)|SERIES|BIO)|ORG)|LT(?:I(?:ACCOUNT|DABS|PLE)?|SOURCES)|G)|A(?:I(?:NTPAGES|DEN)|SSCREATION|DEUP|POF)|FD/SRE?|CSTJR|BIAS|TAU|NA|PN|SM|J)|P(?:[12DN]|R(?:O(?:J(?:GUIDE(?:#OWN)?|S(?:COPE|TUB)|CATS|PAGE)|P(?:O(?:RTION|SAL)|AG(?:ANDA|ES)|ERNAME)|(?:T(?:AGONIS|EC)|VEI)T|CE(?:DURALCLOSE|PAGES)|D(?:UCT(?:REV)?|NOM)?|F(?:(?:RING|AN)E)?|MO(?:NAME|TION)?|XYING)|E(?:(?:S(?:SRELEAS|ERV)|EMPTIV)E|CIS(?:E(?:LANG)?|ION)|VIEWS|FER)|I(?:MARY(?:REDIRECT|TOPIC|USAGE|FILM)?|VA(?:TEFILTER|CY))|J(?:C(?:RE)?|DEL|SD)?|D)|A(?:GE(?:(?:LINK)?S|BLANKING|DECIDE|NUM)|R(?:TI(?:SAN|AL)|ENDIS|ITY)|ID(?:ATTRIBUTE|COPYRIGHT)|Y(?:SITE|TALK|WALL)?|T(?:EN)?T|PER)?|O(?:L(?:I(?:C(?:YPAG|I)ES|TICIAN)|EMIC|CON)|V(?:NAM(?:ING|E)|SPLIT|TITLE|FORK)?|INT(?:WIKT|y)?|TENTIALCOI|(?:RT)?G|STEMAIL|ET|FR)|E(?:R(?:S(?:ON(?:AL(?:ATTACKS)?)?|ISTENCE)|F(?:ECTION|CAT|NAV)|M(?:-PRO|ADEL)|P(?:ETRATOR)?|CENT)|A(?:COCK)?|OPLE|ERS)?|L(?:A(?:G(?:FORMS?|IARISM)?|CE(?:DAB)?|NETNAMES|YPOLICY)|U(?:RAL(?:PT)?|G)|O(?:TBLOA)?T)|I(?:C(?:TURES?|SIZE)|N(?:KLOCK|YIN)|XIEDUST|LLARS|FU)|U(?:BLI(?:CFIGURE|SHED)|RPL(?:ELOCK|IST)|FFERY)|G(?:(?:CHANG|LIF)E|BOLD)|S(?:[AR]|EUDONYM|CI|TS)|P(?:INDEF|LIST|DRV)?|T(?:OPIC|PROT|M)|C(?:LOSE|PP|SD)|M(?:R[CR]|VRC)|B(?:AN|Y)|HILMOS)|D(?:E(?:L(?:#(?:PROCESSES|CONTENT|REASON)|-(?:PROCESSES|CONTENT|REASON)|PRO(?:#(?:[ACFMRT]FD|DRV))?|A(?:FD|Y)|TALK|ETE)?|S(?:C(?:RIP(?:DIS|TOR)|F)|TUB)|T(?:ERMINEPRIMARY|AIL)|A(?:THDOY|DREF|L)|M(?:OCRACY)?|P(?:ROD|TH)|UTERAGONIST|FINITE|CIMAL|RRY)?|A(?:B(?:CO(?:N(?:G(?:AME|EO|OV)|(?:SPOR|CEP)T|P(?:HYS|ROD)|BRAND|MATH|OFF)|MBINE)|N(?:O(?:INCLUDE|T)|AME)|S(?:ISTER|TYLE|ONG)|A(?:CRONYM|BBREV)|DI(?:SPLAY|C)|RE(?:LATED|F)|LINKS?)?|TE(?:LI(?:NK|ST)|RANGETITLES)|PE)|I(?:S(?:RUPT(?:SIGNS|NAME)?|P(?:UTED?|AGES)|A(?:MBIG|STER)|CL(?:AIM|OSE)|ENGAGE)?|A(?:CRITICS|LECT|RY)|FF(?:PUNCT|CAPS|USE)|V(?:IDEDU|ER)SE|RECTOR|CDEF|GITS)|O(?:N(?:T(?:SHOUTBIAS|GETIT|HOAX)|OTFIXIT)?|(?:UBLEDA)?B|Y(?:CITE)?|GBITESMAN|A[CL]|OR|PP|TY|X)|P(?:R(?:#(?:[ACFMRT]FD|DRV|NAC))?|A(?:GES?|FD))?|U(?:PC(?:ITES|AT)|BIOUS|E)|R(?:AFTNOCAT|#RfCs)?|W(?:H(?:OAX)?|MP|G)|C(?:OI|V)|D(?:AB|E)|G(?:FA?)?|B[CN]|LINKS|NCH)?|I(?:N(?:FO(?:BOX(?:ETH(?:NICITY)?|(?:IMAG|CIT)E|FLAG|GEO|REF)|PAGES)|D(?:I(?:C(?:ATEAVAIL|SCRIPTS?)|SCRIMINATE)|E(?:PTH|F)|CRIT)|T(?:E(?:R(?:WIKIBOT|SPERSE)|GRITY|XT)|DAB(?:LINK|S)?)|C(?:OM(?:P(?:ATIBLE|DAB)|INGLINKS)|DAB|ITE)|LINEC(?:ITE(?:CLUTTER)?|LUTTER)|HER(?:IT(?:ORG|WEB)|ENTWEB)|V(?:ALIDBIO|ISIBLE|OLVED)|ACTIV(?:EWP|ITY)|(?:KLES|IT)S)|M(?:P(?:ER(?:SONAT(?:OR|E)|FECT)|LICITCONSENSUS|ARTIAL)|AGE(?:S(?:IZE)?|POL|RES)?|O(?:S FLAG)?S|GSIZE)|D(?:-(?:N(?:AME|C)|SPELLING)|E(?:NTIFYUNCIVIL|ALSTUB)|I(?:DNTHEARTHAT|OM)|HT)|U(?:P(?:#(?:(?:COPYRIGH|FORMA)T|ANIM|NAME|RI)|C)?|C)?|T(?:N(?:(?:AWARD|SPORT)S|R)|A(?:LICTITLE)?|SELF)|R(?:E-(?:CATS|IRL)|ISH FLAGS|LSTATION)|C(?:(?:ONDECORATI)?ON|ANTHEARYOU)|PE(?:XEMPTCONDITIONS|C(?:PROXY)?)|S(?:[EU]|A(?:TERM|WORD)FOR)|L(?:L(?:EGIT|CON)|CLUTTER)|mage resolution|(?:QUEU|JM)E|B(?:ID?|AN)|G(?:NORE)?|INFO|AR)|A(?:[23579]|D(?:M(?:IN(?:A(?:BUSE|CCT)|ISTRATORABUSE|S(?:HOP|OCK)|BOTS?|COND)?|AS[KQ])|V(?:ICEPAGE)?|PROMO|S)?|T(?:T(?:R(?:IBUTEPOV|EQ)|ACK(?:NAME)?|SIT)|D(?:-(?:[EIMR]|T(?:RANS)?)|AB|IS)?|H(?:LETE)?|P)?|R(?:B(?:ITRARYCAT|COND|POL)|CHI(?:VENOTDELETE|TECT)|T(?:SPAM|IST|N)|MEN|GH)|N(?:T(?:ICIPATION|AGONIST)|Y(?:USER|BIO)| OPINION|CITE|D)|C(?:CESSIBILITY|HIEVE NPOV|RONYMTITLE|TUALCOI|ADEMIC|SD)|U(?:T(?:O(?:#IFEXIST|BIOG?|PROB)?|HOR)|RDNAME|D)|P(?:P(?:ROPRIATEICONS|ARENTCOI|NOTE|EAL)|B)?|S(?:T(?:ROART|2000)|S(?:ISTED|ESS)|OF|L)?|VOID(?:EDITWAR|VICTIM|ABUSE|SPLIT|YOU)|L(?:L ANARCHISTS|BUMDAB|TACCN|UM)|ppearance and color|G(?:E MATTERS|FC?)|O(?:A[CL]|BF|HA)?|B(?:OUTSELF|AN)?|E(?:STHETIC|IS)|F(?:FILIATE)?|1[01]?|IR/NC|AB|WW)|R(?:[234]|E(?:D(?:L(?:INK(?:BIO|S)?|OCK)|IR(?:ECTPROTECTION)?|D(?:EAL|IT)|ACT(?:ED)?|UNDANTFORK|[CH]AT|FLAG|NOT?|BIO|YES)?|L(?:I(?:AB(?:ILITY|LE)|ST)|A(?:RT?|TED)|EASENOTES|TIME|Y)|C(?:OGNIZABILITY|IDIVISM|KLESS|USAL)|V(?:DEL(?:REQUEST)?|ERTBAN|IVE)|MOVE(?:UNCIVIL|D)|F(?:LOOP|SPAM)?|ALNAME|QUIRED|SOL)|S(?:(?:CONTEX|EC)T|/(?:[AM]C|SPS)|(?: AG|U)E|BREAKING|OPINION|PRIMARY|SELF|MED)?|O(?:L(?:L(?:BACK(?:USE)?)?|E)|U(?:GHCONSENSUS|TINE)|MA(?:JI|NS)|OMMATE|BIN)|#(?:C(?:ATEGORY|RD)|ASTONISH|SUPPRESS|HARMFUL|DELETE|KEEP|PLA)|P(?:[ACS]|R(?:OTECTION|GM)|URPOSE)|A(?:(?:WDAT|A)A|(?:CIS)?T|PID)|U(?:[CDU]|NAWAY|MOUR)|(?:(?:ICHMED)?I|G)A|N(?:EUTRAL|POV)|(?:L/?|M)N|C(?:AT|SD)|D/G(?:/M)?|V(?:AN|DL)|T(?:OA|V)|Y[BD]?|BK|JL)?|T(?:[23]|A(?:LK(?:#(?:(?:C(?:OMMUNIC|RE)AT|OBJECTIV|US)E|(?:DISCUS|FACT)S|NOMETA)|(?:DONTREVER|FIRS)T|C(?:ENT|OND)|N(?:EW|O)|O)?|G(?:LINE|STUB)|XO(?:BOX)?|RGET)|I(?:TLE(?:S(?:(?:PECIALCHARACTER|INTITLE)S|LASH)|CHANGES|FORMAT|LENGTH|P?TM|VAR)?|NFOILHAT|LDE)|R(?:A(?:NS(?:CRIPTION|LITERATE)|CEIP|ILER)|I(?:V(?:IA(?:LCAT)?)?|TAGONIST|BE)|HAT)|E(?:CH(?:-CONTENT|NICAL)|MPLATECAT|XTBOOKS|ACHER |NNIS/N|RTIARY|STLINK)|O(?:P(?:(?:ICCA|POS)T|100|TEN)|O(?:LMISUSE|MANY|BIG))|P(?:E(?:REVOKE|GRANT)|G(?:#YES)?|NO?|OC?|ROT|YES|TM)|H(?:E(?:YUKON|UNI)?|REESTRIKES|UMBSIZE)|V(?:S(?:E(?:ASON|RIES)|HOW)|-NC|EP)|W(?:ITTER|ODABS)|TS(?:TYLE|G)|URQUOISELOCK|C(?:AT|SD)|X(?:TBKS)?|B(?:AN|K)|S(?:UB|C)|(?:MP)?G|FOLWP)|F(?:[23456789]|I(?:L(?:M(?:(?:(?:C(?:RITICLI|A)|HI)S|PLO)T|M(?:A(?:RKETING|KER)|USIC)|(?:RATIN|FLA)G|N(?:AV|FI|OT)|LE(?:AD|DE)|SC(?:ORE|I)|DIFF|YEAR)|E(?:(?:REDIREC|CA)T|NAMES|SIZE)|(?:IBUS)?TER)|X(?:THEPROBLEM|DABLINKS|IT)|NAL RUNG|DUCIAL|GURE/N)|A(?:I(?:L(?:(?:EDVERIFICATIO)?N|CORP|ORG)|RUSE |TH)|(?:LSEBALANC|KEARTICL)E|CTIONS|MILY|UNA)|R(?:E(?:E(?:COPYING|R)|NCHNAMES|SHSTART)|IN(?:GE(?:LEVEL|/PS|BLP)?|D)|NG)|L(?:A(?:G(?:PLACEHOLDER|CRUFT|BIO)|TLIST)|O(?:WERY|RA))|U(?:T(?:URE(?:ALBUMS?)?|ONBIAS)|R(?:THERDAB|G)?|G |LL)|O(?:R(?:CEDINTERPRET|UM(?:SHOP)?)|URTILDES|LLOWING|C)|M(?:V/W|NN)|(?:DES|N)C|C(?:OI|SD)|1[01])?|E(?:L(?:M(?:IN(?:OFFICIAL)?|AYBE)|B(?:URDEN|LP)|PO(?:INTS|V)|(?:LIS|HA)T|D(?:EAD|UP)|N(?:EVER|O)|R(?:EG|C)|T(?:EMP)?|OFFICIAL|#ADV|CITE|YES|WD)?|X(?:T(?:RAORDINARY|ERNALREL|PROMO)?|P(?:LAIN(?:BLOCK|LEAD)|ABBR)|EMPT(?:BOT|1E)|(?:HAUS|OAR)T|CEPTIONAL)|V(?:A(?:(?:LFRING|D)E|SION)|ENT(?:CRIT(?:ERIA)?)?)|D(?:IT(?:ORIAL(?:IZING)?|CONSENSUS|ING|WAR)?|RED)|P(?:ON(?:YMOUS)?|CATPERS|ISODE|TALK|DAB)?|S(?:(?:DO(?:NT)?|SAYPAGE)S|TABLISHED)|N(?:T(?:ERTAINER)?|FORCEMENT|GLISH)|T(?:HNIC(?:RACECAT|GROUP)|IQ)|C(?:ON(?:OMIST|/RS|RSW)|P)|F(?:M(?:AILING)?|FECT)?|M(?:AILPOST|ERGENCY)|(?:GR|I)S|UPHEMISM|W(?:LO)?|ARLY|Q)|U(?:[1235]|S(?:E(?:R(?:B(?:OX(?:C(?:REATE|AT))?|IO)|CAT(?:YES|NO)?|G(?:ENERATED)?|N(?:OCAT|AME)|(?:SUB)?PAGE|TALKBLOG)?|MODDOMAIN|BYOTHERS)|S(?:TATION|H)|CHARTS|PLACE|OP)|P(?:#(?:P(?:RO(?:TECT|MO)|OLEMIC)|DEL(?:TALK|ETE)|NOT(?:SUITED)?|C(?:OPIES|MT)|G(?:AME|OAL)S|OWN|SUB)|(?:(?:P?R|N)O|FRON)T|LOAD-P|GOOD|YES|OL|E)?|N(?:I(?:T(?:(?:(?:SYMBOL)?|NAME)S)?|NVOLVED|VERSE)|C(?:ENSORED|IVIL|ONF)?|(?:RESPONSIV|DU)E|S(?:OURC|IGN)ED|B(?:LOCK|AN))|B(?:X(?:CREATE|NS)?|LIST|CR|O)|K(?:STATION(?:DAB)?|PLACE)|R(?:(?:DUSCRIP|GEN)T|AA)|C(?:AT|RN|SD)|E(?:IA)?|G[CS]|OWN|DP)|O(?:[IM]|R(?:G(?:CRITE?|DEPTH|IND?|NAME|SIG)?|ANGE(?:LOCK)?|IGINAL|DER)?|N(?:E(?:(?:SHORTHA|EVEN)T|D(?:OWN|AY)|HANDGIVES|OTHER|WAY)|US)|C(?:A(?:SSOC|WARD|T)|E(?:GRS|PON)|LOCATION|VENUE|MISC|/U|SD)?|VER(?:S(?:IMPLIFY|ECTION)|(?:LAP)?CAT)?|W(?:N(?:ER(?:SHIP)?|BEHAVIOR|TALK)?|H)|THER(?:SPAM(?:EXISTS)?|PARENT|NAMES)|P(?:INIONCAT|TIONS|ED)|(?:KAYCHART|A)S|S(?:(?:PO|B)L)?|pen a COIN|LDBOOK|B[EK]|HOTMU|UTING)|L(?:I(?:ST(?:C(?:RITERIA|OMPANY)|(?:GLOSSAR|VERIF)Y|(?:S?OFLIST|A)S|P(?:EOPLE|URP)|N(?:AME)?|E[DN]|RCAT|BIO)|NK(?:S(?:TOAVOID|PAM)|B(?:OXES|ACK)|FARM|LOVE|VIO)|VE(?:SCORES)?)|O(?:CALCONSENSUS|W(?:ERCASE)?|GO(?:UT|S)?|NDONDERRY|UTSOCK)|E(?:A(?:DFORALIST|C(?:AT)?|VE)|G(?:ALMOS|ITHAT)|NGTH)|A(?:TINPLEASE|STING|WMOS|BEL)|D(?:S(?:JARGON|MOS)|ERRY)|PNAME|YRICS|[SU]C)|W(?:H(?:E(?:N(?:NOTCIT|INROM|TABL)E|EL)|AT(?:ISTOBEDON|PLAC)E|Y(?:BLOCK|CITE|N)|I(?:TELOCK|M)|OIS)|E(?:B(?:(?:PAG|SIT)E|NOTE |CRIT)?|LLKNOWN|STBANK|ASEL|IGHT)|I(?:KI(?:HOUND(?:ING)?|VOICE)|A(?:PA|N)|THDRAWN|NI)|O(?:R(?:D(?:PRECEDENCE|ISSUBJECT)|KS)|NTWORK)|A(?:R(?:NVAND)?|TERMARK|WI)|P(?:NOTRS|BB/N|EDIT)|MF-PRO|QT?|W)|G(?:[23456789]|A(?:M(?:E(?:(?:GUID|TYP)E|CRUFT)?|ING)|SLIGHT(?:ING)?|LLERY)|E(?:O(?:(?:LAN|ROA)D|SCOPE|FEAT|PURP)|NREF|TTY|VAL)|R(?:A(?:TUITOUS|PEVINE)|EE(?:NLOC)?K|UDGE|OUP)|O(?:OD(?:CHARTS|FAITH)|LDLOCK)|L(?:OBALBOTS|C)|H(?:ETTO|BH)|F(?:FENSE)?|B(?:OOKS)?|1[01234]?|UIDES|IPBE|CSD|NG)|V(?:G(?:/(?:P(?:O[PV]|LOT)|(?:MIXE|LEA)D|RE(?:LEASE|C)|DATE(?:CAT)?|CONTENT|NONENG|STYLE|EL|JP)|IMAGES|JARGON|LAYOUT|ORDER|SCOPE|BOX)|A(?:N(?:D(?:TYPES|NOT|AL)?|ISH(?:ED )?)|LID(?:ALT)?|MOS)|I(?:(?:ETPLA|OLEN)CE|CTIM)|ER(?:IFY(?:OR)?)?|OTESTACK(?:ING)?|NOTSUFF|ULGAR|D)?|H(?:A(?:T(?:NOTE(?:PLACE|RULES)|EXTRA)?|R(?:DBLOCK|ASS)?|ND(?:LE)?|#NOT|STE)?|O(?:W(?:TO(?:PAGES|DAB)|CITE)|UND(?:ING)?|AX)|I(?:S(?:TORICAL|PAGES)|DDEN(?:CAT)?|GHRISK)|E(?:A(?:LTH|DE)RS|BREW)?|R(?:ULES|T)|U(?:H?|SH)|N[EPRS]?|SOCK|TSV)|Y(?:E(?:AR(?:SINFILM|LINK)|LLOW(?:PAGES)?|SPOV)|OU(?:NGATH|RSELF|TUBE)|(?:TCOPYRIGH)?T)|J(?:(?:A?TITL|PPLAC|UDG)E|OURNALIST|R/SR|&S|FN)|3(?:[DX]|(?:STRIK|TILD)ES|RR(?:BLP|NO)?)|Q(?:U(?:ESTION(?:ABLE|ED)|ALIFIER)|S)|1(?:.0/A|5MOF|DAY |HAT|RR|E)|X(?:(?:CS|F)D|2)|4(?:TILDES|RR)|5(?:TILDES|P)|0(?:RR|WW)|(?:|)|ZHNAME|2DABS|F*\**|911 |KEEP|£|$)|ikipedia:(?:N(?:aming conventions (?:(definite or indefinite article at beginning of name)|(U.S. state and territory highways)|(law enforcement agency categories)|(UK Parliament constituencies)|(government and legislation)|(country-specific topics)|(ethnicities and tribes)|(technical restrictions)|(Football in Australia)|(astronomical objects)|(places in Bangladesh)|(royalty and nobility)|(stations in Poland)|(Canadian stations)|(Latter Day Saints)|(numbers and dates)|(political parties)|(Australian roads)|(baseball players)|(geographic names)|(Norse mythology)|(writing systems)|(Irish stations)|(ancient Romans)|(capitalization)|(broadcasting)|(sports teams)|(sportspeople)|(New Zealand)|(UK stations)|(US stations)|(manuscripts)|(use English)|(video games)|(ice hockey)|(long lists)|(television)|(Macedonia)|(Mongolian)|(West Bank)|(chemistry)|(companies)|(languages)|(Armenian)|(aircraft)|(Burmese)|(Chinese)|(Tibetan)|(plurals)|(Hebrew)|(Korean)|(clergy)|(comics)|(events)|(operas)|(people)|(Greek)|(Indic)|(books)|(fauna)|(films)|(flora)|(music)|(ships))|o(?:tability(?: (?:(organizations and companies)|(astronomical objects)|(geographic features)|(video games)|(academics)|(numbers)|(events)|(people)|(sports)|(books)|(films)|(media)|(music)|(web)))?|n-(?:free (?:use rationale guideline|content(?: criteria)?)|discrimination policy|U.S. copyrights)| (?:(?:disclaimers in article|3D illustration|personal attack|legal threat)s|original research))|e(?:w pages patrol/Reviewers|utral point of view))|M(?:a(?:nual of Style(?:/(?:(?:I(?:(?:n(?:d(?:ones)?ia-related articl|fobox)|(?:reland|slam)-related articl|mag)e|con)|D(?:isambiguation page|ates and number)|R(?:oad junction lis|ecord char)t|(?:Japan|Korea)-related article|Vi(?:deo game|sual art)|Novel)s|C(?:(?:a(?:p(?:ital letter|tion)|nada-related article)|ue sport)s|h(?:ina and Chinese-related articles|emistry)|om(?:puting|ics))|S(?:(?:tringed instrument tuning|ingapore-related article)s|elf-references to avoid|pelling|nooker)|P(?:hil(?:ippine-related articles|osophy)|(?:akistan|oland)-related articles|ronunciation)|A(?:(?:(?:nime- and manga-related articl|rticle message box)e|bbreviation)s|ccessibility)|L(?:i(?:st(?:s of work)?s|nking)|a(?:tter Day Saints|yout)|e(?:ad section|gal))|M(?:(?:edicine-related article|athematic)s|usic(?: samples)?|ilitary history)|T(?:(?:r(?:ivia section|ademark)|(?:ab|it)le)s|e(?:xt formatting|levision))|F(?:rance and French-related articles|ilm)|W(?:riting about fiction|ords to watch)|H(?:awaii-related articles|idden text)|B(?:iography|lazon)))?|ke technical articles understandable)|iscellany for deletion/Speedy redirect)|W(?:iki(?:Project (?:(?:Belgium/(?:(?:Castle, country house, château and kasteel|Brussels) naming convention|Alternate language name)|Swiss municipalities/Article title convention|Ireland/Ireland Category Norm)s|Co(?:(?:mputer science/Manual of styl|uncil/Guid)e|llege football/Naming conventions)|Economics/Reliable sources and weight|Mining/Style guide)|pedia is not (?:for things made up one da|a dictionar)y|media (?:sister projects|policy))|hat Wikipedia is not)|C(?:a(?:tegor(?:i(?:z(?:ation(?:/Ethnicity, gender, religion and sexuality| of people)?|ing redirects)|es, lists, and navigation templates)|y names)|nvassing)|o(?:n(?:tent (?:assessment|forking)|flict of interest|sensus)|py(?:right(?: violation)?s|ing within Wikipedia)|urtesy vanishing)|h(?:anging username/Guidelines|ild protection|eckUser)|riteria for speedy deletion|i(?:ting sources|vility)|lean start)|P(?:r(?:o(?:posed deletion(?: (?:of biographies of living people|(books)))?|ject namespace|tection policy)|eparing images for upload)|a(?:(?:id-contribution disclosur|tent nonsens)e|ssword strength requirements|ge (?:blanking|mover))|l(?:ease do not bite the newcomers|agiarism)|o(?:licies and g|rtal/G)uidelines|eople by year|ublic domain|RIMARYRED)|D(?:o not (?:(?:include the full text of lengthy primary sourc|create hoax)es|disrupt Wikipedia to illustrate a point)|e(?:letion (?:(?:guidelines for administrator|forum|venue)s|p(?:rocess|olicy))|ceased Wikipedians/Guidelines)|is(?:(?:ambigua(?:tion/PrimaryTopicDefini)?|pute resolu)tion|ruptive editing)|ays of the year)|R(?:e(?:vi(?:ewing (?:pending chang|good articl)es|sion deletion)|ference desk/Guidelines(?:/Medical advice)?|(?:c(?:ord chart|ent year)|liable source)s|sponding to threats of harm|using Wikipedia content|d(?: link|irect))|ollback)|A(?:r(?:bitration(?: Committee/CheckUser and Oversight|/Policy)|ti(?:cle (?:titles|size)|st))|(?:narchism referencing guideline|dministrator)s|(?:ccuracy disput|ttack pag)e|s(?:sume good faith| of)|ppealing a block|utobiography)|S(?:(?:cientific citation guidelin|et index articl|ignatur)es|p(?:e(?:llchecking|edy keep)|am(?: blacklist)?|oiler)|u(?:b(?:stitution|pages)|mmary style)|o(?:ck puppetry|ft redirect)|t(?:and-alone lists|ub)|hortcut)|I(?:n(?:(?: the news/Recurring item|terface administrator)s|dic transliteration)|dentifying reliable sources (medicine)|mage(?: use policy|s)|P block exemption|gnore all rules)|T(?:e(?:mplate(?: (?:namespace|editor)|Styles)|levision episodes|rms of use)|(?:alk page (?:guidelin|templat)e|rinidad and Tobago Wikipedian)s)|O(?:ver(?:categorization(?:/User categories)?|sight)|(?:TRS member|pen proxie)s|wnership of content|ffensive material)|E(?:dit(?: (?:filt(?:er help)?er|warring)|ing policy)|xte(?:nded image syntax|rnal links)|vent coordinator|tiquette)|B(?:(?:(?:lock|ann)ing|ot) policy|iographies of living persons|road-concept article|e bold)|U(?:ser(?:(?: (?:categori|pag)|box)es|name policy)|pdating information)|L(?:i(?:nking to external harassment|bel)|yrics and poetry|ogos)|F(?:i(?:le (?:mover|names)|ve Pillars)|ringe theories)|V(?:(?:olunteer Response Tea|andalis)m|erifiability)|H(?:a(?:rassment|tnote)|igh-risk templates)|G(?:lobal rights policy|aming the system)))|w.wiki/[5i])\b)"

test_str = "Wikipedia:Neutral point of view Wikipedia:Neutral Point of View but wp:npov WP:NPOV and Wikipedia:Non-free content criteria"

print('test')
print('--------')

matches = re.finditer(regex, test_str, re.M)

for match in matches:
    print(match)