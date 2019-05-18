# 목표 : 
#형태는 분:초
#이걸로 인풋이 위의 형태로 주어졌을때
#총합을 분초로 계산해 내어라.
#------
#리스트를 만든다 => 분의 리스트, 초의 리스트를 만든다 => 분끼리 모아서 더해서 분에 넣고 
#=> 초끼리 더해서 60으로 나눈 몫은 분 값에 더하고 => 나머지를 초에 넣는다 => 그것을 다시 \s:\s를 사이에 두고 조인한다.

total_min = 0
total_sec = 0
more = 'y'

while more == 'y':
	min_sec_str = input('interval? in xx:xx format')
	min_sec_list = min_sec_str.split(':')
	total_min += int(min_sec_list[0])
	total_sec += int(min_sec_list[1])
	more = input('have more? [y]/[n]')

print(f'the total interval is {str(total_min+total_sec//60)}:{str(total_sec%60)}')

print('i love you.')

print('Visca El Barca')
