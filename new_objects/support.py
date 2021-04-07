


class OsDownloadsFolderError(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt




class DownloadPending:
    # todo: consider using DownloadPending object under certain conditions ... if you need expect full download or rename the file
    # ... root downloads folder should be "/downloads"
    def __init__(self, driver, timeout: int, rename: bool):
        self.driver = driver
        self._check_download(timeout)
        self._rename_download_file(rename)

    def _check_download(self, timeout):
        import time
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.common.exceptions import JavascriptException, InvalidArgumentException, TimeoutException
        try:
            time.sleep(timeout)
            if not self.driver.current_url.startswith("chrome://downloads"):
                self.driver.get("chrome://downloads/")
                wait = WebDriverWait(self.driver, timeout)
                wait.until(lambda tab: tab.current_url.startswith("chrome://downloads"))
                self.driver.set_page_load_timeout(timeout)
                return self.driver.execute_script("""   
                                                    var items = downloads.Manager.get().items_; 
                                                    if (items.every(e => e.state === "COMPLETE")) 
                                                    return items.map(e => e.fileUrl || e.file_url);
                                                    """)
        except TimeoutException:
            return True
        except JavascriptException:
            return False
        except InvalidArgumentException as er:
            return f'{er} ... any browser other than "Chrome" does not work with this method!'
        finally:
            time.sleep(timeout)

    #  file is stored in the working directory
    def _rename_download_file(self, rename: bool):
        import os
        import pathlib
        from datetime import datetime
        from selenium.common.exceptions import InvalidArgumentException
        try:
            if self.driver.current_url.startswith("chrome://downloads") and rename:
                file_name_download = self.driver.execute_script("""return document.querySelector("body > downloads-manager")
                .shadowRoot.querySelector("#frb0").shadowRoot.querySelector("#name").innerText;""")
                file = os.path.join(os.path.expanduser('~') + "/Downloads/" + str(file_name_download))  # check name folder if you have a different name - change
                #file = os.path.join("/dev/shm/" + str(file_name_download))  # if run docker-selenium
                serial_number = datetime.now().strftime("%H_%M")
                while os.path.isfile(file):
                    if not os.path.isfile(file):
                        raise ValueError(f"{str(file_name_download)} isn't a file!")
                    else:
                        x = str(file_name_download)
                        search = x.rfind('.')
                        file_extension = x[int(search):]
                        os.rename(file, f"new_file_{str(serial_number)}{str(file_extension)}")
                        try:
                            if not pathlib.Path(f"new_file_{str(serial_number)}{str(file_extension)}").absolute():
                                raise OsDownloadsFolderError("... root downloads folder should be name: \"Downloads\"!")
                        except OsDownloadsFolderError as er:
                            return f'Error directory {er}'
                        break
            self.driver.back()
            self.driver.refresh()
        except InvalidArgumentException as er:
            return f'{er} ... any browser other than "Chrome" does not work with this method!'


