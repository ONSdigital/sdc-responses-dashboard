Feature: Viewing figures for Survey/Collection exercise
  As a business representative
  I need to view figures for a collection exercise period
  So that I can view the figures for that period

  Background:
    Given there is at least one live collection exercise
    And the user is on the dashboard homepage
    And the user as chosen a survey

  Scenario: The user can view figures for a collection exercise period
    Given The user can see a live collection exercise
    When They click on an collection exercise period
    Then They can view report figures on that collection exercise