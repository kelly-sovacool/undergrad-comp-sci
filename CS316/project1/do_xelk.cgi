#!/usr/bin/python3
"""Xelkalai Conversion Common Gateway Interface
Author: Kelly Sovacool
Email: kellysovacool@uky.edu
Date: 20 Sept. 2017
"""
import abc
import cgi
import collections


def main():
    form = cgi.FieldStorage()
    parameters = collections.OrderedDict()  # maintains key-value pairs in original order
    parameters['origunits'] = StringParameter('origunits', "Original Units", form)
    parameters['convunits'] = StringParameter('convunits', "New Units", form, original_units=parameters["origunits"].value)
    parameters['numunits'] = FloatParameter('numunits', "Value to Convert", form)
    parameters['convfactor'] = FloatParameter('convfactor', "Conversion Factor", form)
    html = "Content-type: text/html\n\n<html lang=\"en\"\n<head>\n<title>Xelk</title>\n<style type=\"text/css\">\n#errors {\n\tcolor: red;\n\tfont-style: normal;\n\tfont-weight: bold;\n\tfont-size: 2em;\n\t}\n#result {\n\tcolor: green;\n\tfont-style: normal;\n\tfont-size: 2em;\n\t}\n"
    param_style = ""
    param_body = ""
    param_errors = ""

    for description, parameter in parameters.items():
        param_errors += parameter.error_html
        param_style += parameter.style_html
        param_body += parameter.body_html

    html += param_style + "</style>\n</head>\n<body>\n" + param_body + param_errors
    if not param_errors:
        result = parameters['convfactor'].value * parameters['numunits'].value * Parameter.conversions[parameters["origunits"].value][parameters['convunits'].value]
        html += "<h3 id=\"result\">Result: {}</h3>\n".format(result)
    html += "</body>\n</html>\n"
    print(html)


def remove_type_str_brackets(type_variable):
    """ Return the string representation of variable's type without angle brackets for compatibility with HTML."""
    return str(type_variable)[8:-2]


class Parameter(metaclass=abc.ABCMeta):
    """ Manage an HTML parameter's name, value, and type."""
    conversions = {'parsec': {'lightyear': 3.26, 'parsec': 1, 'xlarn': 1/7.3672},
                   'lightyear': {'kilometers': 3.086*10**13, 'parsec': 1/3.26, 'lightyear': 1},
                   'kilometers': {'lightyear': 1/(3.086*10**13), 'kilometers': 1},
                   'xlarn': {'parsec': 7.3672, 'xlarn': 1},
                   'galacticyear': {'terrestrialyear': 250000000, 'galacticyear': 1},
                   'xarnyear': {'terrestrialyear': 1.2579, 'xarnyear': 1},
                   'terrestrialyear': {'terrestrialminute': 525600, 'galacticyear': 1/250000000, 'terrestrialyear': 1, 'xarnyear': 1/1.2579},
                   'terrestrialminute': {'terrestrialyear': 1/525600, 'terrestrialminute': 1}}

    @abc.abstractmethod
    def __init__(self, name, description, form, expected_type):
        self.name = name
        self.description = description
        self.expected_type = expected_type
        try:
            input_value = form.getvalue(name)
        except KeyError:  # if input name is not in the form, parameter value is None
            input_value = None
        self.value = input_value
        self.error_message = ""

    @property
    def is_valid_type(self):
        return type(self.value) == self.expected_type

    @property
    def color(self):
        return "red" if self.error_message else "blue"

    @property
    def error_html(self):
        return "<h2 id=\"errors\">Error: {}</h2>\n".format(self.error_message) if self.error_message else ""

    @property
    def style_html(self):
        return "#" + self.name + " {\n\tcolor: " + self.color + ";\n\tfont-style: normal;\n\t}\n"

    @property
    def body_html(self):
        return "<h1 id=\"{}\">{}: {}</h1>\n".format(self.name, self.description, self.value)


class StringParameter(Parameter):
    """ For string parameters such as Original Units and New Units """
    def __init__(self, name, description, form, original_units=None):
        super().__init__(name, description, form, str)
        if not self.value:
            self.error_message = "{} is missing".format(self.description)
        elif not self.is_valid_type:
            self.error_message = "{} given as {} but needed {}.".format(self.description, remove_type_str_brackets(type(self.value)), remove_type_str_brackets(self.expected_type))
        else:
            self.value = self.value.lower().strip()
            if self.value not in Parameter.conversions:
                self.error_message = "{} conversion not supported".format(self.value)
            elif original_units in Parameter.conversions and self.value not in Parameter.conversions[original_units]:
                self.error_message = "{} conversion not supported by original units".format(self.value)


class FloatParameter(Parameter):
    """ For float parameters such as Conversion Value and Conversion Factor """
    def __init__(self, name, description, form):
        super().__init__(name, description, form, float)
        try:
            self.value = float(self.value)
        except ValueError:
            self.error_message = "{} is not a floating-point number".format(self.value)
        except TypeError:
            self.error_message = "{} is missing".format(self.description)
        else:
            self.error_message = "{} {} is less than or equal to zero".format(self.description, self.value) if self.value <= 0 else ""


if __name__ == "__main__":
    main()
