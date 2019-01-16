from django.test import TestCase

# Create your tests here.

class TestHome(TestCase):
    

    def test_get_sign_up_buyer(self):
        resp = self.client.get("/accounts/signup/buyer/")
        self.assertEqual(resp.status_code, 200)
        
    def test_post_sign_up_buyer(self):
        formdata={'username':'buyer12','first_name':'buyer','last_name':'12','email':'buyer@buyer.ie','password1':'987654321z','password2':'987654321z'}
        resp = self.client.post('/accounts/signup/buyer/',formdata)
        self.assertEqual(resp.status_code, 302)    