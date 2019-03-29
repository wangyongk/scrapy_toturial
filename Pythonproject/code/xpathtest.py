from lxml import etree

wb_data = """
        <div>
            <ul>
                 <li class="item-0"><a href="link1.html">first item</a></li>
                 <li class="item-1"><a href="link2.html">second item</a></li>
                 <li class="item-inactive"><a href="link3.html">third item</a></li>
                 <li class="item-1"><a href="link4.html">fourth item</a></li>
                 <li class="item-0"><a href="link5.html">fifth item</a>
             </ul>
         </div>
        """
html=etree.HTML(wb_data)
print(html)

result =etree.tostring(html)
print(result.decode("utf-8"))

html_data=html.xpath('/html/body/div/ul/li/a')
for i in html_data:
    print(i.text)
print("----------------------------------1")
html_data = html.xpath('/html/body/div/ul/li/a/text()')
for i in html_data:
    print(i)

print("----------------------------------2")
html_data=etree.tostring(html,pretty_print=True)
res=html_data.decode("utf-8")
'''print(html_data)'''
print(res)
print("-----------我是分割线--------3")
html=etree.HTML(wb_data)
html_data = html.xpath('/html/body/div/ul/li/a/@href')
for i in html_data:
    print(i)
