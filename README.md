# 🌐 IP Address Finder

Un'applicazione desktop moderna e intuitiva per trovare e gestire i tuoi indirizzi IP pubblici e locali, con funzionalità avanzate di geolocalizzazione e sistema integrato.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Caratteristiche Principali

### 🔍 **Rilevamento IP Avanzato**
- **IP Pubblico**: Rileva automaticamente il tuo indirizzo IP pubblico utilizzando servizi multipli per garantire affidabilità
- **IP Locale**: Mostra istantaneamente il tuo indirizzo IP locale nella rete domestica/aziendale
- **Backup Multi-servizio**: Sistema di fallback che utilizza diversi provider (ipify.org, httpbin.org, myip.com)

### 🌍 **Geolocalizzazione Intelligente**
- **Informazioni Geografiche**: Ottieni dettagli completi sulla posizione del tuo IP pubblico
- **Dati ISP**: Visualizza informazioni sul provider di servizi internet
- **Coordiniate GPS**: Coordinate precise di latitudine e longitudine
- **Timezone**: Fuso orario associato alla tua posizione

### 🖥️ **Interfaccia Moderna**
- **Design Dark Theme**: Interfaccia elegante con tema scuro moderno
- **Responsive UI**: Layout ottimizzato per una migliore esperienza utente
- **Animazioni Hover**: Effetti interattivi sui pulsanti e elementi
- **Codice Colori Semantico**: Colori distintivi per successo, errore e informazioni

### 📋 **Gestione Clipboard**
- **Copia Rapida**: Copia istantaneamente gli indirizzi IP negli appunti
- **Feedback Visivo**: Conferme immediate delle operazioni di copia
- **Compatibilità Cross-platform**: Supporto clipboard per tutti i sistemi operativi

## 🚀 Installazione e Avvio

### Metodo 1: Avvio Automatico (Consigliato)
```bash
# Windows
start.bat

# Linux/macOS
python start.py
```

### Metodo 2: Installazione Manuale
```bash
# 1. Installa le dipendenze
pip install -r requirements.txt

# 2. Avvia l'applicazione
python main.py
```

## 📁 Struttura del Progetto

```
ip-address-finder/
├── 📄 main.py              # Applicazione principale con GUI
├── 🚀 start.py             # Script di avvio automatico
├── 💾 start.bat            # Launcher per Windows
├── 📋 requirements.txt     # Dipendenze Python
├── 📖 README.md            # Documentazione del progetto
└── 🖼️ ico/                 # Directory per icone (opzionale)
    └── app_icon.ico        # Icona dell'applicazione
```

## 🔧 Descrizione dei File

### `main.py` - 🎯 **Core Application**
Il cuore dell'applicazione che contiene:

- **`AdvancedIPFinder`**: Classe principale che gestisce l'intera interfaccia utente
- **GUI Components**: Interfaccia grafica costruita con Tkinter
- **IP Detection**: Logica per il rilevamento di IP pubblici e locali
- **Network Services**: Integrazione con servizi web per IP e geolocalizzazione
- **Clipboard Management**: Gestione della copia negli appunti
- **Threading**: Operazioni asincrone per non bloccare l'interfaccia

**Caratteristiche tecniche:**
- 🎨 **Design System**: Schema colori coerente e moderno
- 🔄 **Multi-threading**: Richieste di rete non bloccanti
- 🛡️ **Error Handling**: Gestione robusta degli errori di rete
- 📱 **Responsive Layout**: Interfaccia adattiva e centrata

### `start.py` - ⚡ **Smart Launcher**
Sistema di avvio intelligente che include:

- **Dependency Checker**: Verifica automatica delle dipendenze Python
- **Auto-installer**: Installazione automatica dei pacchetti mancanti
- **Environment Validation**: Controllo dell'ambiente di esecuzione
- **Colored Output**: Output colorato per una migliore user experience
- **Error Recovery**: Gestione intelligente degli errori di installazione

**Funzionalità:**
- ✅ **Auto-setup**: Configura automaticamente l'ambiente
- 🔍 **Smart Detection**: Rileva Python e le librerie necessarie
- 🎨 **Colored CLI**: Interface a linea di comando colorata
- ⏱️ **Timeout Handling**: Gestione dei timeout di installazione

### `start.bat` - 🏁 **Windows Quick Launcher**
Launcher semplificato per utenti Windows:
- Avvio con doppio click
- Titolo personalizzato della finestra
- Pausa finale per visualizzare eventuali errori

### `requirements.txt` - 📦 **Dependencies**
Lista delle dipendenze essenziali:
- **`requests`**: Per le chiamate HTTP ai servizi di rilevamento IP
- **`pyperclip`**: Per la gestione avanzata degli appunti cross-platform

## 🎮 Come Utilizzare

### 1️⃣ **Ottenere l'IP Pubblico**
1. Clicca sul pulsante **"🔍 Ottieni IP Pubblico"**
2. Attendi il caricamento (indicatore di progresso)
3. Visualizza il risultato con opzioni aggiuntive

### 2️⃣ **Visualizzare l'IP Locale**
- L'IP locale viene mostrato automaticamente all'avvio
- Utilizza il pulsante **"📋 Copia"** per copiarlo

### 3️⃣ **Esplorare le Informazioni Geografiche**
1. Dopo aver ottenuto l'IP pubblico, clicca **"🌍 Info Geo"**
2. Visualizza dettagli completi su:
   - 🌍 Paese e città
   - 📍 Regione e coordinate
   - 🌐 Provider internet (ISP)
   - 🕐 Fuso orario

### 4️⃣ **Copiare negli Appunti**
- Utilizza i pulsanti **"📋 Copia"** per copiare rapidamente gli IP
- Ricevi conferma immediata dell'operazione

## 🛠️ Requisiti di Sistema

### **Software Requirements**
- **Python**: 3.7 o superiore
- **Sistema Operativo**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Connessione Internet**: Necessaria per il rilevamento IP pubblico

### **Hardware Requirements**
- **RAM**: Minimo 512 MB disponibili
- **Storage**: 50 MB di spazio libero
- **Display**: Risoluzione minima 800x600

## 🔒 Privacy e Sicurezza

### **Protezione dei Dati**
- ✅ **No Data Storage**: Nessun dato viene salvato localmente
- ✅ **No Tracking**: Non vengono tracciati comportamenti o preferenze
- ✅ **HTTPS Only**: Tutte le comunicazioni utilizzano protocolli sicuri
- ✅ **Local Processing**: Elaborazione completamente locale dei dati

### **Servizi Utilizzati**
I seguenti servizi esterni vengono utilizzati esclusivamente per il rilevamento IP:
- 🔗 **ipify.org**: Servizio principale per IP pubblico
- 🔗 **httpbin.org**: Servizio di backup
- 🔗 **myip.com**: Servizio alternativo
- 🔗 **ip-api.com**: Per informazioni di geolocalizzazione

## 🐛 Troubleshooting

### **Problemi Comuni e Soluzioni**

#### ❌ **"Errore nel recuperare l'IP pubblico"**
**Possibili cause:**
- Connessione internet assente o instabile
- Firewall che blocca le richieste HTTP
- Servizi di rilevamento IP temporaneamente non disponibili

**Soluzioni:**
1. Verifica la connessione internet
2. Riprova dopo alcuni secondi
3. Controlla le impostazioni del firewall

#### ❌ **"IP locale non disponibile"**
**Possibili cause:**
- Problemi di configurazione di rete
- Interfacce di rete disabilitate

**Soluzioni:**
1. Riavvia l'applicazione
2. Controlla le connessioni di rete attive
3. Riavvia l'adattatore di rete se necessario

#### ❌ **"Impossibile ottenere informazioni di geolocalizzazione"**
**Possibili cause:**
- IP pubblico non valido
- Servizio di geolocalizzazione non disponibile
- Restrizioni di rete aziendali

**Soluzioni:**
1. Verifica di avere un IP pubblico valido
2. Riprova dopo alcuni minuti
3. Contatta l'amministratore di rete se in ambiente aziendale

## 📈 Roadmap e Sviluppi Futuri

### **Versione 2.0 - Pianificata**
- 🌐 **Multi-language Support**: Supporto per inglese e altre lingue
- 📊 **Network Monitoring**: Monitoraggio continuo della connessione
- 🕐 **History Tracking**: Cronologia degli IP rilevati
- 🔄 **Auto-refresh**: Aggiornamento automatico periodico
- 📱 **Mobile Version**: Versione per dispositivi mobili

### **Versione 2.5 - In Valutazione**
- 🛡️ **VPN Detection**: Rilevamento connessioni VPN/Proxy
- 🌍 **Extended Geo Info**: Informazioni geografiche estese
- 📧 **Export Features**: Esportazione dati in vari formati
- 🎨 **Theme Customization**: Personalizzazione temi e colori

## 👨‍💻 Informazioni Sviluppatore

**Sviluppato da**: EventExecutor  
**Anno**: 2024  
**Versione Corrente**: 1.0  

### **Contatti e Supporto**
Per bug report, richieste di funzionalità o supporto generale, apri una issue nel repository del progetto.

---

## 📜 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per i dettagli completi.

---

<div align="center">

**🌟 Se questo progetto ti è stato utile, considera di lasciare una stella! 🌟**

**Fatto con ❤️ e Python**

</div>
