# Copyright © 2018 Yang Shuai <yangshuai@gmail.com>
# This work is free. You can redistribute it and/or modify it under the
# terms of the Do What The Fuck You Want To Public License, Version 2,
# as published by Sam Hocevar. See the COPYING file for more details.

import sublime, sublime_plugin, re

def region_to_ab(region):
    return (region.a, region.b)

def ab_to_region(a, b):
    return sublime.Region(a, b)

class ColumnMassageCommand(sublime_plugin.TextCommand):
    def run(self, edit, operation=None, a_tuple=None, a_string=""):

        v = self.v = self.view
        w = self.w = v.window()
        e = self.e = edit

        self.view.run_command("split_selection_into_lines")

        if operation == None:
            w.show_input_panel("Please type the rule to modify the text", "\\t+|||((|||))|||declare @((1)) nvarchar(20) = N'((2))';", self.massage_rule_done, None, None)
        elif operation == "replace_region":
            temp_region = ab_to_region(a_tuple[0], a_tuple[1])
            v.replace(e, temp_region, a_string)


    def massage_rule_done(self, raw_rule):
        print('\n' * 10)
        v = self.view

        rule_parts = raw_rule.split("|||")
        column_delimiter = rule_parts[0]
        column_delimiter_regex = re.compile(column_delimiter)
        column_left = rule_parts[1]
        column_right = rule_parts[2]
        rule = rule_parts[3]

        print(column_left)
        print(column_right)
        print(rule)

        column_template_regex = re.compile(re.escape(column_left) + "(\d+)" + re.escape(column_right))

        unique_column_template_found = list(set(re.findall(column_template_regex, rule)))
        print(unique_column_template_found)

        for region in v.sel():
            line_regions = v.lines(region)
            for current_line_region in line_regions:
                current_line = v.substr(current_line_region).strip()
                current_line_column_list = re.split(column_delimiter_regex, current_line)
                print(current_line_column_list)

                rule_copy = rule
                for c in unique_column_template_found:
                    temp = column_left + c + column_right
                    rule_copy = rule_copy.replace(temp, current_line_column_list[int(c) - 1])

                print(current_line)
                self.view.run_command("column_massage", {"operation": "replace_region", "a_tuple": region_to_ab(current_line_region), "a_string": rule_copy})
