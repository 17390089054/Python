from die import Die
import pygal

#创建一个D6和一个D10
die_1=Die()
die_2=Die(10)

#掷多次筛子 并将结果存储到一个列表中
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)
    
#分析结果
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
    frequency=results.count(value)
    frequencies.append(frequency)


#可视化结果
hist=pygal.Bar()

hist.title="Result of rolling  D6 and D10 dice 1000 times."
hist.x_labels=[x for x in range(2,17)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('different_visual.svg')
