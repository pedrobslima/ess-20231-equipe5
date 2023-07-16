Feature: Search Content
    As a random user
    I want to Search for tags
    To find posts related to then

    Scenario: Search for one Tag
        Given I am on Search page
        And there is on system, only 3 posts containing the tag "t1", posts "p1", "p2" and "p3"
        And i search for only for the tag "t1"
        Then only these three posts gonna be returned from system
        And they three will be displayed on screen

    Scenario: Search for multiple Tags
        Given I am on publish page
        And the system contains only 3 posts ("p1", "p2" and "p3")
        And these three post contains respectivaly the tags ("t1" and "t2"), ("t2") and ("t1" and "t3")
        And i search for the tags "t1" and "t2"
        Then only the post "p1" will match both tags so will be returned from system
        And only the post "p1" will be displayed on screen

    
    Scenario: Search for unmatching Tags
        Given I am on publish page
        And the system contains only 3 posts ("p1", "p2" and "p3")
        And these three post contains respectivaly the tags ("t1" and "t2"), ("t2") and ("t1" and "t3")
        And i search for the tags "t1" and "t3"
        Then no matching post will be returned from system
        And a message about the unmatch gonna be showed
