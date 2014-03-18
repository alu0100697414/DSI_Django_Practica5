# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Given I am at "([^"]*)"')
def given_i_am_at_group1(step, group1):
    assert False, 'This step must be implemented'

@step(u'Then I should see "([^"]*)"')
def then_i_should_see_group1(step, group1):
    assert False, 'This step must be implemented'
