import pygal_maps_world.maps as pyg

wm=pyg.World()
wm.title = 'Population of Countries in North America'
wm.add('North America', {'ca':34126000, 'mx':113423000, 'us':309349000})

# render_to_file() 创建一个包含该图表的.svg文件
wm.render_to_file('num_population.svg')