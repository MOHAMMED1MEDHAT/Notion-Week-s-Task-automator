#the flow: for each task in the list ->
#hover over the btn -> 
#   click settings btn ->
#       click the name txtbx.set_attribute("{taskName}")    
#       XPATH{//*/div[@class="notion-focusable-within"]/div} ->
#           click the status dropdownBtn
#           XPATH{//*/div[2][@class="notion-scroller vertical"]/div/div/div/div/div/div/div[2]/div[4]} ->
#           click not-started-option
#           XPATH{//*/div[@id=":r3i:"]} ->
#           click chooseDate dropdownBtn
#           XPATH{//*/div[2][@class="notion-scroller vertical"]/div/div/div/div/div/div/div[2]/div[6]} ->
#           click pickDate btn
#           XPATH{//*/footer/div} ->
#           set_attribute("text","Dec 20,2023")
#           XPATH{//*/div[@role="dialog"]/div/div[2]/div/div/div/div/input} ->
#           click done btn 
#           XPATH{//*/div[2][text()="Done"]} ->
#           click chooseType dropdownBtn
#           XPATH{//*/div[2][@class="notion-scroller vertical"]/div/div/div/div/div/div/div[2]/div[8]} ->
#           click typeOption
#           XPATH{//*/span[text()=config.TaskTypes[0]]}
#           XPATH{//*/span[text()=config.TaskTypes[1]]}
#           XPATH{//*/span[text()=config.TaskTypes[2]]}
#           XPATH{//*/span[text()=config.TaskTypes[3]]}
#           XPATH{//*/span[text()=config.TaskTypes[4]]}
#           XPATH{//*/span[text()=config.TaskTypes[5]]}
#           XPATH{//*/span[text()=config.TaskTypes[6]]}
#           XPATH{//*/span[text()=config.TaskTypes[7]]} ->
#           click save btn
#           XPATH{//*/div[text()="Done"]} ->
#           click create task btn
#           XPATH{//*/div[text()="Create task"]} 
#
#           
#
#
#
#
#