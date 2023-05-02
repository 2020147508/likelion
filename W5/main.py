import datetime
import re

def create_membership():
	# 아래 코드는 python에 내장되어 있는 datetime 모듈을 활용하여 오늘 날짜를 입력하는 코드입니다. 
	# stnr_date 코드는 제가 작성했으니, 건드리지 않으셔도 되옵니다 :)
    now = datetime.datetime.now()
    stnr_date = now.strftime('%Y%m%d')
    
    users = []
    # user 딕셔너리에 username, password, email을 아래 주어진 제한 조건에 알맞게 입력받는 코드를 작성하세요.
	# user 딕셔너리 값에는 username, password, email, stnr_date 총 4가지 값이 저장되어야 합니다.
    while True:
        user = {}
        while True :
            input_id = input("ID를 입력하세요: ")
            korean_checking = re.match('^[ㄱ-힣]{2,4}$', input_id)
            if korean_checking:
                user['id'] = input_id
                break
            else:
                print("2~4글자의 한글만 입력해 주세요.")

        while True :
            input_password = input("Password를 입력하세요: ")
            if input_password[0].isupper() and len(input_password) >= 8 and ('!' in input_password or '@' in input_password or '#' in input_password or '$' in input_password):
                user['password'] = input_password
                break
            else:
                print("첫 문자가 영문 대문자이고, 총 글자 수가 8글자 이상이고, 특수문자 (!, @, #, $) 중 1가지를 반드시 포함하는 비밀번호를 입력해 주세요.")

        while True :
            input_email = input("Email을 입력하세요: ")
            if input_email.endswith(".com"):
                input_email_check = input_email.replace("@", '')[0:-4]
                input_email_checking = re.match('^[a-zA-Z0-9]+$', input_email_check)
                if input_email_checking:
                    user['email'] = input_email
                    break
                else:
                    print("이메일 주소는 오직 숫자와 영문으로만 이루어 져야 하고, @를 제외한 특수문자는 입력될 수 없습니다.")
            else:
                print(".com으로 끝나는 이메일 주소를 입력하세요.")

        user['stnr_date'] = stnr_date
        
        users.append(user)

        continue_or_not = input("사용자를 추가로 등록하고 싶으신가요? (Y/N)")
        if (continue_or_not == 'Y'):
            continue
        else:
            return users
    

"""
id 제한 조건
- 한글만 입력 받아야 함
- 총 글자 수는 2-4글자

password 제한 조건
- 첫 문자는 영문 대문자
- 총 글자 수는 8글자 이상
- 특수문자 (!, @, #, $) 중 1가지 반드시 포함

email 제한 조건
- @를 제외한 특수문자는 입력될 수 없음 (입력 가능한 문자는 숫자와 영문)
- 통상적인 email 포맷을 따름
  * @을 포함하고, '.com'으로 이메일 주소가 끝나야 함
  

/데이터 예시/
{홍산하, asdf1234!, sannah@naver.com, 20230427}
{김한준, q1w2e3r4!, zhivagokim@naver.com, 20230427}
{천승범, zxcv4860!, vision6@naver.com, 20230427}

반복문과 조건문을 잘 활용하여, 사용자가 입력을 중단할 때까지 입력 받을 수 있도록 코드를 작성할 것
"""


def load_to_txt(user_list):
    f = open('memberdb.txt', 'w', encoding='UTF-8')
    # user_list에 있는 user 3명의 딕셔너리 값을 txt에 작성하세요.
	# 올바르게 생성된 텍스트 파일의 예시는 상단에 이미지로 첨부되어 있습니다.
    if len(user_list) < 3:
        for i in range(len(user_list)):
            f.write(f"{user_list[i]['id']}, {user_list[i]['password']}, {user_list[i]['email']}, {user_list[i]['stnr_date']}\n")
    else:
        for i in range(0, 3):
            f.write(f"{user_list[i]['id']}, {user_list[i]['password']}, {user_list[i]['email']}, {user_list[i]['stnr_date']}\n")
    f.close()
    
def run():
	# 위에서 정의한 create_membership 함수가 실행되어 반환된 결과값을 user_list 객체에 저장합니다.
    user_list = create_membership()
    # 위에 생성된 user_list 객체를 load_to_txt 함수의 입력변수로 활용하여 txt 파일을 생성합니다.
    load_to_txt(user_list)
    
run()