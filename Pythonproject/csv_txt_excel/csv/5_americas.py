import pygal_maps_world.maps as pyg

# 创建一个World实例
wm=pyg.World()

#设置了地图的title属性
wm.title = 'North, Central, and South America'

# 使用 add() 它接受一个标签和列表
# 列表突出国家的国别码。每次调用add()都将为指定的
#国家选择一种颜色，并在图标左边显示该颜色和指定的标签
wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy',
                         'pe', 'py', 'sz', 'uy', 've'])

# render_to_file() 创建一个包含该图表的.svg文件
wm.render_to_file('americas.svg')