Feature: Select a collection exercise
  As an business representative
  I need to view all available collection exercises
  So that I can view relevant data for that collection exercise

  Background:
    Given there is at least one live collection exercise
    And the user is on the dashboard homepage

  Scenario: The user is able to select a collection exercise
    Given The user has selected a survey
    Then They are shown at least one collection exercise