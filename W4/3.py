score = {}
sum=0 #평균을 구하기 위해 학생들 점수의 총합이 담길 변수

score["철수"] = 98
score["영희"] = 80
score["순이"] = 100
score["돌이"] = 70

print(score)
print(len(score))

del score["철수"]
del score["영희"]
del score["순이"]
del score["돌이"]

print(score)
print(len(score))

score = dict(철수 = 98, 영희 = 80, 순이 = 100, 돌이 = 70)

print(score)
print(len(score))

for v in score.values():
	sum+=v

#학생들의 점수 평균 출력
print(sum/len(score))

score.clear()
print(score)
print(len(score))