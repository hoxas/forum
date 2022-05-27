from tests.utils import *

from common.utils import *

# Create your tests here
"""Testing common.utils"""


class TestRequestContextGeneric(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.request = RequestFactory().get('/')
        objectCreator(cls, 'profile')
        cls.request.user = cls.user
        cls.request_context_generic = Request_Context_Generic(cls.request)

    def test_request_context_generic_properties(self):
        """Testing common.utils.Request_Context_Generic properties"""
        self.assertEqual(self.request_context_generic.request, self.request)
        self.assertEqual(self.request_context_generic.user, self.request.user)


class TestTimeDeltaNow(TestCase):
    def test_time_delta_now(self):
        """Testing common.utils.time_delta_now"""
        time_initial = timeCreator()
        with freeze_time(time_initial):
            time_delta = timeDeltaNow(time_initial)
            self.assertEqual(time_delta[0],  0)
            self.assertEqual(time_delta[1], 0)

        time_minute = timeCreator('1m')
        with freeze_time(time_minute):
            time_delta = timeDeltaNow(time_initial)
            self.assertEqual(time_delta[0], 1)
            self.assertEqual(time_delta[1], 0)

        time_hour = timeCreator('1h')
        with freeze_time(time_hour):
            time_delta = timeDeltaNow(time_initial)
            self.assertEqual(time_delta[0], 60)
            self.assertEqual(time_delta[1], 0)


class TestTimeHuman(TestCase):
    def test_time_human(self):
        """Testing common.utils.time_human"""
        minutes_in_hour = 60
        minutes_in_day = 24 * minutes_in_hour
        minutes_in_year = 365 * minutes_in_day

        self.assertEqual(timeHuman((0, 0)), 'less than a minute ago')
        self.assertEqual(timeHuman((1, 0)), '1 minutes ago')
        self.assertEqual(timeHuman((minutes_in_hour, 0)), '1 hours ago')
        self.assertEqual(timeHuman((minutes_in_day, 0)), '1 days ago')
        self.assertEqual(timeHuman((minutes_in_year, 0)), '1 years ago')
