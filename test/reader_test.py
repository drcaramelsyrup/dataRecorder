import unittest
from ..src import reader_handler


class TestReaderFunctions(unittest.TestCase):

	def setUp(self):
		self.reader = reader_handler.ReaderHandler(10)

	def test_readDataReturnsNumberSpaceNumberEOL(self):
		self.assertEqual(self.reader.readData(), "1 1\n\r")

	def test_readDataReturnsNumberSpaceNumberSpaceNumberEOL(self):
		self.assertEqual(self.reader.readData(), "2 67.3 8\n\r")


if __name__ == '__main__':
	unittest.main()