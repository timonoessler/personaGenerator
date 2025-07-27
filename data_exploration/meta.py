question_meta = {
    'Q0': {
        'text': 'Trinken Sie alkoholhaltiges oder alkoholfreies Bier bzw. bierhaltige Getränke?',
        'type': 'single',
        'labels': {1: 'Ja', 2: 'Nein', -99: 'Keine Angabe'}
    },
    'Q1': {
        'text': 'Wie häufig trinken Sie grundsätzlich alkoholfreies oder alkoholhaltiges Bier bzw. bierhaltige Getränke?',
        'type': 'single',
        'labels': {
            1: 'täglich',
            2: 'mehrmals pro Woche',
            3: 'mehrmals im Monat',
            4: 'einmal pro Monat',
            5: 'seltener als einmal pro Monat',
            -99: 'Keine Angabe'
        }
    },
    'Q2': {
        'text': 'In welchen Situationen trinken Sie Bier bzw. bierhaltige Getränke?',
        'type': 'group',
        'labels': {}
    },
    **{f'Q2{c}': {
        'text': txt,
        'type': 'single',
        'labels': {1: 'nie', 2: 'gelegentlich', 3: 'häufig', -99: 'Keine Angabe'},
        'parent': 'Q2'
    } for c, txt in [
        ('A', 'in Gesellschaft bei Freunden/Familie'),
        ('B', 'auf privaten Partys oder Feiern'),
        ('C', 'zuhause beim Essen'),
        ('D', 'zuhause zur Entspannung'),
        ('E', 'bei öffentlichen Veranstaltungen (Sport, Kultur, Musik etc.)'),
        ('F', 'in Bars, Restaurants, Pubs, Clubs etc.'),
        ('G', 'im Urlaub im Hotel, am Strand etc.')
    ]},
    'Q3': {
        'text': 'Nennen Sie uns Ihre bevorzugte(n) Lieblingsmarke(n) für Bier bzw. bierhaltige Getränke',
        'type': 'freetext',
        'labels': {}
    },
    'Q4': {
        'text': 'Wo kaufen Sie Bier bzw. bierhaltige Getränke hauptsächlich?',
        'type': 'group',
        'labels': {}
    },
    **{f'Q4{c}': {
        'text': txt,
        'type': 'single',
        'labels': {1: 'nie', 2: 'gelegentlich', 3: 'häufig', -99: 'Keine Angabe'},
        'parent': 'Q4'
    } for c, txt in [
        ('A', 'Stationärer Lebensmittelhandel (Supermarkt, Verbrauchermarkt, Discounter)'),
        ('B', 'Stationärer Getränkefachhandel/-abholmärkte'),
        ('C', 'Tankstelle'),
        ('D', 'Gastronomie/Hotellerie'),
        ('E', 'Kiosk/Späti/Büdchen/24x7 Store'),
        ('F', 'direkt in der Brauerei'),
        ('G', 'Mensa/Kantine/Verpflegungsautomat'),
        ('H', 'Lieferservice/Online-Lebensmittelhandel')
    ]},
    'Q5': {
        'text': 'Wie wichtig ist Ihnen, dass die von Ihnen konsumierten Biere bzw. bierhaltigen Getränke alkoholfrei sind?',
        'type': 'single',
        'labels': {
            1: 'völlig unwichtig',
            2: 'eher unwichtig',
            3: 'indifferent',
            4: 'eher wichtig',
            5: 'äußerst wichtig',
            -99: 'Keine Angabe'
        }
    },
    **{f'Q6{c}': {
        'text': txt,
        'type': 'single',
        'labels': {
            1: 'trifft überhaupt nicht zu',
            2: 'trifft eher nicht zu',
            3: 'teils/teils',
            4: 'trifft eher zu',
            5: 'trifft voll und ganz zu',
            -99: 'Keine Angabe'
        }
    } for c, txt in [
        ('A', 'Ich besitze ein großes Interesse an Bier oder bierhaltigen Getränken.'),
        ('B', 'Bier und bierhaltige Getränke spielen eine große Rolle in meinem Leben.'),
        ('C', 'Es macht mir großen Spaß, ein Bier oder bierhaltiges Getränk zu konsumieren.'),
        ('D', 'Der Konsum von Bier oder bierhaltigen Getränken ist sehr wichtig für mich.'),
        ('E', 'Der Konsum von Bier oder bierhaltigen Getränken ist sehr vorteilhaft für mich.'),
        ('F', 'Auf den Konsum von Bier oder bierhaltigen Getränken kann ich auf keinen Fall verzichten.')
    ]},
    **{f'Q7{c}': {
        'text': txt,
        'type': 'single',
        'labels': {
            1: 'trifft überhaupt nicht zu',
            2: 'trifft eher nicht zu',
            3: 'teils/teils',
            4: 'trifft eher zu',
            5: 'trifft voll und ganz zu',
            -99: 'Keine Angabe'
        }
    } for c, txt in [
        ('A', 'Gesunde Ernährung ist mir sehr wichtig.'),
        ('B', 'Mir ist es sehr wichtig, dass Getränke umweltfreundlich hergestellt und vertrieben werden.'),
        ('C', 'Ich probiere sehr gerne neue Produkte oder Geschmacksrichtungen aus.'),
        ('D', 'Für biologisch produzierte Getränke bin ich bereit, einen adäquaten Mehrpreis zu zahlen.'),
        ('E', 'Mir ist es sehr wichtig, dass bei der Herstellung keine Inhaltsstoffe tierischen Ursprungs verwendet werden.'),
        ('F', 'Mir ist es sehr wichtig, beim Konsum von Getränken völlig auf Alkohol zu verzichten.')
    ]},
    **{f'Q8{c}': {
        'text': txt,
        'type': 'single',
        'labels': {
            1: 'sehr geringer Einfluss',
            2: 'geringer Einfluss',
            3: 'mittlerer Einfluss',
            4: 'starker Einfluss',
            5: 'sehr starker Einfluss',
            -99: 'Keine Angabe'
        }
    } for c, txt in [
        ('A', 'Geschmack des Getränks'),
        ('B', 'Geruch/Aroma des Getränks'),
        ('C', 'Kaufpreis des Getränks'),
        ('D', 'Bekanntheit der Marke'),
        ('E', 'Nachhaltige Produktion des Getränks'),
        ('F', 'Herkunftsregion der Marke'),
        ('G', 'Design der Verpackung'),
        ('H', 'Verpackungsgröße/-form'),
        ('I', 'Aktionsangebot im Handel'),
        ('J', 'Alkoholgehalt des Getränks'),
        ('K', 'Empfehlung von Dritten'),
        ('L', 'Verfügbarkeit im Handel')
    ]},
    **{f'Q9{c}': {
        'text': txt,
        'type': 'single',
        'labels': {
            1: 'sehr niedrige Präferenz',
            2: 'niedrige Präferenz',
            3: 'mittlere Präferenz',
            4: 'hohe Präferenz',
            5: 'sehr hohe Präferenz',
            -99: 'Keine Angabe'
        }
    } for c, txt in [
        ('A', 'Alkoholfreies Bier oder alkoholfreie Biermischgetränke'),
        ('B', 'Weizenbier/Weissbier/Berliner Weisse'),
        ('C', 'Kölsch'),
        ('D', 'Altbier (z.B. Diebels)'),
        ('E', 'Pale Ale (IPA etc.)'),
        ('F', 'Stout (z.B. Guinness)'),
        ('G', 'Märzen/Export/Kellerbier/Zwickel'),
        ('H', 'Radler/Biermischgetränke'),
        ('I', 'Pils/Pilsner'),
        ('J', 'Bockbier/Schwarzbier/Rauchbier'),
        ('K', 'Helles oder Lager'),
        ('L', 'Craft Beer')
    ]},
    **{f'Q10{c}': {
        'text': txt,
        'type': 'single',
        'labels': {
            1: 'sehr niedrige Präferenz',
            2: 'niedrige Präferenz',
            3: 'mittlere Präferenz',
            4: 'hohe Präferenz',
            5: 'sehr hohe Präferenz',
            -99: 'Keine Angabe'
        }
    } for c, txt in [
        ('A', 'Alkoholfreies Bier ohne Alkohol (0% Alkoholgehalt)'),
        ('B', 'Alkoholfreies Bier mit sehr geringem Alkoholgehalt (bis max. 0,5%)'),
        ('C', 'Normales Bier mit Alkohol (> 0,5% Alkoholgehalt)')
    ]},
    **{f'Q11{c}': {
        'text': txt,
        'type': 'single',
        'labels': {
            1: 'sehr niedrige Präferenz',
            2: 'niedrige Präferenz',
            3: 'mittlere Präferenz',
            4: 'hohe Präferenz',
            5: 'sehr hohe Präferenz',
            -99: 'Keine Angabe'
        }
    } for c, txt in [
        ('A', 'rauchiger Geschmack'),
        ('B', 'herber-hopfiger Geschmack'),
        ('C', 'süßlich-malziger Geschmack'),
        ('D', 'fruchtiger Geschmack'),
        ('E', 'Geschmack nach Kräutern'),
        ('F', 'Geschmack nach Gewürzen'),
        ('G', 'bitterer Geschmack'),
        ('H', 'säuerlicher Geschmack'),
        ('I', 'Zitrusgeschmack')
    ]},
    **{f'Q12{c}': {
        'text': txt,
        'type': 'single',
        'labels': {
            1: 'gar nicht',
            2: 'schwach',
            3: 'mittel',
            4: 'stark',
            5: 'sehr stark',
            -99: 'Keine Angabe'
        }
    } for c, txt in [
        ('A', 'Werbung im Fernsehen, Radio oder Streaming-TV'),
        ('B', 'Werbung auf Social Media-Kanälen der Hersteller/Händler'),
        ('C', 'Empfehlungen durch Influencer:innen'),
        ('D', 'Werbung in Zeitschriften/Illustrierten'),
        ('E', 'Außenwerbung (Plakate, Events)'),
        ('F', 'Werbung in Sportstätten/Stadien'),
        ('G', 'Verkau fsförderung in Hauswurfsendungen'),
        ('H', 'E-Mail-Werbung/Apps von Herstellern/Händlern'),
        ('I', 'Verkau fsförderungen vor Ort im Ladengeschäft')
    ]},
    'Q13': {
        'text': 'Welchem Geschlecht ordnen Sie sich zu?',
        'type': 'single',
        'labels': {1: 'männlich', 2: 'weiblich', 3: 'divers', -99: 'Keine Angabe'}
    },
    'Q14': {
        'text': 'In welchem Jahr sind Sie geboren?',
        'type': 'single',
        'labels': {i: str(2008 - (i - 1)) for i in range(1, 16)} | {-99: 'Keine Angabe'}
    },
    'Q15': {
        'text': 'In welchem Bundesland wohnen Sie derzeit?',
        'type': 'single',
        'labels': {
            1: 'Baden-Württemberg', 2: 'Bayern', 3: 'Berlin', 4: 'Brandenburg', 5: 'Bremen',
            6: 'Hamburg', 7: 'Hessen', 8: 'Mecklenburg-Vorpommern', 9: 'Niedersachsen',
            10: 'Nordrhein-Westfalen', 11: 'Rheinland-Pfalz', 12: 'Saarland', 13: 'Sachsen',
            14: 'Sachsen-Anhalt', 15: 'Schleswig-Holstein', 16: 'Thüringen',
            17: 'nicht in Deutschland', -99: 'Keine Angabe'
        }
    },
    'Q16': {
        'text': 'Wie ist Ihre aktuelle Beschäftigungssituation?',
        'type': 'single',
        'labels': {
            1: 'Angestellte/Angestellter', 2: 'Selbständige/Selbstständiger',
            3: 'Student:in', 4: 'Schüler:in', 5: 'Beamt:in', 6: 'Rentner:in',
            7: 'Hausfrau/Hausmann', 8: 'ohne Beschäftigung', 9: 'in Ausbildung/Freiwilligendienst',
            -99: 'Keine Angabe'
        }
    },
    **{f'Q17{c}': {
        'text': txt,
        'type': 'multiple',
        'labels': {0: 'Nein', 1: 'Ja', -99: 'Keine Angabe'}
    } for c, txt in [
        ('A', 'alleinlebend'),
        ('B', 'mit Kind/Kindern lebend'),
        ('C', 'mit Eltern/Elternteil lebend'),
        ('D', 'mit Freund:in bzw. Lebenspartner:in lebend'),
        ('E', 'mit sonstigen Personen lebend (z.B. WG)')
    ]}
}
