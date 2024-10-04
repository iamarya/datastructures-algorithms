<div _ngcontent-serverapp-c318="" class="body-text p-24"><p><span style="font-size:17pt;"><strong>Hash Maps</strong></span></p><p>&nbsp;</p><p><span style="font-size:11pt;">Hash maps are the most important data structures used in computer science. They are&nbsp;<strong>key value</strong> paired data structures.&nbsp;</span></p><p>&nbsp;</p><p><span style="font-size:13.999999999999998pt;"><strong>Key</strong></span><span style="font-size:11pt;"><strong>&nbsp;</strong></span></p><p><span style="font-size:11pt;">A key is an entity for which we want to store some data.&nbsp;</span></p><p>&nbsp;</p><p><span style="font-size:13.999999999999998pt;"><strong>Value</strong></span><span style="font-size:11pt;"><strong>&nbsp;</strong></span></p><p><span style="font-size:11pt;">The data which is stored for a particular key is called value.</span></p><p>&nbsp;</p><p><span style="font-size:13.999999999999998pt;"><strong>Types of Hash Maps</strong></span></p><ol><li><span style="font-size:11pt;">Unordered Maps</span></li><li><span style="font-size:11pt;">Ordered Maps</span></li></ol><p><span style="font-size:11pt;">&nbsp;</span></p><p>&nbsp;</p><p><span style="font-size:13.999999999999998pt;"><strong>Unordered Map</strong></span></p><ol><li><span style="font-size:11pt;">It is declared as&nbsp;<strong>unordered_map&lt;T,U&gt;</strong> where T and U are the data types.&nbsp;</span></li><li><span style="font-size:11pt;">Here T represents the&nbsp;<strong>Key.</strong></span></li><li><span style="font-size:11pt;">Here U represents the&nbsp;<strong>Value.</strong></span></li><li><span style="font-size:11pt;">In unordered map, we can put anything in terms of value. (It can be data type like integer, character, float or even any data structure like vector, array, set etc).</span></li><li><span style="font-size:11pt;">But, in terms of key, we can only put data types like integer, character, float and not any data structure.</span></li><li><span style="font-size:11pt;">The default value of any key in the unordered_map is&nbsp;<strong>zero</strong>.</span></li></ol><p style="margin-left:36pt;"><span style="font-size:11pt;"><img src="https://files.codingninjas.in/article_images/hashmaps-dsa-new-0-1702465725.webp"></span></p><p>&nbsp;</p><p><span style="font-size:11pt;"><strong>Operations in Unordered Map</strong></span></p><ol><li><span style="font-size:11pt;"><strong>Insertion -&nbsp;Inserting any new key into the data structure with any value. Let us consider key to be integer type and value also to be integer type. Then insertion will be done as&nbsp;map[key] = value.&nbsp;</strong></span></li><li><span style="font-size:11pt;"><strong>Updation -&nbsp;Updating the current value of a key to a new value. Again it will be done as&nbsp;map[key] = new_value. If the key is not already present, it will insert it with new_value otherwise the previous value will be updated to new_value.</strong></span></li><li><span style="font-size:11pt;"><strong>Size -&nbsp;It returns the size of the hashmap. It actually determines how many keys are present in the hashmap.</strong></span></li><li><span style="font-size:11pt;"><strong>Searching -&nbsp;We can also search a particular key and its corresponding value in the map. It is done by&nbsp;map[key].&nbsp;This will return the value of the key passed.</strong></span></li></ol><p><span style="font-size:11pt;"><strong>All the operations have time complexity - O(1)</strong></span></p><p>&nbsp;</p><p>&nbsp;</p><p><span style="font-size:13.999999999999998pt;"><strong>Map</strong></span></p><ol><li><span style="font-size:11pt;">It is declared as&nbsp;<strong>map&lt;T,U&gt;</strong> where T and U are the data types.&nbsp;</span></li><li><span style="font-size:11pt;">Here T represents the&nbsp;<strong>Key.</strong></span></li><li><span style="font-size:11pt;">Here U represents the&nbsp;<strong>Value.</strong></span></li><li><span style="font-size:11pt;">In a map, we can put anything in terms of value. (It can be data type like integer, character, float or even any data structure like vector, array, set etc).</span></li><li><span style="font-size:11pt;">Here, the key can also be anything. (It can be data type like integer, character, float or even any data structure like vector, array, set etc).</span></li><li><span style="font-size:11pt;">The default value of any key in the unordered_map is&nbsp;<strong>zero</strong>.</span></li></ol><p>&nbsp;</p><p style="text-align:center;"><span style="font-size:11pt;"><strong><img src="https://files.codingninjas.in/article_images/hashmaps-dsa-new-1-1702465726.webp"></strong></span></p><p>&nbsp;</p><p><span style="font-size:11pt;"><strong>Notice, we can not use vector&lt;char&gt; as the key in unordered_map because it is a data structure and not a data type.</strong></span></p><p>&nbsp;</p><p><span style="font-size:11pt;">All the operations in unordered_map are also applicable in maps.</span></p><p><span style="font-size:11pt;"><strong>The time complexity of operations in the map is O(logn).</strong></span></p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p><span style="font-size:13.999999999999998pt;"><strong>Difference between maps and unordered_maps</strong></span></p><p>&nbsp;</p><p>&nbsp;</p><figure class="table" style="float:left;width:451.27559055118115pt;"><table class="ck-table-resized" style="width: 100%;"><colgroup><col style="width:50%;"><col style="width:50%;"></colgroup><tbody><tr><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">Maps</span></td><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">Unordered Maps</span></td></tr><tr><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">The time complexity of insertion, updation, and searching is&nbsp;<strong>Logarithmic</strong>.</span></td><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">The time complexity of insertion, updation, and searching is&nbsp;<strong>Constant</strong>.</span></td></tr><tr><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">The value can be of any type - data types or data structures.</span></td><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">The value can be of any type - data types or data structures.</span></td></tr><tr><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">The key can be of any type - data types or data structures.</span></td><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">The key can not be of any type - only primitive data types are allowed to be kept as key. Eg- int, char, float, double etc.</span></td></tr><tr><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">Handles the occurrence of collisions efficiently as it has a&nbsp;<strong>strong</strong> hash function.&nbsp;</span></td><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">It has a&nbsp;<strong>weak</strong> hash function. Thus, occurrence of collisions increases rapidly in complex implementations.</span></td></tr><tr><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">It uses a balanced&nbsp;<strong>Binary Search Tree</strong> for internal implementation.</span></td><td style="border:1pt solid #000000;padding:5pt;vertical-align:top;"><span style="font-size:11pt;">It uses a&nbsp;<strong>pair of keys and values</strong> for internal implementation.</span></td></tr></tbody></table></figure><p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p><p><span style="font-size:11pt;"><strong>&nbsp;</strong></span></p><p>&nbsp;</p></div>