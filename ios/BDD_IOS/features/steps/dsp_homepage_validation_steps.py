"""Step definitions for the homepage"""

from behave import when
from pages.ios_pages.dsp_org_accept_id import DspOrgAcceptID


@when("user enters the pin and click on continue")
def dsp_app_enter_pin(context):
    """Step enters the pin and click on continue"""
    context.dsp_app_homepage = DspOrgAcceptID(context.driver)
    context.dsp_app_homepage.app_enter_pin()
    context.dsp_app_homepage.app_enter_pin_continue()
