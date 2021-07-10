import yaml
import os


class LoaderDataCss:

    def load_css(self):
        path = os.path.dirname(__file__)
        print(f"!!!!!{__file__}")
        with open(os.path.join(path, "css_item.yaml")) as file:
            css_regular = yaml.safe_load(file)
            return css_regular
