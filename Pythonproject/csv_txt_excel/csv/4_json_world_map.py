import json
import pygal_maps_world.maps as pyg
import pygal.style
from e_country_codes import get_country_code

#加载数据
filname='population_data.json'
with open(filname) as f:
    # json.load()将数据转换成列
    # 便于python进行处理
    pop_data=json.load(f)

cc_population={}
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code =get_country_code(country_name)
        if code:
            cc_population[code]=population


# 根据人口数量将所有的国家分为三组
cc_pops1,cc_pops2,cc_pops3={},{},{}
for cc,pop in cc_population.items():
    if pop<10000000:
        cc_pops1[cc]=pop
    elif pop<1000000000:
        cc_pops2[cc]=pop
    else:
        cc_pops3[cc]=pop
print(len(cc_pops1),len(cc_pops2),len(cc_pops3))

#wm=pyg.World()
#wm_style=RoteStyle('#336699')
wm_style=pygal.style.RotateStyle('#3399AA',base_style=pygal.style.LightColorizedStyle)
wm=pyg.World(style=wm_style)
wm.title = 'World Population in 2010,by Countries'
wm.add('0-10m',cc_pops1)
wm.add('10m-1bn',cc_pops2)
wm.add('>1bn',cc_pops3)


#wm.add('2010', cc_population)

# render_to_file() 创建一个包含该图表的.svg文件
wm.render_to_file('world_population.svg')
"""
        常见错误
File "D:/Python/hoilday_codes/csv/4_json_world_map.py", line 13, in <module>
Caribbean small states:6880000
    population = int(pop_dict['Value'])
East Asia & Pacific (all income levels):2201536674
ValueError: invalid literal for int() with base 10: '1127437398.85751'
        错误原因：
python 不能直接将包含小数点的字符串转换成整数
我们可以先将字符串转换为浮点数，再将浮点数转换成整数
更改方法：
population = int(pop_dict['Value'])
改为 population = int(float(pop_dict['Value']))


"""