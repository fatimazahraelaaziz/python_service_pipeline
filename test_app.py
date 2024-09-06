import pytest
from flask_testing import TestCase
import tempfile
import os
from service_count import app, read_counter, update_counter

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False  # Disable CSRF for testing
        app.config['SECRET_KEY'] = 'test-secret-key'
        return app

    @pytest.fixture(autouse=True)
    def setup_counter_file(self):
        # Create a temporary file for testing
        self.temp_dir = tempfile.mkdtemp()
        self.temp_file = os.path.join(self.temp_dir, 'counter.txt')
        
        # Store the original COUNTER_FILE path
        self.original_counter_file = app.config['COUNTER_FILE']
        
        # Update the COUNTER_FILE path in the app
        app.config['COUNTER_FILE'] = self.temp_file
        
        yield
        
        # Clean up after the test
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)
        os.rmdir(self.temp_dir)
        
        # Restore the original COUNTER_FILE path
        app.config['COUNTER_FILE'] = self.original_counter_file

    def test_get_request(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn(b"Current POST requests count:", response.data)

    def test_post_request(self):
        initial_count = read_counter()
        response = self.client.post('/')
        self.assert200(response)
        self.assertIn(b"POST requests counter updated", response.data)
        self.assertEqual(read_counter(), initial_count + 1)

if __name__ == '__main__':
    pytest.main()