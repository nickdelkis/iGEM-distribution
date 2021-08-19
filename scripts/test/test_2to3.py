import unittest

import sbol3

import scripts.scriptutils


class Test2To3Conversion(unittest.TestCase):

    def test_convert_identities(self):
        with open('testfiles/sbol3-small-molecule.rdf') as fp:
            rdf_data = fp.read()
        rdf_data = scripts.scriptutils.convert_identities2to3(rdf_data)
        self.assertIsNotNone(rdf_data)
        doc = sbol3.Document()
        doc.read_string(rdf_data, sbol3.RDF_XML)
        # Expecting 8 top level objects, 4 Components and 4 Sequences
        self.assertEqual(8, len(doc.objects))


if __name__ == '__main__':
    unittest.main()
