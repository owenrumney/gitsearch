from builtins import sorted

import tabulate


def display_table(data, headers):
    view_data = []
    for item in sorted(data):
        view_item = []
        for header in headers:
            view_item.append(item.get(header))
        view_data.append(view_item)

    print(tabulate.tabulate(view_data, headers, tablefmt='orgtbl'))
