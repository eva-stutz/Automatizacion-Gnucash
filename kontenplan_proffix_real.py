#Este codigo Funciona en Windows, Mac, Linux sin configuración adicional.
#en linux activo env en bash:  source pdf_env/bin/activate y luego ejecuto desde bash. 
#!/usr/bin/env python3
"""
GnuCash Kontenplan Generator - Proffix Real System 🏦
PARTE 1: Imports, Class y Aktiven

Basado en tu plan de cuentas real de 6 años de experiencia
Struktur auf Deutsch - Komplett aus deinem CSV extrahiert
"""

import xml.etree.ElementTree as ET
import uuid
import os
from datetime import datetime

class GnuCashKontenplanReal:
    def __init__(self):
        self.accounts = []
        self.currencies = ['CHF', 'USD', 'EUR']
        
        # Plan de cuentas REAL basado en tu Kontenplan CSV de Proffix
        self.kontenplan = {
            # AKTIVEN (Vermögenswerte) - 1000-1999
            'aktiven': {
                'name': 'Aktiven',
                'type': 'ASSET',
                'accounts': {  #Dieses Kontoplan gehört der Stiftung Sozialwerke Paz (www.stiftung-pazperu.ch - www.pazperuong.org). Wenn du möchtest, kannst sogar an die unter listeten Konten dein Beitrag geben.
                    # Flüssige Mittel (100) ##estas cuentas pertenecen a la fundacion Sozialwerke Paz: www.pazperuong.org - www.stiftung-pazperu.ch  Si quieres hasta puedes colaborar con el proyecto
                    '1000': {'name': 'Kasse', 'currency': 'CHF'},
                    '1020': {'name': 'UBS 296-983505.M1C CHF', 'currency': 'CHF'},  
                    '1022': {'name': 'UBS Stipendien 296-983505 0562 P USD', 'currency': 'USD'},
                    '1024': {'name': 'UBS 296-983505.60H USD', 'currency': 'USD'},
                    '1025': {'name': 'UBS 296-983505.M4H EUR', 'currency': 'EUR'},
                    '1030': {'name': 'Scotiabank cuenta corriente', 'currency': 'USD'},
                    '1031': {'name': 'Scotiabank Sparkonto', 'currency': 'USD'},
                    '1050': {'name': 'Festgelder', 'currency': 'CHF'},
                    
                    # Wertschriften mit Börsenkurs (106)
                    '1060': {'name': 'DEPOT UBS 296-983505-S1', 'currency': 'CHF'},
                    
                    # Forderungen Leistungen (110)
                    '1100': {'name': 'Debitoren Schweiz', 'currency': 'CHF'},
                    '1101': {'name': 'Debitoren Ausland', 'currency': 'CHF'},
                    '1109': {'name': 'Delkredere', 'currency': 'CHF'},
                    '1130': {'name': 'Forderungen (St.) Detracciones Perú', 'currency': 'USD'},
                    
                    # Übrige kurzfristige Forderungen (114)
                    '1140': {'name': 'Vorschüsse und Darlehen', 'currency': 'CHF'},
                    '1150': {'name': 'Treuhandkonto Arequipa', 'currency': 'USD'},
                    '1170': {'name': 'Vorsteuer MWST Material, Waren, Dienstleistungen, Energie', 'currency': 'CHF'},
                    '1171': {'name': 'Vorsteuer MWST Investitionen, übriger Betriebsaufwand', 'currency': 'CHF'},
                    '1176': {'name': 'Verrechnungsteuer', 'currency': 'CHF'},
                    
                    # Vorräte und nicht fakturierte Dienstleistungen (120)
                    '1200': {'name': 'Vorräte', 'currency': 'CHF'},
                    '1280': {'name': 'Nicht fakturierte Dienstleistungen', 'currency': 'CHF'},
                    
                    # Aktive Rechnungsabgrenzungen (130)
                    '1300': {'name': 'Aktive Rechnungsabgrenzungen', 'currency': 'CHF'},
                    
                    # Finanzanlagen (140)
                    '1400': {'name': 'Wertschriften', 'currency': 'CHF'},
                    '1411': {'name': 'Mietzinsdepot UBS', 'currency': 'CHF'},
                    '1440': {'name': 'Darlehen Paz Peru Arequipa', 'currency': 'CHF'},
                    '1441': {'name': 'Darlehen Techo propio II', 'currency': 'USD'},
                    '1442': {'name': 'Darlehen Div. Caritas', 'currency': 'USD'},
                    '1449': {'name': 'WB Darlehen Dritte', 'currency': 'USD'},
                    
                    # Mobile Sachanlagen (150)
                    '1510': {'name': 'Mobiliar Liegenschaft Peru', 'currency': 'CHF'},
                    '1520': {'name': 'Büromaschinen, Informatik, Kommunikationstechnologie', 'currency': 'CHF'},
                    '1530': {'name': 'Fahrzeuge', 'currency': 'CHF'},
                    
                    # Immobile Sachanlagen (160)
                    '1600': {'name': 'Liegenschaft Peru', 'currency': 'USD'},
                    '1609': {'name': 'WB Liegenschaft Peru', 'currency': 'USD'},
                }
            },
            
            
 ### Parte 2
            
# PASSIVEN (Verbindlichkeiten) - 2000-2999  
            'passiven': {
                'name': 'Passiven',
                'type': 'LIABILITY',
                'accounts': {
                    # Verbindlichkeiten aus Lieferungen und Leistungen (200)
                    '2000': {'name': 'Kreditoren Schweiz', 'currency': 'CHF'},
                    '2001': {'name': 'Kreditoren Ausland', 'currency': 'USD'},
                    
                    # Kurzfristige verzinsliche Verbindlichkeiten (210)
                    '2100': {'name': 'Treuhandkonto LBS USD', 'currency': 'USD'},
                    '2200': {'name': 'Geschuldete MWST (Umsatzsteuer)', 'currency': 'CHF'},
                    '2210': {'name': 'Kapital Friedhelm Krieger', 'currency': 'CHF'},
                    '2270': {'name': 'Sozial Versicherungen', 'currency': 'CHF'},
                    
                    # Passive Rechnungsabgrenzungen und kurzfristige Rückstellungen (230)
                    '2300': {'name': 'Passive Rechnungsabgrenzungen', 'currency': 'CHF'},
                    
                    # Langfristige verzinsliche Verbindlichkeiten (240)
                    '2400': {'name': 'LBS Darlehen Caritas', 'currency': 'CHF'},
                    '2401': {'name': 'LBS Darlehen Techo Propio II', 'currency': 'USD'},
                    
                    # Fonds (250)
                    '2500': {'name': 'Fonds Projekt Casa Isabel', 'currency': 'CHF'},
                    '2501': {'name': 'Fonds Projekt Sonrisas', 'currency': 'USD'},
                    '2509': {'name': 'Fonds Andere Projekte', 'currency': 'USD'},
                    '2510': {'name': 'Fonds Mikrokredit', 'currency': 'CHF'},
                    '2511': {'name': 'Fonds Stipendien', 'currency': 'CHF'},
                    
                    # Organisationskapital (280)
                    '2800': {'name': 'Stiftungskapital', 'currency': 'CHF'},
                    
                    # Reserven und Jahresgewinn oder Jahresverlust (290)
                    '2900': {'name': 'Freiwillige Gewinnreserven', 'currency': 'CHF'},
                    '2910': {'name': 'Erarbeitetes freies Kapital', 'currency': 'CHF'},
                    '2990': {'name': 'Jahresergebnis', 'currency': 'CHF'},
                    '2999': {'name': 'WB Abklärungskonto', 'currency': 'CHF'},
                }
            },
            
            # ERTRAG (Einnahmen) - 3000-3999
            'ertrag': {
                'name': 'Ertrag',
                'type': 'INCOME',
                'accounts': {
                    # Zweckgebundene Spenden (300)
                    '3000': {'name': 'Projekt Casa Isabel', 'currency': 'CHF'},
                    '3010': {'name': 'Projekt Sonrisas', 'currency': 'CHF'},
                    '3090': {'name': 'Andere Projekte', 'currency': 'CHF'},
                    '3100': {'name': 'Wohnungsverkauf', 'currency': 'USD'},
                    
                    # Allgemeine Spenden (320)
                    '3200': {'name': 'Einzelspenden', 'currency': 'CHF'},
                    '3205': {'name': 'Stipendien', 'currency': 'CHF'},
                    '3210': {'name': 'Kollekten', 'currency': 'CHF'},
                    '3220': {'name': 'Benefizveranstaltungen', 'currency': 'CHF'},
                    
                    # Diverse Erträge (34)
                    '3400': {'name': 'Warenverkäufe', 'currency': 'CHF'},
                }
            },
      
      ###PARTE 3

# AUFWAND (Ausgaben) - 4000-6999
            'aufwand': {
                'name': 'Aufwand', 
                'type': 'EXPENSE',
                'accounts': {
                    # Zweckgebundene Projektaufwand (400)
                    '4000': {'name': 'Aufwand Casa Isabel', 'currency': 'CHF'},
                    '4010': {'name': 'Projekt Sonrisas', 'currency': 'CHF'},
                    '4090': {'name': 'Andere Projekte', 'currency': 'CHF'},
                    '4100': {'name': 'Ausgaben Bauprojekt', 'currency': 'CHF'},
                    
                    # Leistungsaufwand Peru (420)
                    '4200': {'name': 'Laufende Ausgaben Peru', 'currency': 'CHF'},
                    '4210': {'name': 'Anschafungen Peru', 'currency': 'CHF'},
                    '4280': {'name': 'Projektbegleitkosten Peru', 'currency': 'CHF'},
                    '4290': {'name': 'Ausserord. Kosten Peru', 'currency': 'CHF'},
                    '4300': {'name': 'Stipendien und Beiträge', 'currency': 'CHF'},
                    
                    # Aufwand für bezogene Dienstleistungen (440)
                    '4400': {'name': 'Warenaufand / Fremdleistungen', 'currency': 'CHF'},
                    
                    # Diverse Stiftungsleistungen (447)
                    '4900': {'name': 'Übrige Stiftungsleistungen', 'currency': 'CHF'},
                    
                    # Personalkosten Stiftungsrat (50)
                    '5000': {'name': 'Stiftungsrathonorare', 'currency': 'CHF'},
                    '5070': {'name': 'Stiftungsratspesen', 'currency': 'CHF'},
                    
                    # Personalkosten Verwaltung (508)
                    '5200': {'name': 'Löhne und Gehälter', 'currency': 'CHF'},
                    '5270': {'name': 'Personalnebenkosten', 'currency': 'CHF'},
                    '5290': {'name': 'Leistungen Dritter', 'currency': 'CHF'},
                    
                    # Betriebsaufwand (600)
                    '6000': {'name': 'Raumaufwand', 'currency': 'CHF'},
                    '6100': {'name': 'Unterhalt, Reparatur, Ersatz', 'currency': 'CHF'},
                    '6200': {'name': 'Fahrzeugaufwand', 'currency': 'CHF'},
                    '6300': {'name': 'Haft- Sachversicherung', 'currency': 'CHF'},
                    '6500': {'name': 'Büromaterial', 'currency': 'CHF'},
                    '6510': {'name': 'Internet und Telekomunikation', 'currency': 'CHF'},
                    '6530': {'name': 'Buchführung und Revision', 'currency': 'CHF'},
                    '6540': {'name': 'Übriger Stiftungsaufwand', 'currency': 'CHF'},
                    
                    # Werbeaufwand (660)
                    '6600': {'name': 'Werbeaufwand', 'currency': 'CHF'},
                    '6640': {'name': 'Reise-/ Representationskosten', 'currency': 'CHF'},
                    
                    # Abschreibungen (680)
                    '6800': {'name': 'Abschreibungen Sachanlagen', 'currency': 'CHF'},
                    '6820': {'name': 'Abschreibungen EDV', 'currency': 'CHF'},
                    '6850': {'name': 'Abschreibungen Finanzanlagen', 'currency': 'CHF'},
                    '6890': {'name': 'Abschreibungen Darlehen', 'currency': 'USD'},
                    
                    # Finanzaufwand und Finanzertrag (69)
                    '6900': {'name': 'Finanzaufwand', 'currency': 'CHF'},
                    '6950': {'name': 'Finanzertrag', 'currency': 'CHF'},
                    '6951': {'name': 'Kurs Verlust', 'currency': 'CHF'},
                    '6980': {'name': 'Bankspesen', 'currency': 'CHF'},
                    '6990': {'name': 'Kursdifferenz', 'currency': 'CHF'},
                }
            },
            
            # SONSTIGE KONTEN (7000+)
            'sonstige': {
                'name': 'Sonstige Konten',
                'type': 'EXPENSE',
                'accounts': {
                    # Buchungskorrekturen / Vorjahresfehler
                    '7990': {'name': 'Buchungskorrekturen / Vorjahresfehler', 'currency': 'USD'},
                    
                    # Betriebsfremder Aufwand und betriebsfremder Ertrag (80)
                    '8000': {'name': 'Ausserordentlicher Aufwand', 'currency': 'CHF'},
                    '8010': {'name': 'Ausserordentlicher Ertrag', 'currency': 'CHF'},
                    
                    # Fondszuweisungen (-) / Fondsentnahmen (890)
                    '8900': {'name': 'Fonds Projekt Casa Isabel', 'currency': 'CHF'},
                    '8901': {'name': 'Fonds Projekt Sonrisas', 'currency': 'CHF'},
                    '8909': {'name': 'Fonds Andere Projekte', 'currency': 'CHF'},
                    '8911': {'name': 'Fonds Stipendien', 'currency': 'CHF'},
                    
                    # Abschluss (9)
                    '9000': {'name': 'Jahresgewinn/- verlust', 'currency': 'CHF'},
                }
            }
        }
                     
####PARTE 4
    def create_gnucash_xml(self, output_file):
        """Erstellt vollständige GnuCash-Datei mit deutschem Kontenplan"""
        print("🏦 Erstelle deutschen GnuCash-Kontenplan mit PROFFIX-Struktur...")
        
        # XML Root erstellen
        root = ET.Element('gnc-v2')
        self._add_namespaces(root)
        
        # Buch erstellen
        book = ET.SubElement(root, 'gnc:book', version='2.0.0')
        
        # Buch-ID
        book_id = ET.SubElement(book, 'book:id', type='guid')
        book_id.text = str(uuid.uuid4()).replace('-', '')
        
        # Währungen erstellen
        for currency in self.currencies:
            self._create_commodity(book, currency)
            
        # Stammkonto erstellen
        root_account_id = self._create_root_account(book)
        
        # Hauptkonten erstellen
        main_account_ids = {}
        for key, category in self.kontenplan.items():
            main_id = self._create_main_account(book, category['name'], 
                                              category['type'], root_account_id)
            main_account_ids[key] = main_id
            
        # Einzelkonten erstellen
        for category_key, category in self.kontenplan.items():
            parent_id = main_account_ids[category_key]
            for account_code, account_info in category['accounts'].items():
                self._create_account(book, account_code, account_info, parent_id)
                
        # Datei speichern
        self._write_xml_file(root, output_file)
        
        print(f"✅ Deutscher Kontenplan mit PROFFIX-Struktur erstellt: {output_file}")
        self._print_summary()
        
    def _add_namespaces(self, root):
        """Fügt alle GnuCash-Namespaces hinzu"""
        namespaces = {
            'xmlns:gnc': 'http://www.gnucash.org/XML/gnc',
            'xmlns:act': 'http://www.gnucash.org/XML/act', 
            'xmlns:book': 'http://www.gnucash.org/XML/book',
            'xmlns:cd': 'http://www.gnucash.org/XML/cd',
            'xmlns:cmdty': 'http://www.gnucash.org/XML/cmdty',
        }
        
        for prefix, uri in namespaces.items():
            root.set(prefix, uri)
            
    def _create_commodity(self, parent, currency_code):
        """Erstellt Währungsdefinition"""
        commodity = ET.SubElement(parent, 'gnc:commodity', version='2.0.0')
        
        space = ET.SubElement(commodity, 'cmdty:space')
        space.text = 'CURRENCY'
        
        id_elem = ET.SubElement(commodity, 'cmdty:id')
        id_elem.text = currency_code
        
        name = ET.SubElement(commodity, 'cmdty:name')
        currency_names = {
            'CHF': 'Schweizer Franken',
            'USD': 'US Dollar',
            'EUR': 'Euro'
        }
        name.text = currency_names.get(currency_code, currency_code)
        
        xcode = ET.SubElement(commodity, 'cmdty:xcode')
        xcode.text = currency_code
        
        fraction = ET.SubElement(commodity, 'cmdty:fraction')
        fraction.text = '100'
        
    def _create_root_account(self, parent):
        """Erstellt Stammkonto"""
        account = ET.SubElement(parent, 'gnc:account', version='2.0.0')
        
        name = ET.SubElement(account, 'act:name')
        name.text = 'Stammkonto'
        
        id_elem = ET.SubElement(account, 'act:id', type='guid')
        account_id = str(uuid.uuid4()).replace('-', '')
        id_elem.text = account_id
        
        type_elem = ET.SubElement(account, 'act:type')
        type_elem.text = 'ROOT'
        
        return account_id
        
    def _create_main_account(self, parent, name, account_type, parent_id):
        """Erstellt Hauptkonto (Aktiven, Passiven, etc.)"""
        account = ET.SubElement(parent, 'gnc:account', version='2.0.0')
        
        name_elem = ET.SubElement(account, 'act:name')
        name_elem.text = name
        
        id_elem = ET.SubElement(account, 'act:id', type='guid')
        account_id = str(uuid.uuid4()).replace('-', '')
        id_elem.text = account_id
        
        type_elem = ET.SubElement(account, 'act:type')
        type_elem.text = account_type
        
        commodity = ET.SubElement(account, 'act:commodity')
        space = ET.SubElement(commodity, 'cmdty:space')
        space.text = 'CURRENCY'
        id_curr = ET.SubElement(commodity, 'cmdty:id')
        id_curr.text = 'CHF'
        
        commodity_scu = ET.SubElement(account, 'act:commodity-scu')
        commodity_scu.text = '100'
        
        parent_elem = ET.SubElement(account, 'act:parent', type='guid')
        parent_elem.text = parent_id
        
        return account_id
        
    def _create_account(self, parent, account_code, account_info, parent_id):
        """Erstellt einzelnes Konto"""
        account = ET.SubElement(parent, 'gnc:account', version='2.0.0')
        
        name = ET.SubElement(account, 'act:name')
        name.text = f"{account_code} - {account_info['name']}"
        
        id_elem = ET.SubElement(account, 'act:id', type='guid')
        id_elem.text = str(uuid.uuid4()).replace('-', '')
        
        type_elem = ET.SubElement(account, 'act:type')
        type_elem.text = 'BANK'
        
        commodity = ET.SubElement(account, 'act:commodity')
        space = ET.SubElement(commodity, 'cmdty:space')
        space.text = 'CURRENCY'
        id_curr = ET.SubElement(commodity, 'cmdty:id')
        id_curr.text = account_info['currency']
        
        commodity_scu = ET.SubElement(account, 'act:commodity-scu')
        commodity_scu.text = '100'
        
        code = ET.SubElement(account, 'act:code')
        code.text = account_code
        
        description = ET.SubElement(account, 'act:description')
        description.text = f"Konto {account_code} - {account_info['name']}"
        
        parent_elem = ET.SubElement(account, 'act:parent', type='guid')
        parent_elem.text = parent_id
        
    def _write_xml_file(self, root, output_file):
        """Schreibt XML-Datei mit korrekter Formatierung"""
        xml_str = ET.tostring(root, encoding='utf-8', xml_declaration=True)
        
        with open(output_file, 'wb') as f:
            f.write(xml_str)
            
    def _print_summary(self):
        """Zeigt Zusammenfassung der erstellten Konten"""
        print(f"\n📊 KONTENPLAN-ZUSAMMENFASSUNG (PROFFIX REAL):")
        
        total_accounts = 0
        for category_key, category in self.kontenplan.items():
            count = len(category['accounts'])
            total_accounts += count
            print(f"   {category['name']}: {count} Konten")
            
        print(f"\n🎯 TOTAL: {total_accounts} Konten in {len(self.currencies)} Währungen")
        print(f"💰 Währungen: {', '.join(self.currencies)}")
        
        print(f"\n🔢 KONTONUMMERN-BEREICHE (PROFFIX STRUKTUR):")
        print(f"   1000-1999: Aktiven (32 Konten)")
        print(f"             - Flüssige Mittel: 1000, 1020, 1022, 1024, 1025...")
        print(f"             - Forderungen: 1100, 1101, 1130...")
        print(f"             - Anlagevermögen: 1400, 1510, 1520, 1600...")
        print(f"   2000-2999: Passiven (19 Konten)")
        print(f"             - Kreditoren: 2000, 2001...")
        print(f"             - Fonds: 2500, 2501, 2509, 2510, 2511...")
        print(f"             - Eigenkapital: 2800, 2900, 2990...")
        print(f"   3000-3999: Ertrag (9 Konten)")
        print(f"             - Projektspenden: 3000, 3010, 3090...")
        print(f"             - Allgemeine Spenden: 3200, 3205, 3210...")
        print(f"   4000-6999: Aufwand (35 Konten)")
        print(f"             - Projektkosten Peru: 4000, 4010, 4090...")
        print(f"             - Personalkosten: 5000, 5200...")
        print(f"             - Betriebskosten: 6000, 6100, 6200, 6510...")
        print(f"   7000+:     Sonstige & Abschlusskonten (8 Konten)")

def main():
    print("🏦 GnuCash Kontenplan Generator - PROFFIX REAL")
    print("=" * 55)
    print("📋 Basiert auf deinem echten Kontenplan CSV")
    print("🇩🇪 Alle 103 Konten mit deutschen Namen")
    print("💰 Multi-Währung: CHF, USD, EUR")
    print("✨ Exakt wie in deinem Proffix-System!")
    print("")
    
    generator = GnuCashKontenplanReal()
    
    output_file = input("📁 Output-Datei (Enter für 'kontenplan_proffix_real.gnucash'): ").strip()
    if not output_file:
        output_file = "kontenplan_proffix_real.gnucash"
        
    generator.create_gnucash_xml(output_file)
    
    print(f"\n🎉 KONTENPLAN ERSTELLT!")
    print(f"📄 Datei: {output_file}")
    print(f"🔧 Bereit für deutsche GnuCash-Version")
    print(f"📊 Alle 103 Konten aus deinem Proffix")
    print(f"\n💡 NÄCHSTE SCHRITTE:")
    print(f"   1. Öffne die Datei in GnuCash (deutsch)")
    print(f"   2. Alle Konten sind exakt wie in Proffix")
    print(f"   3. Teste mit PDF-Processor v3.0")
    print(f"\n👑 Dein PROFFIX-Kontenplan ist in GnuCash!")

if __name__ == "__main__":
    main()
