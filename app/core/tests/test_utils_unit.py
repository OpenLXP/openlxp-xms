import logging
from unittest.mock import patch

from django.test import TestCase, tag

from core.management.utils.notification import (check_if_email_verified,
                                                send_notifications)
from core.management.utils.xms_internal import send_log_email
from core.models import ReceiverEmailConfiguration, SenderEmailConfiguration

logger = logging.getLogger('dict_config_logger')


@tag('unit')
class UtilsTests(TestCase):
    """Unit Test cases for utils """

    # Test cases for NOTIFICATION
    def test_send_notifications(self):
        """Test for function to send emails of log file to personas"""
        with patch('core.management.utils.notification'
                   '.EmailMessage') as mock_send, \
                patch('core.management.utils.notification'
                      '.boto3.client'):
            self.receive_email_list = ['receiver1@openlxp.com',
                                       'receiver1@openlxp.com']
            self.sender_email = "sender@openlxp.com"

            send_notifications(self.receive_email_list, self.sender_email)
            self.assertEqual(mock_send.call_count, 2)

    # Test cases for xds_internal

    def test_send_log_email(self):
        """Test for function to send emails of log file to personas"""
        with patch('core.management.utils.xms_internal'
                   '.ReceiverEmailConfiguration') as receive_email_cfg, \
                patch('core.management.utils.xms_internal'
                      '.SenderEmailConfiguration') as sender_email_cfg, \
                patch('core.management.utils.xms_internal'
                      '.send_notifications', return_value=None
                      ) as mock_send_notification:

            self.receive_email_list = ['receiver1@openlxp.com',
                                       'receiver1@openlxp.com']
            self.sender_email = "sender@openlxp.com"
            self.message = 'Test message'

            receive_email = ReceiverEmailConfiguration(
                email_address=self.receive_email_list)
            receive_email_cfg.first.return_value = receive_email

            send_email = SenderEmailConfiguration(
                sender_email_address=self.sender_email)
            sender_email_cfg.first.return_value = send_email
            send_log_email(self.message)
            self.assertEqual(mock_send_notification.call_count, 1)

    def test_check_if_email_verified(self):
        """Test to check if email id from user is verified """
        receive_email_list = ['receiver1@openlxp.com',
                              'receiver1@openlxp.com']
        with patch('core.management.utils.notification'
                   '.list_email_verified') as mock_list:
            mock_list.return_value = receive_email_list
            email_value = 'receiver1@openlxp.com'
            return_val = check_if_email_verified(email_value)
            self.assertFalse(return_val)

    def test_check_if_email_not_verified(self):
        """Test to check if email id from user is verified """
        receive_email_list = ['receiver1@openlxp.com',
                              'receiver1@openlxp.com']
        with patch('core.management.utils.notification'
                   '.list_email_verified') as mock_list:
            mock_list.return_value = receive_email_list
            email_value = 'receiver2@openlxp.com'
            return_val = check_if_email_verified(email_value)
            self.assertTrue(return_val)
