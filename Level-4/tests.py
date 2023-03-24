import unittest
import code as c

class TestTaxPayer(unittest.TestCase): 
  
    # tests for correct retrieval of stock info given a symbol
    def test_1(self):
        op = c.DB_CRUD_ops()
        expected_output = "[METHOD EXECUTED] get_stock_info\n[QUERY] SELECT * FROM stocks WHERE symbol = 'MSFT'\n[RESULT] ('2022-01-06', 'MSFT', 300.0)"
        actual_output = op.get_stock_info('MSFT')
        self.assertEqual(actual_output, expected_output)

    # tests for correct defense against SQLi in the case where a user passes more than one query or restricted characters
    def test_2(self):
        op = c.DB_CRUD_ops()
        expected_output = "[METHOD EXECUTED] get_stock_info\n[QUERY] SELECT * FROM stocks WHERE symbol = 'MSFT'; UPDATE stocks SET price = '500' WHERE symbol = 'MSFT'--'\nCONFIRM THAT THE ABOVE QUERY IS NOT MALICIOUS TO EXECUTE"
        actual_output = op.get_stock_info("MSFT'; UPDATE stocks SET price = '500' WHERE symbol = 'MSFT'--")
        self.assertEqual(actual_output, expected_output)

    # tests for correct retrieval of stock price
    def test_3(self):
        op = c.DB_CRUD_ops()
        expected_output = "[METHOD EXECUTED] get_stock_price\n[QUERY] SELECT price FROM stocks WHERE symbol = 'MSFT'\n[RESULT] (300.0,)\n"
        actual_output = op.get_stock_price('MSFT')
        self.assertEqual(actual_output, expected_output)

    # tests for correct update of stock price given symbol and updated price
    def test_4(self):
        op = c.DB_CRUD_ops()
        expected_output = "[METHOD EXECUTED] update_stock_price\n[QUERY] UPDATE stocks SET price = '300' WHERE symbol = 'MSFT'\n"
        actual_output = op.update_stock_price('MSFT', 300.0)
        self.assertEqual(actual_output, expected_output)
    
        
if __name__ == '__main__':    
    unittest.main()