import json
from django.test import TestCase
from authentication.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from note.models import Note


class TestNoteAPIs(TestCase):

    def setUp(self):
        self.client = APIClient()

        # first user
        self.user = User.objects.create_user(
            email='ninja@gmail.com',
            first_name='Moses',
            last_name='Mugoya',
            password='@rand0mPass'
        )
        
        # second user
        self.second_user = User.objects.create_user(
            email='jason@gmail.com',
            first_name='Jason',
            last_name='Derulo',
            password='@rand0mPass'
        )

        # notes
        self.note = Note.objects.create(title='Sample title', content='Sample content', owner=self.user)
        self.note2 = Note.objects.create(title='Second Sample title', content='Second Sample content', owner=self.user)

        # urls
        self.note_url = reverse('note:note-view')
        self.login_url = reverse('authentication:login')
        self.note_detail_url = reverse('note:note-detail-view', args=[self.note.id])
        self.share_note_url = reverse('note:share-note-view', args=[self.note.id, self.second_user.id])
        self.search_url = reverse('note:search-notes')


    def _login_user(self, email='ninja@gmail.com', password='@rand0mPass'):
        response = self.client.post(self.login_url, {'email': email, 'password': password}, format='json')
        return json.loads(response.content)['access']

    def _auth_headers(self, access_token):
        return {'Authorization': f'Bearer {access_token}'}


    # valid note creation
    def test_valid_note_creation(self):
        access_token = self._login_user()

        headers = self._auth_headers(access_token)
    
        note_data = {
            "title": "My title",
            "content": "my content",
        }

        response = self.client.post(self.note_url, note_data, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    # missing access token
    def test_unauthorized_note_creation(self):
        
        note_data = {
            "title": "My title",

        }

        response = self.client.post(self.note_url, note_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    

    # test missing field 
    def test_missing_field_note_creation(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)

        note_data = {
            "title": "My title"
        }

        response = self.client.post(self.note_url, note_data, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    # test listing authenticated users notes
    def test_valid_list_notes(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)

        headers = {'Authorization': f'Bearer {access_token}'}

        response = self.client.get(self.note_url, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    # test valid note update
    def test_valid_note_update(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)

        note_data = {
            "title": "My updated title",
            "content": "my updated content"
        }

        response = self.client.put(self.note_detail_url, note_data, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    

    # test invalid note update: missing fields
    def test_invalid_note_update(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)

        note_data = {
            "title": "My updated title",
        }

        response = self.client.put(self.note_detail_url, note_data, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    # test get single note
    def test_get_single_note(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)

        response = self.client.get(self.note_detail_url, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    # test delete note
    def test_delete_note(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)

        response = self.client.delete(self.note_detail_url, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    

    # test share note
    def test_share_note(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)

        response = self.client.post(self.share_note_url, format='json', headers=headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test valid search
    def test_search_notes_with_valid_query(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)
        
        query = 'sample'

        response = self.client.get(self.search_url, {'q': query}, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 


    # test invalid search
    def test_search_notes_without_query(self):
        access_token = self._login_user()
        headers = self._auth_headers(access_token)

        response = self.client.get(self.search_url, headers=headers)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)


    

   

        
    



    






    



