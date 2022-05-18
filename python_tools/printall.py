import win32api
import win32print


def printer_loading(filenames):
    open(filenames, "r")
    win32api.ShellExecute(
        0,
        "print",
        filenames,
        #
        # If this is None, the default printer will
        # be used anyway.
        #
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
    # 调用默认打印机
