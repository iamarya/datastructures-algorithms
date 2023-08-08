<div _ngcontent-serverapp-c231="" class="note-body"><div _ngcontent-serverapp-c231="" class="body-text"><h2><strong>ChainMap</strong></h2><p>&nbsp;</p><p>A ‘ChainMap’ groups multiple dictionaries or other mappings together to create a single, updateable view. If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.</p><p>A ‘ChainMap’ class is provided for quickly linking a number of mappings so they can be treated as a single unit. It is often much faster than creating a new dictionary and running multiple update() calls.</p><p>A ChainMap basically encapsulates many dictionaries into a single unit and returns a list of dictionaries.</p><p>&nbsp;</p><p><strong>Syntax:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">collections</span>.<span class="hljs-title">ChainMap</span>(<span class="hljs-params">dict1, dict2, dict3,...</span>)</span></code></pre><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program to demonstrate </span>
<span class="hljs-comment"># ChainMap </span>


<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> ChainMap 
<span class="hljs-comment"># winnings of different</span>

d1 = {<span class="hljs-string">'JS'</span>: <span class="hljs-string">'ReactJS'</span>, <span class="hljs-string">'TS'</span>: <span class="hljs-string">'ReactTS'</span>} 
d2 = {<span class="hljs-string">'JS'</span>: <span class="hljs-string">'NodeJS'</span>, <span class="hljs-string">'TS'</span>: <span class="hljs-string">'DenoJS'</span>} 
d3 = {<span class="hljs-string">'JS'</span>: <span class="hljs-string">'AngularJS'</span>, <span class="hljs-string">'TS'</span>: <span class="hljs-string">'Angular'</span>} 
<span class="hljs-comment"># Defining the chainmap </span>
c = ChainMap(d1, d2, d3) 

print(c)</code></pre><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">ChainMap({<span class="hljs-string">'TS'</span>: <span class="hljs-string">'ReactTS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'ReactJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'DenoJS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'NodeJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'Angular'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'AngularJS'</span>})</code></pre><p>&nbsp;</p><p><strong>Accessing Keys and Values from ChainMap</strong></p><p>Values from ChainMap can be accessed using the key name. They can also be accessed by using the keys() and values() method.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># Python program to demonstrate </span>
<span class="hljs-comment"># ChainMap </span>


<span class="hljs-keyword">from</span> collections <span class="hljs-keyword">import</span> ChainMap 
<span class="hljs-comment"># winnings of different</span>

d1 = {<span class="hljs-string">'JS'</span>: <span class="hljs-string">'ReactJS'</span>, <span class="hljs-string">'TS'</span>: <span class="hljs-string">'ReactTS'</span>} 
d2 = {<span class="hljs-string">'JS'</span>: <span class="hljs-string">'NodeJS'</span>, <span class="hljs-string">'TS'</span>: <span class="hljs-string">'DenoJS'</span>} 
d3 = {<span class="hljs-string">'JS'</span>: <span class="hljs-string">'AngularJS'</span>, <span class="hljs-string">'TS'</span>: <span class="hljs-string">'Angular'</span>} 
<span class="hljs-comment"># Defining the chainmap </span>
c = ChainMap(d1, d2, d3) 

<span class="hljs-comment"># Accessing Values using key name </span>
print(c[<span class="hljs-string">'TS'</span>]) 

<span class="hljs-comment"># Accesing values using values() </span>
<span class="hljs-comment"># method </span>
print(c.values()) 

<span class="hljs-comment"># Accessing keys using keys() </span>
<span class="hljs-comment"># method </span>
print(c.keys())</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">ReactTS                                                                                                                       
ValuesView(ChainMap({<span class="hljs-string">'TS'</span>: <span class="hljs-string">'ReactTS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'ReactJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'DenoJS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'NodeJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'Angular'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'AngularJS'</span>}
))                                                                                                                            
KeysView(ChainMap({<span class="hljs-string">'TS'</span>: <span class="hljs-string">'ReactTS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'ReactJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'DenoJS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'NodeJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'Angular'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'AngularJS'</span>}))</code></pre><p>&nbsp;</p><p><strong>Adding new dictionary</strong></p><p>A new dictionary can be added by using the <strong>new_child()</strong> method. The newly added dictionary is added at the beginning of the ChainMap.</p><p>&nbsp;</p><p><strong>Example:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs"><span class="hljs-comment"># printing chainMap </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"All the ChainMap contents are : "</span>) 
<span class="hljs-keyword">print</span> (chain) 

<span class="hljs-comment"># using new_child() to add new dictionary </span>
chain1 = chain.new_child(dic3) 

<span class="hljs-comment"># printing chainMap </span>
<span class="hljs-keyword">print</span> (<span class="hljs-string">"Displaying new ChainMap : "</span>) 
<span class="hljs-keyword">print</span> (chain1)</code></pre><p>&nbsp;</p><p><strong>Output:</strong></p><p>&nbsp;</p><pre><code class="language-python hljs">All the ChainMap contents are :                                                                                               
ChainMap({<span class="hljs-string">'TS'</span>: <span class="hljs-string">'ReactTS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'ReactJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'DenoJS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'NodeJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'Angular'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'AngularJS'</span>})          
Displaying new ChainMap :                                                                                                     
ChainMap({<span class="hljs-string">'TS'</span>: <span class="hljs-string">'VueTS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'VueJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'ReactTS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'ReactJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'DenoJS'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'NodeJS'</span>}, {<span class="hljs-string">'TS'</span>: <span class="hljs-string">'Angular
'</span>, <span class="hljs-string">'JS'</span>: <span class="hljs-string">'AngularJS'</span>}) </code></pre></div></div>