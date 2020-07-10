

class html_soup:

    def __init__(self, url):
        self.url = url

    def get_soup(self):
        """
        :param url: url address
        :return: soup of the html.
        """

        chrome_options = Options()
        chrome_options.add_argument(cfg.HEADLESS)
        # start web browser
        browser = wb.Chrome(executable_path=os.path.abspath(cfg.CHROME_DRIVER), chrome_options=chrome_options)
        # get source code
        browser.get(self.url)
        html = browser.page_source
        time.sleep(cfg.TIME_SLEEP)
        browser.close()
        return bs(html, cfg.HTML_PARSER)