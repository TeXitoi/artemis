from artemis.test_mechanism import ArtemisTestFixture, dataset, DataSet
import pytest
xfail = pytest.mark.xfail

@dataset([DataSet("map")])
class TestMap(ArtemisTestFixture):
    """
    test walk transfert
    """

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1132", raises=AssertionError)
    def test_map_01(self):
        """
        test walk journey
        """
        self.journey(_from="stop_area:MAP:SA:1",
                     to="stop_area:MAP:SA:2",
                     datetime="20041210T070000")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1132", raises=AssertionError)
    def test_map_02(self):
        """
        test walk transfert at start
        """
        self.journey(_from="stop_area:MAP:SA:1",
                     to="stop_area:MAP:SA:3",
                     datetime="20041210T070000")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1132", raises=AssertionError)
    def test_map_03(self):
        """
        test walk transfert at start, at end
        """
        self.journey(_from="stop_area:MAP:SA:1",
                     to="stop_area:MAP:SA:4",
                     datetime="20041210T070000")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1132", raises=AssertionError)
    def test_map_04(self):
        """
        test walk transfert at start, in the middle
        """
        self.journey(_from="stop_area:MAP:SA:1",
                     to="stop_area:MAP:SA:5",
                     datetime="20041210T070000")

    @xfail(reason="http://jira.canaltp.fr/browse/NAVITIAII-1132", raises=AssertionError)
    def test_map_05(self):
        """
        test walk transfert at end
        """
        self.journey(_from="stop_area:MAP:SA:2",
                     to="stop_area:MAP:SA:4",
                     datetime="20041210T070000")

    def test_map_06(self):
        """
        test walk transfert in the middle
        """
        self.journey(_from="stop_area:MAP:SA:2",
                     to="stop_area:MAP:SA:5",
                     datetime="20041210T070000")

