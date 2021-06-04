"""
Common Base classes, Definitions and Ancestors.
"""

INTERMEDIATE_STATUS_CODES = {
    0x00: 'BZT wartet auf Betragbestätigung',
    0x01: 'Bitte Anzeigen auf dem PIN-Pad beachten',
    0x02: 'Bitte Anzeigen auf dem PIN-Pad beachten',
    0x03: 'Vorgang nicht möglich ',
    0x04: 'BZT wartet auf Antwort vom FEP ',
    0x05: 'BZT sendet Autostorno',
    0x06: 'BZT sendet Nachbuchungen',
    0x07: 'Karte nicht zugelassen ',
    0x08: 'Karte unbekannt / undefiniert ',
    0x09: 'Karte verfallen',
    0x0A: 'Karte einstecken',
    0x0B: 'Bitte Karte entnehmen!',
    0x0C: 'Karte nicht lesbar ',
    0x0D: 'Vorgang abgebrochen',
    0x0E: 'Vorgang wird bearbeitet bitte warten... ',
    0x0F: 'BZT leitet einen automatischen Kassenabschluss ein',
    0x10: 'Karte ungültig ',
    0x11: 'Guthabenanzeige',
    0x12: 'Systemfehler',
    0x13: 'Zahlung nicht möglich',
    0x14: 'Guthaben nicht ausreichend ',
    0x15: 'Geheimzahl falsch',
    0x16: 'Limit nicht ausreichend ',
    0x17: 'Bitte warten... ',
    0x18: 'Geheimzahl zu oft falsch ',
    0x19: 'Kartendaten falsch',
    0x1A: 'Servicemodus',
    0x1B: 'Autorisierung erfolgt. Bitte tanken ',
    0x1C: 'Zahlung erfolgt. Bitte Ware entnehmen ',
    0x1D: 'Autorisierung nicht möglich ',
    0x26: 'BZT wartet auf Eingabe der Mobilfunknummer',
    0x27: 'BZT wartet auf Wiederholung der Mobilfunknummer ',
    0x41: 'Bitte Anzeigen auf dem PIN-Pad beachten. Bitte Karte entnehmen! ',
    0x42: 'Bitte Anzeigen auf dem PIN-Pad beachten. Bitte Karte entnehmen! ',
    0x43: 'Vorgang nicht möglich. Bitte Karte entnehmen!',
    0x44: 'BZT wartet auf Antwort vom FEP. Bitte Karte entnehmen! ',
    0x45: 'BZT sendet Autostorno. Bitte Karte entnehmen! ',
    0x46: 'BZT sendet Nachbuchungen. Bitte Karte entnehmen! ',
    0x47: 'Karte nicht zugelassen. Bitte Karte entnehmen! ',
    0x48: 'Karte unbekannt / undefiniert. Bitte Karte entnehmen!',
    0x49: 'Karte verfallen. Bitte Karte entnehmen! ',
    0x4A: '',
    0x4B: 'Bitte Karte entnehmen!',
    0x4C: 'Karte nicht lesbar. Bitte Karte entnehmen! ',
    0x4D: 'Vorgang abgebrochen. Bitte Karte entnehmen! ',
    0x4E: 'Vorgang wird bearbeitet bitte warten... Bitte Karte entnehmen! ',
    0x4F: 'BZT leitet einen automatischen Kassenabschluss ein. Bitte Karte entnehmen!',
    0x50: 'Karte ungültig. Bitte Karte entnehmen!',
    0x51: 'Guthabenanzeige. Bitte Karte entnehmen! ',
    0x52: 'Systemfehler. Bitte Karte entnehmen! ',
    0x53: 'Zahlung nicht möglich. Bitte Karte entnehmen!',
    0x54: 'Guthaben nicht ausreichend. Bitte Karte entnehmen!',
    0x55: 'Geheimzahl falsch. Bitte Karte entnehmen! ',
    0x56: 'Limit nicht ausreichend. Bitte Karte entnehmen! ',
    0x57: 'Bitte warten... Bitte Karte entnehmen! ',
    0x58: 'Geheimzahl zu oft falsch. Bitte Karte entnehmen! ',
    0x59: 'Kartendaten falsch. Bitte Karte entnehmen!',
    0x5A: 'Servicemodus. Bitte Karte entnehmen! ',
    0x5B: 'Autorisierung erfolgt. Bitte tanken. Bitte Karte entnehmen! ',
    0x5C: 'Zahlung erfolgt. Bitte Ware entnehmen. Bitte Karte entnehmen!',
    0x5D: 'Autorisierung nicht möglich. Bitte Karte entnehmen! ',
    0x66: 'BZT wartet auf Eingabe der Mobilfunknummer. Bitte Karte entnehmen! ',
    0x67: 'BZT wartet auf Wiederholung der Mobilfunknummer. Bitte Karte entnehmen!',
    0xC7: 'BZT wartet auf Eingabe des Kilometerstands ',
    0xC8: 'BZT wartet auf Kassierer',
    0xC9: 'BZT leitet eine automatische Diagnose ein',
    0xCA: 'BZT leitet eine automatische Initialisierung ein',
    0xCB: 'Händlerjournal voll ',
    0xCC: 'Lastschrift nicht möglich, PIN notwendig ',
    0xD2: 'DFÜ-Verbindung wird hergestellt',
    0xD3: 'DFÜ-Verbindung besteht',
    0xE0: 'BZT wartet auf Anwendungsauswahl ',
    0xE1: 'BZT wartet auf Sprachauswahl ',
    0xF1: 'Offline ',
    0xF2: 'Online',
    0xF3: 'Offline-Transaktion',
    0xFF: 'custom or unknown status.',
}

ERRORCODES = {
    # ERRORCODES PAGE: 165
    # SUBSTITUTED: ^[A-Fa-f\d]{2,2}
    # TO: 0x\0: "
    # AND: .*$ TO: \0",
    0x00: '00 no error',
    # 01-63 01 – 99 errorcodes from network-operator
    # system/authorisation-system',
    0x64: 'card not readable (LRC-/parity-error)',
    0x65: 'card-data not present (neither track-data nor chip found)',
    0x66: 'processing-error (also for problems with card-reader mechanism)',
    0x67: 'function not permitted for ec- and Maestro-cards',
    0x68: 'function not permitted for credit- and tank-cards',
    0x6A: 'turnover-file full',
    0x6B: 'function deactivated (PT not registered)',
    0x6C: 'abort via time-out or abort-key ',
    0x6E: 'card in blocked-list (response to command 06 E4)',
    0x6F: 'wrong currency',
    0x71: 'credit not sufficient (chip-card)',
    0x72: 'chip error ',
    0x73: 'card-data incorrect (e.g. country-key check, checksum-error)',
    0x77: 'end-of-day batch not possible ',
    0x78: 'card expired',
    0x79: 'card not yet valid',
    0x7A: 'card unknown',
    0x7D: 'communication error (communication module does not answer or is '
    'not present)',
    0x83: 'function not possible',
    0x85: 'key missing',
    0x89: 'PIN-pad defective',
    0x9A: 'trnasferprotocol- error',
    0x9B: 'error from dial-up/communication fault',
    0x9C: 'please wait',
    0xA0: 'receiver not ready',
    0xA1: 'remote station does not respond',
    0xA3: 'no connection',
    0xA4: 'submission of Geldkarte not possible',
    0xB1: 'memory full',
    0xB2: 'merchant-journal full',
    0xB4: 'already reversed',
    0xB5: 'reversal not possible',
    0xB7: 'pre-authorisation incorrect (amount too high) or amount wrong',
    0xB8: 'error pre-authorisation',
    0xBF: 'voltage supply to low (external power supply)',
    0xC0: 'card locking mechanism defective',
    0xC1: 'merchant-card locked ',
    0xC2: 'diagnosis required',
    0xC3: 'maximum amount exceeded',
    0xC4: 'card-profile invalid. New card-profiles must be loaded.',
    0xC5: 'payment method not supported',
    # PAGE 166
    0xC6: 'currency not applicable',
    0xC8: 'amount zu small',
    0xC9: 'max. transaction-amount zu small',
    0xCB: 'function only allowed in EURO',
    0xCC: 'printer not ready',
    0xD2: 'function not permitted for service-cards/bank-customer-cards',
    0xDC: 'card inserted',
    0xDD: 'error during card-eject (for motor-insertion reader)',
    0xDE: 'error during card-insertion (for motor-insertion reader)',
    0xE0: 'remote-maintenance activated',
    0xE2: 'card-reader does not answer / card-reader defective',
    0xE3: 'shutter closed',
    0xE7: 'min. one goods-group not found',
    0xE8: 'no  goods-groups-table loaded',
    0xE9: 'restriction-code not permitted',
    0xEA: 'card-code not permitted (e.g. card not activated via Diagnosis)',
    0xEB: 'function not executable (PIN-algorithm unknown)',
    0xEC: 'PIN-processing not possible',
    0xED: 'PIN-pad defective',
    0xF0: 'open end-of-day batch present',
    0xF1: 'ec-cash/Maestro offline error',
    0xF5: 'OPT-error',
    0xF6: 'OPT-data not available (= OPT personalisation required)',
    0xFA: 'error transmitting offline-transactions (clearing error)',
    0xFB: 'turnover data-set defective',
    0xFC: 'necessary device not present or defective',
    0xFD: 'baudrate not supported',
    0xFE: 'register unknown',
    0xFF: 'system error'  # (= other/unknown error), See TLV tags 1F16 and 1F17
}

TERMINAL_STATUS_CODES = {
    0x00: 'PT ready',
    0x51: 'initialisation required',
    0x62: 'date/time incorrect',
    0x9C: 'please wait (e.g. software-update still running)',
    0xB1: 'memory full',
    0xB2: 'merchant-journal full',
    0xBF: 'voltage supply too low  (external power supply)',
    0xC0: 'card locking mechanism defect',
    0xC1: 'merchant card locked',
    0xC2: 'diagnosis required',
    0xC4: 'card-profile invalid. New card-profiles must be loaded',
    0xCC: 'printer not ready',
    0xDC: 'card inserted',
    0xDF: 'out-of-order',
    0xE0: 'remote-maintenance activated',
    0xE1: 'card not completely removed',
    0xE2: 'card-reader doe not answer / card-reader defective',
    0xE3: 'shutter closed',
    0xF6: 'OPT-data not availble (= OPT-Personalisation required)'}


DEBUG_PACKET_NAME = {
    (0x0F, None): 'RFU for proprietary applications, the utilisation for '
    'particular cases should be clarified between manufacturers',
    (0x01, 0x01): 'RFU',
    (0x04, 0x01): 'Set Date and Time in ECR',
    (0x04, 0x0E): 'Menu-Request',
    (0x04, 0x0F): 'Status-Information',
    (0x04, 0xFF): 'Intermediate-Statusinformation',
    (0x05, 0x01): 'Status-Enquiry',
    (0x05, 0xFF): 'RFU',
    (0x06, 0x00): 'Registration',
    (0x06, 0x01): 'Authorisation',
    (0x06, 0x02): 'Log-Off',
    (0x06, 0x03): 'Account Balance Request',
    (0x06, 0x09): 'Prepaid Top-Up',
    (0x06, 0x0A): 'Tax Free',
    (0x06, 0x0B): 'RFU',
    (0x06, 0x0C): 'TIP',
    (0x06, 0x0F): 'Completion',
    (0x06, 0x10): 'Send Turnover Totals',
    (0x06, 0x11): 'RFU',
    (0x06, 0x12): 'Print Turnover Receipts',
    (0x06, 0x18): 'Reset Terminal',
    (0x06, 0x1A): 'Print System Configuration',
    (0x06, 0x1B): 'Set/Reset Terminal-ID',
    (0x06, 0x1E): 'Abort',
    (0x06, 0x20): 'Repeat Receipt',
    (0x06, 0x21): 'Telephonic Authorisation',
    (0x06, 0x22): 'Pre-Authorisation/Reservation',
    (0x06, 0x23):
        'Partial-Reversal of a Pre-Authorisation/Booking of a Reservation',
    (0x06, 0x24): 'Book Total',
    (0x06, 0x25): 'Pre-Authorisation Reversal',
    (0x06, 0x30): 'Reversal',
    (0x06, 0x31): 'Refund',
    (0x06, 0x50): 'End-of-Day',
    (0x06, 0x51): 'Send offline Transactions',
    (0x06, 0x70): 'Diagnosis',
    (0x06, 0x79): 'Selftest',
    (0x06, 0x82): 'RFU',
    (0x06, 0x85): 'Display Text (only included for downwards-compatibility, '
    'for new implementations use 06 E0)',
    (0x06, 0x86): 'Display Text with Numerical Input (only included for '
        'downwards-compatibility, for new implementations use 06 E2)',
    (0x06, 0x87): 'PIN-Verification for Customer-Card (only included for '
    'downwards-compatibility, for new implementations use 06 E3)',
    (0x06, 0x88): 'Display Text with Function-Key Input (only included for '
        'downwards-compatibility, for new implementations use 06 E1)',
    (0x06, 0x90): 'RFU',
    (0x06, 0x91): 'Set Date and Time in PT',
    (0x06, 0x93): 'Initialisation',
    (0x06, 0x95): 'Change Password',
    (0x06, 0xB0): 'Abort',
    (0x06, 0xC0): 'Read Card',
    (0x06, 0xCE): 'RFU',
    (0x06, 0xD1): 'Print Line',
    (0x06, 0xD3): 'Print Text-Block',
    (0x06, 0xD4): 'RFU',
    (0x06, 0xD8): 'Dial-Up',
    (0x06, 0xD9): 'Transmit Data via Dial-Up',
    (0x06, 0xDA): 'Receive Data via Dial-Up ',
    (0x06, 0xDB): 'Hang-Up',
    (0x06, 0xDD): 'Transparent-Mode',
    (0x06, 0xE0): 'Display Text',
    (0x06, 0xE1): 'Display Text with Function-Key Input',
    (0x06, 0xE2): 'Display Text with Numerical Input',
    (0x06, 0xE3): 'PIN-Verification for Customer-Card',
    (0x06, 0xE4): 'Blocked-List Query to ECR',
    (0x08, 0x01): 'Activate Service-Mode',
    (0x08, 0x02): 'Switch Protocol',
    (0x08, 0x10): 'Software-Update',
    (0x08, 0x11): 'Read File',
    (0x08, 0x12): 'Delete File',
    (0x08, 0x20): 'Start OPT Action',
    (0x08, 0x21): 'Set OPT Point-in-Time',
    (0x08, 0x22): 'OPT-Pre-Initialisation',
    (0x08, 0x23): 'Output OPT-Data',
    (0x08, 0x24): 'OPT Out-of-Order',
    (0x08, 0x30): 'Select Language',
    (0x08, 0x40): 'Change Baudrate',
    (0x08, 0x50): 'Activate Card-Reader',
    (0x80, 0x00): 'Positive Acknowledgement',
    (0x84, 0x00): 'Positive Acknowledgement',
    (0x84, None): 'Negative Acknowledgement',
    (0x84, 0x9C): 'Repeat Statusinfo'
}


def noop(*args, **kwargs):
    pass


class Logling(object):
    """A simple log interface."""

    def log(self, *args, **kwargs):
        print(" ".join(args))


class Dumpling(object):
    """
    Interface, which defines that this object can
      - dump itself into a list of bytes
      - tell you how much bytes of data it has.
      - dumpling does not solve how you store your data.
    """

    def dump(self):
        """
        Returns a list of bytes, representing this dumpling in the
        stream.
        """
        return []

    def dump_length(self):
        """
        Has to return how many bytes this class does dump. Returns an
        integer.
        """
        return len(self.dump())


class Transport(Logling):
    insert_delays = False

    def connect(self, *args, **kwargs):
        """
        connect to transport.
        """

    def receive(self, timeout=None, *args, **kwargs):
        """Receive data."""

    def send(self, message, *args, **kwargs):
        """Send data."""
