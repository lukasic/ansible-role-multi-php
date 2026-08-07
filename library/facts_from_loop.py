#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            results=dict(type='list', required=True),
            name_template=dict(type='str', required=True),
            expr=dict(type='str', required=True),
        )
    )

    results = module.params['results']
    name_template = module.params['name_template']
    expr = module.params['expr']

    facts = {}

    for result in results:
        item = result.get('item')
        try:
            fact_name = name_template.format(item=item)
        except Exception as e:
            module.fail_json(msg="Error during evaluation of name_template: %s" % str(e))

        try:
            value = eval(expr, {"__builtins__": {}}, {"item": item, "result": result})
        except Exception as e:
            module.fail_json(msg="Error during eval() expr for item=%s: %s" % (item, str(e)))

        facts[fact_name] = value

    module.exit_json(changed=False, ansible_facts=facts)


if __name__ == '__main__':
    main()
