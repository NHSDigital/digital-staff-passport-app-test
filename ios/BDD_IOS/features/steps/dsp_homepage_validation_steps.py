"""Step definitions for android app poc feature"""
import logging

from behave import given, when, then
from pages.base_page import BasePage
from pages.ios_pages.dsp_org_accept_id import DspOrgAcceptID


@when("user enters the pin and click on continue")
def dsp_app_enter_pin(context):
    context.dsp_app_homepage = DspOrgAcceptID(context.driver)
    context.dsp_app_homepage.app_enter_pin()
    context.dsp_app_homepage.app_enter_pin_continue()
