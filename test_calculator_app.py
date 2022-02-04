import time,pytest
import pywinauto

from .gui_auto import PyWinAuto

"""

 Basic Operational Tests
 
"""

def test_user_can_start_app():
    mgr = PyWinAuto()
    assert mgr.app.is_process_running(), "APP COULDNT START"
    mgr.close_app()


def test_user_can_close_app():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.type_keys("%{F4}")  # Alt-F4
    time.sleep(1)
    assert mgr.app.is_process_running() == False, "APP COULDNT CLOSE"


def test_user_can_press_0():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button9.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "0", "0 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_1():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button19.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "1", "1 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_2():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button18.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "2", "2 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_3():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button17.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "3", "3 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_4():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button16.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "4", "4 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_5():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button15.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "5", "5 BUTTON MISMATCH"
    mgr.close_app()

@pytest.mark.xfail(reason="fix needed. Press 6. Get 5")
def test_user_can_press_6():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button14.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "6", "6 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_7():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button13.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "7", "7 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_8():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button12.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "8", "8 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_9():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button11.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "9", "9 BUTTON MISMATCH"
    mgr.close_app()


def test_user_can_press_clear():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button4.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n"+"==== Exception error window rised ====",)
        assert False


@pytest.mark.xfail(reason="fix needed. Press delete char. Get Unhandled Exception")
def test_user_can_press_delete():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button7.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n"+"==== Exception error window rised ====",)
        assert False


@pytest.mark.xfail(reason="fix needed. Press divide. Get Unhandled Exception")
def test_user_can_press_divide():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button6.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n"+"==== Exception error window rised ====",)
        assert False


def test_user_can_press_mult():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button5.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n"+"==== Exception error window rised ====",)
        assert False


def test_user_can_press_minus():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button3.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n"+"==== Exception error window rised ====",)
        assert False
        
        
def test_user_can_press_plus():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button2.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n"+"==== Exception error window rised ====",)
        assert False
        
        
def test_user_can_press_equal():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button0.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n"+"==== Exception error window rised ====",)
        assert False


def test_user_can_press_float():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button8.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n" + "==== Exception error window rised ====", )
        assert False
        
 
@pytest.mark.xfail(reason="fix needed. Press change sign. Get Unhandled Exception")
def test_user_can_press_sign():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button10.click()
    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n" + "==== Exception error window rised ====", )
        assert False
        
        
def test_user_can_perform_clear():
    mgr = PyWinAuto()
    mgr.app.Калькулятор.Button19.click()
    mgr.app.Калькулятор.Button18.click()
    mgr.app.Калькулятор.Button17.click()
    mgr.app.Калькулятор.Button4.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "", "CLEAR NOT PERFOMED"
    mgr.close_app()


def test_user_can_delete_one_digit():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button19.click()
    mgr.app.Калькулятор.Button18.click()
    mgr.app.Калькулятор.Button17.click()

    mgr.app.Калькулятор.Button7.click()
    assert mgr.app.Калькулятор.Edit.window_text() == "12", "DELETE DIGIT NOT PERFOMED"

    mgr.close_app()

@pytest.mark.xfail
def test_user_can_perform_clear_6_times():
    mgr = PyWinAuto()
    for i in range(10):
        mgr.app.Калькулятор.Button19.click()
        mgr.app.Калькулятор.Button18.click()
        mgr.app.Калькулятор.Button17.click()
        mgr.app.Калькулятор.Button4.click()
        assert mgr.app.Калькулятор.Edit.window_text() == "", "CLEAR NOT PERFOMED"
    mgr.close_app()



"""

Functionality Test Cases

"""


def test_user_can_add_two_int():
    mgr = PyWinAuto()
    #2
    mgr.app.Калькулятор.Button18.click()
    #+
    mgr.app.Калькулятор.Button2.click()
    #2
    mgr.app.Калькулятор.Button18.click()
    #=
    mgr.app.Калькулятор.Button0.click()

    assert mgr.app.Калькулятор.Edit.window_text() == "4"

    mgr.close_app()


@pytest.mark.xfail()
def test_user_can_add_two_negative():
    mgr = PyWinAuto()
    # 8
    mgr.app.Калькулятор.Button12.click()
    #-8
    mgr.app.Калькулятор.Button10.click()
    # +
    mgr.app.Калькулятор.Button2.click()
    # 2
    mgr.app.Калькулятор.Button18.click()
    # -2
    mgr.app.Калькулятор.Button10.click()
    # =
    mgr.app.Калькулятор.Button0.click()

    assert mgr.app.Калькулятор.Edit.window_text() == "-10"

    mgr.close_app()



def test_user_can_add_pos_and_neg():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()# 8

    mgr.app.Калькулятор.Button2.click()  # +

    mgr.app.Калькулятор.Button18.click()  # 2

    mgr.app.Калькулятор.Button10.click()  # -2

    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "6"

    mgr.close_app()

@pytest.mark.xfail()
def test_user_can_sub_two_negative():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8
    mgr.app.Калькулятор.Button10.click()  # -8

    mgr.app.Калькулятор.Button3.click()  # -

    mgr.app.Калькулятор.Button18.click()  # 2
    mgr.app.Калькулятор.Button10.click()  # -2

    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "-6"

    mgr.close_app()

def test_user_can_sub_pos_and_neg():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8

    mgr.app.Калькулятор.Button3.click()  # -

    mgr.app.Калькулятор.Button18.click()  # 2
    mgr.app.Калькулятор.Button10.click()  # -2

    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "10"

    mgr.close_app()

@pytest.mark.xfail()
def test_user_can_sub_neg_and_pos():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8
    mgr.app.Калькулятор.Button10.click()  # -8

    mgr.app.Калькулятор.Button3.click()  # -

    mgr.app.Калькулятор.Button18.click()  # 2


    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "-10"

    mgr.close_app()

def test_user_can_mult_two_int():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8

    mgr.app.Калькулятор.Button5.click()  # *

    mgr.app.Калькулятор.Button18.click()  # 2

    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "16"

    mgr.close_app()


def test_user_can_mult_two_negative():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8
    mgr.app.Калькулятор.Button10.click()  # -8

    mgr.app.Калькулятор.Button5.click()  # *

    mgr.app.Калькулятор.Button18.click()  # 2
    mgr.app.Калькулятор.Button10.click()  # -2

    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "16"

    mgr.close_app()

@pytest.mark.xfail()
def test_user_can_mult_pos_and_neg():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8

    mgr.app.Калькулятор.Button5.click()  # *

    mgr.app.Калькулятор.Button18.click()  # 2
    mgr.app.Калькулятор.Button10.click()  # -2

    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "-16"

    mgr.close_app()

@pytest.mark.xfail()
def test_user_can_mult_neg_and_pos():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8
    mgr.app.Калькулятор.Button10.click()  # -8

    mgr.app.Калькулятор.Button5.click()  # *

    mgr.app.Калькулятор.Button18.click()  # 2

    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "-16"

    mgr.close_app()


def test_user_can_div_two_pos():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8

    mgr.app.Калькулятор.Button6.click()  #:

    mgr.app.Калькулятор.Button18.click()  # 2

    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "4"

    mgr.close_app()

def test_user_can_div_two_neg():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8
    mgr.app.Калькулятор.Button10.click()  # -8

    mgr.app.Калькулятор.Button6.click()  #:

    mgr.app.Калькулятор.Button18.click()  # 2
    mgr.app.Калькулятор.Button10.click()  # -2
    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "4"

    mgr.close_app()

@pytest.mark.xfail()
def test_user_can_div_pos_and_neg():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8

    mgr.app.Калькулятор.Button6.click()  #:

    mgr.app.Калькулятор.Button18.click()  # 2
    mgr.app.Калькулятор.Button10.click()  # -2
    mgr.app.Калькулятор.Button0.click()  # =

    assert mgr.app.Калькулятор.Edit.window_text() == "-4"

    mgr.close_app()

@pytest.mark.xfail
def test_user_can_div_number_by_zero_without_exception():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button12.click()  # 8

    mgr.app.Калькулятор.Button6.click()  #:

    mgr.app.Калькулятор.Button9.click()  # 0

    mgr.app.Калькулятор.Button0.click()  # =

    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n" + "==== Exception error window rised ====", )
        assert False

def test_user_can_div_zero_by_any_number_without_exceptio():
    mgr = PyWinAuto()

    mgr.app.Калькулятор.Button9.click()  # 0

    mgr.app.Калькулятор.Button6.click()  #:

    mgr.app.Калькулятор.Button12.click()  # 8

    mgr.app.Калькулятор.Button0.click()  # =

    try:
        mgr.close_app()
    except (pywinauto.findwindows.ElementAmbiguousError) as e:
        print("\n" + "==== Exception error window rised ====", )
        assert mgr.app.Калькулятор.Edit.window_text() == "0"

# TODO add tests for float numbers
# TODO add tests for input from keyboard
