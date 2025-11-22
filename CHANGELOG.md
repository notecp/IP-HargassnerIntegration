# Changelog

Alle wichtigen Änderungen an diesem Projekt werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/lang/de/).

## [Unreleased]

## [0.1.0] - 2025-11-22

### ✨ Added

Erste Release-Kandidat Version der Bauergroup Hargassner Integration.

- **Thread-safe Telnet Client** mit Auto-Reconnect
  - Exponential backoff (5s → 300s)
  - Multi-Encoding Support (UTF-8, Latin-1, CP1252)
  - Background asyncio task für kontinuierlichen Empfang
- **Config Flow** für GUI-basierte Konfiguration
  - Connection validation
  - Firmware-Auswahl (V14_1HAR_q1)
  - Sprach-Auswahl (EN/DE)
  - Sensor-Set Auswahl (STANDARD/FULL)
- **Data Update Coordinator** für effizienten Datenabruf
- **138 Parameter vollständig dokumentiert**
  - Alle Heizkreise (A, 1-6)
  - Alle Warmwasser-Kreise (A, 1-3)
  - Lambda-Sonde Parameter
  - Motor-Ströme
  - Buffer-Sensoren
  - Kategorisiert und strukturiert
- **15+ Standard-Sensoren**, 30+ im Full-Modus
  - Boiler State, Temperature, Power
  - Buffer Temperatures
  - Energy Dashboard Integration (kWh)
  - Error Handling
- **DAQ-Parser Tool** (`tools/daq_parser.py`)
  - Extrahiert Firmware-Templates aus SD-Karten DAQ-Dateien
  - Unterstützt JSON, Python und Text-Ausgabe
  - Erleichtert Hinzufügen neuer Firmware-Versionen
- **Umfassende Dokumentation**
  - ARCHITECTURE.md (Technische Architektur)
  - INSTALLATION.md (Installationsanleitung)
  - DEVELOPMENT.md (Entwickler-Leitfaden)
  - CONTRIBUTING.md (Beitrags-Richtlinien)
  - VERSIONING.md (Semantic Versioning Guidelines)
  - COMMIT_GUIDELINES.md (Conventional Commits Standard)
- **Übersetzungen** (Englisch, Deutsch)
- **Firmware Support**
  - V14_1HAR_q1 vollständig unterstützt

### 🔧 Technical

- Async/await Architektur durchgängig
- Type hints 100%
- Moderne Home Assistant Best Practices
- Saubere Code-Struktur mit src/-Verzeichnis
- Error Handling auf allen Ebenen
- Thread-safe Data Access mit asyncio.Lock

---

## Links

- [VERSIONING.md](VERSIONING.md) - Semantic Versioning Guidelines
- [COMMIT_GUIDELINES.md](COMMIT_GUIDELINES.md) - Commit Message Standard
- [README.md](README.md) - Projekt-Übersicht
- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) - Technische Architektur
