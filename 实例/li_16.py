#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ��Ŀ�����ָ����ʽ������
# ���������ʹ�� datetime ģ��
 
import datetime
 
if __name__ == '__main__':
 
    # ����������ڣ���ʽΪ dd/mm/yyyy������ѡ����Բ鿴 strftime() ����
    print(datetime.date.today().strftime('%d/%m/%Y'))
 
    # �������ڶ���
    miyazakiBirthDate = datetime.date(1941, 1, 5)
 
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
 
    # ������������
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
 
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))
 
    # �����滻
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
 
    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))