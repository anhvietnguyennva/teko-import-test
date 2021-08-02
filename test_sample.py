from export_test_jira.wraper import jira_test

issue = "TEST-15"
jira_link = "https://google.com"
confluence_link = "https://google.com"
folder = "Test/Import"


class TestSample:
    
    @jira_test(
        issue_links=[issue],
        name="Return HTTP 400 when input is invalid",
        objective="Test validate input",
        precondition="No precondition",
        web_links=[jira_link],
        confluence_links=[confluence_link],
        folder=folder
    )
    def test_1(self, client):
        pass
