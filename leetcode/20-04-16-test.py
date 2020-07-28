#-*- coding:utf-8 -*-
# @author : MaLei
# @datetime : 2019-14-16 15:18
# @file : 20-04-16-test.py
# @software : PyCharm

'''
题目：有一张用户签到表【t_user_attendence】，标记每天用户是否签到（说明：该表包含所有用户所有工作日的出勤记录） ，

包含三个字段：日期【fdate】，用户id【fuser_id】，用户当天是否签到【fis_sign_in：0否1是】；


问题1：请计算截至当前每个用户已经连续签到的天数（输出表仅包含当天签到的所有用户，计算其连续签到天数）

输出表【t_user_consecutive_days】:用户id【fuser_id】，用户联系签到天数【fconsecutive_days】



问题2：请计算每个用户历史以来最大的连续签到天数（输出表为用户签到表中所有出现过的用户，计算其历史最大连续签到天数）

输出表【t_user_max_days】:用户id【fuser_id】，用户最大连续签到天数【fmax_days】
'''