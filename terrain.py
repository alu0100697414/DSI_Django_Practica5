from django.core.management import call_command
from django.test.simple import DjangoTestSuiteRunner
 
from lettuce import before, after, world

@step(u'I am at "([^"]*)"')
def i_am_at_url(step, url):
    world.browser.get(url)
