Feature: Search Content
    As a random user
    I want to Search for tags
    To find posts related to then

    Scenario: Search for one Tag
        Given I am on Search page
        And there is on system, only 3 posts containing the tag "t1", posts "p1", "p2" and "p3"
        And i search for only for the tag "t1"
        Then only these three posts gonna be displayed on screen

    Scenario: Search for multiple Tags
        Given I am on publish page
        And the system contains only 3 posts ("p1", "p2" and "p3")
        And these three post contains respectivaly the tags ("t1" and "t2"), ("t2") and ("t1" and "t3")
        And i search for the tags "t1" and "t2"
        Then only the post "p1", who match the tags, will be displayed on screen

    Scenario: Search for unmatching Tags
        Given I am on publish page
        And the system contains only 3 posts ("p1", "p2" and "p3")
        And these three post contains respectivaly the tags ("t1" and "t2"), ("t2") and ("t1" and "t3")
        And i search for the tags "t1" and "t3"
        Then no matching post will be returned from system
        And a message about the unmatch gonna be showed
    
    Scenario: SearchBar Hints
        Given The user focus on SearchBar
        And the user has recently searched only for "comedia" and "terror"
        Then will be diplayed above the searchBar buttons with the tags "comedia" and "terror"

    Scenario: SearchBar AutoFill
        Given The user focus on SearchBar
        And the searchBar has hinted the tags "comedia" and "terror"
        And the user select "comedia"
        Then the searchBar will be overwrited by the tag "comedia"

    Scenario: Clear Hints
        Given The user focus on SearchBar
        And the searchBar has hinted the tags "comedia" and "terror"
        And the user select the buttom to clear the hints
        Then the tags "comedia" and "terror" will not be displayed anymore

        
