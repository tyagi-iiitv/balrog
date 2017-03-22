import auslib.admin.views.validator

def testNewRulePostValidate():
    data=dict(backgroundRate=31, mapping='c', priority=33, product='Firefox', update_type='minor', channel='nightly')
    auslib.admin.views.validator.validate_rule(data)
