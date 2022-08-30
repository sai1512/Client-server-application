from os import listdir, path
import unittest
import uuid


from server import execute


user = [None]
username = uuid.uuid1()
password = uuid.uuid4()
execute(user, f'register {username} {password}')


class ExecutionTester(unittest.TestCase):
    def test_step1_read_write(self):
        execute(user, 'write_file saikumar.txt Hello!!Everyone.')
        output = execute(user, 'read_file saikumar.txt')
        self.assertEqual(output, 'Hello!!Everyone.')

    def test_step2_list(self):
        output = execute(user, 'list')
        self.assertEqual(output, '\n'.join(listdir(f'./users/{user[0]}')))

    def test_step3_create_folder(self):
        execute(user, 'create_folder sai_kumar')
        self.assertTrue(path.isdir(f'./users/{user[0]}/sai_kumar'))


unittest.main()
