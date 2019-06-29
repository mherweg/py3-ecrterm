"""
Incoming Packets should be always parsable.
this test tries to look at the parser in detail.
"""
from logging import info
from unittest import TestCase, main

from ecrterm.ecr import parse_represented_data
from ecrterm.packets.base_packets import Completion, Packet


class TestParsingMechanisms(TestCase):

    def test_version_completion(self):
        # following completion is sent by the PT with version on
        # statusenquiry:
        data_expected = \
            '10 02 06 0F 0B F0 F0 F7 32 2E 31 34 2E 31 35 00 10 03 B1 11'
        # small test to test the completion with software version to be
        # recognized.
        rep = parse_represented_data(data_expected)
        self.assertEqual(rep.__class__, Completion)

    PACKET_LIST = [
        # 06 D1
        '06 D1 17 00 20 20 20 20 20 20 20 20 20 4B 61 73 73 65 6E '
        '73 63 68 6E 69 74 74',
        # 04 0F
        '04 0F 37 27 00 04 00 00 00 00 40 00 49 09 78 0C 09 38 48 '
        '0D 04 25 22 F1 F1 59 66 66 66 66 D2 00 21 22 01 00 17 00 01 87 '
        '01 75 0B 61 39 95 19 40 29 60 09 99 14 0E 05 12 8A 02',
        '06 00 63 00 00 00 FE 09 78 03 00 06 59 10 02 16 02 12 01 40 1A '
        '02 10 00 26 28 0A 02 04 0F 0A 02 06 0F 0A 02 06 1E 0A 02 04 FF '
        '0A 02 06 D8 0A 02 06 DB 0A 02 06 D9 0A 02 06 DA 0A 02 06 DD 0A '
        '02 06 D3 27 03 14 01 FF 28 10 15 02 44 45 15 02 45 4E 15 02 46 '
        '52 15 02 49 54 40 02 C0 00 1F 04 02 F1 00 1F 05 01 00',
        '06 0F 11 19 00 29 52 00 12 33 49 09 78 06 05 27 03 14 01 FF',
        '06 01 0E 02 01 04 00 00 00 00 10 00 19 44 49 09 78',
        '04 FF 1E 0A 01 06 1A 24 18 07 16 42 69 74 74 65 20 4B 61 72 74 '
        '65 20 65 69 6E 73 74 65 63 6B 65 6E',
    ]

    def test_parsing_two(self):
        """
        parse some packets
         - from the tutorial
         - from complicated scenarios
         - from failing parsings
        and tell me if they are understood:
        """
        for idx, packet in enumerate(self.PACKET_LIST):
            rep = parse_represented_data(packet)
            info(rep)
            if not isinstance(rep, Packet):
                raise AssertionError("Packet could not be parsed: #%s" % idx)

    def test_roundtrip(self):
        """
        parse packets, then serialize them again and check
        """
        for idx, packet in enumerate(self.PACKET_LIST):
            parsed = parse_represented_data(packet)
            serialized = parsed.serialize()
            self.assertEqual(str(parsed), str(parse_represented_data(serialized)),
                             "Parsed representation doesn't match serialized representation (case {})".format(idx))
            self.assertEqual(bytearray.fromhex(packet), serialized,
                             "Serialized {} message doesn't match original message (case {})".format(
                                 parsed.__class__.__name__,
                                 idx))


if __name__ == '__main__':
    main()
