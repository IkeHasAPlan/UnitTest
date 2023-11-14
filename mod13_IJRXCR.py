import unittest
import SDV_inputs

class test_get_symbol(unittest.TestCase):
    def test_symbol(self):
        self.assertEqual(SDV_inputs.get_symbol("TEST"), True)
        
    def test_char_in_range(self):
        self.assertEqual(SDV_inputs.get_symbol("TOOMANYLETTERS"), False)
        
    def test_no_ints(self):
        self.assertEqual(SDV_inputs.get_symbol("G00GL"), False)
    
    def test_for_caps(self):
        self.assertEqual(SDV_inputs.get_symbol("googl"), False)
        
class test_get_chart_type(unittest.TestCase):
    def test_is_num_1_or_2(self):
        self.assertEqual(SDV_inputs.get_chart_type(1), True)
        
    def test_num_not_1_or_2(self):
        self.assertEqual(SDV_inputs.get_chart_type(3), False)
        
    def test_no_strings(self):
        self.assertEqual(SDV_inputs.get_chart_type("test"), False)
        
        
class test_get_time_series(unittest.TestCase):
    def test_is_num_1_or_2(self):
        self.assertEqual(SDV_inputs.get_time_series(1), True)
        
    def test_num_not_1_or_2(self):
        self.assertEqual(SDV_inputs.get_time_series(5), False)
        
    def test_no_strings(self):
        self.assertEqual(SDV_inputs.get_time_series("test"), False)
        
class test_get_start_date(unittest.TestCase):
    def test_year_is_not_future(self):
        self.assertEqual(SDV_inputs.get_start_date(2024,12,22), False)
        
    def test_month_is_valid(self):
        self.assertRaises(Exception, SDV_inputs.get_start_date,2022,13,22)
        
    def test_date_is_valid(self):
        self.assertRaises(Exception, SDV_inputs.get_start_date,2022,13,234)
        
    def test_date_works(self):
        self.assertEqual(SDV_inputs.get_start_date(2022,12,23), True)
        
    class test_get_end_date(unittest.TestCase):
        def test_year_is_not_future(self):
            self.assertEqual(SDV_inputs.get_end_date(2024,12,22), False)
        
        def test_month_is_valid(self):
            self.assertRaises(Exception, SDV_inputs.get_end_date,2022,13,22)
        
        def test_date_is_valid(self):
            self.assertRaises(Exception, SDV_inputs.get_end_date,2022,13,234)
        
        def test_date_works(self):
            self.assertEqual(SDV_inputs.get_end_date(2022,12,23), True)
        
    

if __name__ == '__main__':
    unittest.main()
    
