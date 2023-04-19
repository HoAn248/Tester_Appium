from appium import webdriver
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from termcolor import colored
desired_cap = {
    "uuid": "emulator-5554",
    "platformName": "Android",
    "appPackage": "com.example.flutter_cuoi_ki",
    "automationName": "UiAutomator2"
}

print(colored('Chương trình bắt đầu chạy', 'green'))
print('===============')
driver = webdriver.Remote("http://localhost:1111/wd/hub", desired_cap)
driver.implicitly_wait(10)

app = driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="flutter_cuoi_ki"]')

# # Mở ứng dụng
app.click()
# # Bấm get started

driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="GET STARTED"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Sign Up"]').click()

def registerTest(name, email, age, password, comfirmPassword,content,test):
    nameTextR = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
    emailTextR = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    ageTextR = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[3]')
    passwordTextR = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[4]')
    comfirmPasswordTextR = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[5]')
    submitRegister = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]')

    nameTextR.click()
    time.sleep(0.5)
    nameTextR.clear()
    time.sleep(0.5)
    nameTextR.send_keys(name)
   

    emailTextR.click()
    time.sleep(0.5)
    emailTextR.clear()
    time.sleep(0.5)
    emailTextR.send_keys(email)
  

    ageTextR.click()
    time.sleep(0.5)
    ageTextR.clear()
    time.sleep(0.5)
    ageTextR.send_keys(age)
  

    passwordTextR.click()
    time.sleep(0.5)
    passwordTextR.clear()
    time.sleep(0.5)
    passwordTextR.send_keys(password)
 

    comfirmPasswordTextR.click()
    time.sleep(0.5)
    comfirmPasswordTextR.clear()
    time.sleep(0.5)
    comfirmPasswordTextR.send_keys(comfirmPassword)
 

    submitRegister.click()
    time.sleep(2)
    check = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')

    if(check.get_attribute('text') == content):
        print(colored(test, 'cyan'))
        print(colored('PASS', 'green'))
        print("=============")
    else:
        print(colored(test, 'cyan'))
        print(colored("FAIL: " + check.get_attribute('text'), 'red'))
        print("=============")
    
# Nhập đúng các trường với name và password đều >=6 và <=20 kí tự, age có thể để trống, email chưa đăng kí trước đó, password bằng với confirm password.
registerTest('Hồ Đức An','hda1@gmail.com','20','testcase','testcase','Đăng kí thành công','Testcase Regiter 1')

# Nhập đúng các trường nhưng email đã được đăng kí trước đó
registerTest('Trần Tấn Cẩn','hda1@gmail.com','25','testcase','testcase','Email này đã được đăng ký ở một tài khoản khác','Testcase Regiter 2')

# Nhập thiếu kí tự name có 5 kí tự, những trường còn lại đều đúng
registerTest('12345','hda3@gmail.com','25','testcase','testcase','Chiều dài tên không hợp lệ, vui lòng nhập từ 6 đến 20 kí tự','Testcase Regiter 3')

# Nhập đủ kí tự name có 6 kí tự, những trường còn lại đều đúng
registerTest('Nghiem1','hda4@gmail.com','25','testcase','testcase','Đăng kí thành công','Testcase Regiter 4')

# Nhập thiếu kí tự password có 5 kí tự, những trường còn lại đều đúng
registerTest('ho an 2k2','hda5@gmail.com','25','12345','12345','Chiều dài password không hợp lệ, vui lòng nhập từ 6 đến 20 kí tự','Testcase Regiter 5')

# Nhập đủ kí tự password có 6 kí tự, những trường còn lại đều đúng
registerTest('ho an 2k2','hda6@gmail.com','25','123456','123456','Đăng kí thành công','Testcase Regiter 6')

# Nhập dư kí tự name hơn 20 kí tự, những trường còn lại đều đúng
registerTest('01234567890123456789012','hda7@gmail.com','25','123456','123456','Chiều dài tên không hợp lệ, vui lòng nhập từ 6 đến 20 kí tự','Testcase Regiter 7')

# Nhập đủ kí tự name có 20 kí tự, những trường còn lại đều đúng
registerTest('01234567890123456789','hda8@gmail.com','25','123456','123456','Đăng kí thành công','Testcase Regiter 8')

# Nhập dư kí tự password hơn 20 kí tự, những trường còn lại đều đúng
registerTest('testcase9','hda9@gmail.com','25','01234567890123456789012','01234567890123456789012','Chiều dài password không hợp lệ, vui lòng nhập từ 6 đến 20 kí tự','Testcase Regiter 9')

# Nhập đủ kí tự password có 20 kí tự, những trường còn lại đều đúng
registerTest('testcase9','hda10@gmail.com','25','01234567890123456789','01234567890123456789','Đăng kí thành công','Testcase Regiter 10')

# Nhập confrirm password không giống password có 20 kí tự, những trường còn lại đều đúng
registerTest('testcase9','hda11@gmail.com','25','abcdefg','abcdef','Password nhập lại không chính xác','Testcase Regiter 11')

time.sleep(0.5)
driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="Sign In"]').click()




def loginTest(email,password,content,test):
    textEmailL = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
    textPasswordL = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText[2]')
    submitLogin = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]')
    time.sleep(0.5)
    textEmailL.click()
    time.sleep(0.5)
    textEmailL.clear()
    time.sleep(0.5)
    textEmailL.send_keys(email)
    time.sleep(0.5)

    textPasswordL.click()
    time.sleep(0.5)
    textPasswordL.clear()
    time.sleep(0.5)
    textPasswordL.send_keys(password)
    time.sleep(0.5)

    submitLogin.click()
    time.sleep(2)
    check = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]')
    if(check.get_attribute('text') == content):
        print(colored(test, 'cyan'))
        print(colored('PASS', 'green'))
        print("=============")
    else:
        print(colored(test, 'cyan'))
        print(colored("FAIL: " + check.get_attribute('text'), 'red'))
        print("=============")

# Bổ trống Email
loginTest('','123','Email không được bỏ trống','Testcase Login 1')
# Bổ trống Password
loginTest('hda1@gmail.com','','Mật khẩu không được bỏ trống','Testcase Login 2')
# Nhập trường email sai và password đúng.
loginTest('123','testcase','Email không chính xác!','Testcase Login 3')
# Nhập trường email đúng và password sai.
loginTest('hda1@gmail.com',':VVVVVV','Mật khẩu không chính xác!','Testcase Login 4')
# Nhập các trường email và password đã được đăng kí trước đó.
loginTest('hda1@gmail.com','testcase','Đăng nhập thành công','Testcase Login 5')
print()
print('============')
print(colored('èn, no bờ rô bờ lem', 'blue'))


