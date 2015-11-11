__author__ = 'stako'


class CommonMethods():

    def __init__(self, driver):
        self.driver = driver

    def get_value_from_select(self, web_element):
        ng_model = web_element.get_attribute("ng-model")
        list_from_ng_options = web_element.get_attribute("ng-options").split()
        index_ng_options_name = list_from_ng_options.index("as") + 1
        ng_options_name = list_from_ng_options.pop(index_ng_options_name).split('.')[1]
        index_ng_options = list_from_ng_options.index("in") + 1
        ng_options = list_from_ng_options.pop(index_ng_options)
        print ng_model
        value_from_select = self.driver.execute_script("var res; var outer_scope = angular.element(arguments[0]).scope(); ar= outer_scope." + ng_options + \
                                                      "; ar.forEach(function(obj) {if (obj.id == outer_scope." + \
                                                      ng_model + "){res = obj};}); return res." + ng_options_name,
                                                      web_element)
        return value_from_select

    def get_value_from_text_field(self, web_element):
        ng_model = web_element.get_attribute("ng-model")
        value_from_text_field = self.driver.execute_script(
            "return angular.element(arguments[0]).scope()." + str(ng_model),
            web_element)
        return value_from_text_field

    def get_value_from_web_element(self, web_element):
        if web_element.tag_name == "input":
            return self.get_value_from_text_field(web_element)
        elif web_element.tag_name == "select":
            return self.get_value_from_select(web_element)
