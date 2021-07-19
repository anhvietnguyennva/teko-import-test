from export_test_jira.wraper import jira_test

issue = "TEST-15"
jira_link = "https://google.com"
confluence_link = "https://google.com"
folder = "Test/Import"


class TestSample:
    
    @jira_test(
        issue_links=[issue],
        name="Test case name",
        web_links=[jira_link],
        confluence_links=[confluence_link],
        folder=folder
    )
    def test_1(self, client):
        pass

    @jira_test(
        issue_links=[issue],
        name="a",
        web_links=[jira_link],
        confluence_links=[confluence_link],
        folder=folder
    )
    def test_2(self, client):
        pass

    @jira_test(
        issue_links=[issue],
        name="b",
        web_links=[jira_link],
        confluence_links=[confluence_link],
        folder=folder
    )
    def test_3(self, client):
        pass

    @jira_test(
        issue_links=[issue],
        name="d",
        web_links=[jira_link],
        confluence_links=[confluence_link],
        folder=folder
    )
    def test_4(self, client):
        pass

    @jira_test(
        issue_links=[issue],
        name="v",
        web_links=[jira_link],
        confluence_links=[confluence_link],
        folder=folder
    )
    def test_5(self, client):
        pass
